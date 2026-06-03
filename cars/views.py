from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CarForm, RegisterForm, MessageForm
from .models import Car, Brand, Favorite, Message


def home(request):
    featured_cars = Car.objects.select_related('brand', 'owner').filter(is_featured=True)[:6]
    suv_cars = Car.objects.select_related('brand', 'owner').filter(vehicle_type='SUV')[:4]
    sedan_cars = Car.objects.select_related('brand', 'owner').filter(vehicle_type='Sedan')[:4]
    brands = Brand.objects.all()

    total_cars = Car.objects.count()
    active_cars = Car.objects.filter(is_active=True).count()
    archived_cars = Car.objects.filter(is_active=False).count()
    featured_count = Car.objects.filter(is_featured=True).count()
    total_messages = Message.objects.count()
    total_favorites = Favorite.objects.count()

    context = {
        'featured_cars': featured_cars,
        'suv_cars': suv_cars,
        'sedan_cars': sedan_cars,
        'brands': brands,
        'total_cars': total_cars,
        'active_cars': active_cars,
        'archived_cars': archived_cars,
        'featured_count': featured_count,
        'total_messages': total_messages,
        'total_favorites': total_favorites,
    }
    return render(request, 'cars/home.html', context)


def car_list(request):
    cars = Car.objects.select_related('brand', 'owner').filter(is_active=True)
    brands = Brand.objects.all()

    q = request.GET.get('q')
    brand = request.GET.get('brand')
    vehicle_type = request.GET.get('vehicle_type')

    if q:
        cars = cars.filter(
            Q(title__icontains=q) |
            Q(model__icontains=q) |
            Q(brand__name__icontains=q) |
            Q(description__icontains=q)
        )

    if brand:
        cars = cars.filter(brand_id=brand)

    if vehicle_type:
        cars = cars.filter(vehicle_type=vehicle_type)

    context = {
        'cars': cars,
        'brands': brands,
    }
    return render(request, 'cars/car_list.html', context)


def car_detail(request, pk):
    car = get_object_or_404(Car.objects.select_related('brand', 'owner'), pk=pk)

    is_favorited = False
    if request.user.is_authenticated:
        is_favorited = Favorite.objects.filter(user=request.user, car=car).exists()

    return render(request, 'cars/car_detail.html', {
        'car': car,
        'is_favorited': is_favorited,
    })


@login_required
def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.is_featured = False
            car.is_active = True
            car.save()
            return redirect('site_ads')
    else:
        form = CarForm()

    return render(request, 'cars/car_form.html', {'form': form, 'page_title': 'Add New Car'})


@login_required
def car_update(request, pk):
    car = get_object_or_404(Car, pk=pk)

    if car.owner != request.user and not request.user.is_superuser:
        return redirect('car_detail', pk=car.pk)

    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            updated_car = form.save(commit=False)
            if not request.user.is_superuser:
                updated_car.owner = request.user
                updated_car.is_featured = False
            updated_car.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm(instance=car)

    return render(request, 'cars/car_form.html', {'form': form, 'page_title': 'Edit Car'})


@login_required
def archive_car(request, pk):
    car = get_object_or_404(Car, pk=pk)

    if car.owner != request.user and not request.user.is_superuser:
        return redirect('car_detail', pk=car.pk)

    car.is_active = False
    car.save()
    return redirect('dashboard')


@login_required
def activate_car(request, pk):
    car = get_object_or_404(Car, pk=pk)

    if car.owner != request.user and not request.user.is_superuser:
        return redirect('dashboard')

    car.is_active = True
    car.save()
    return redirect('dashboard')


@login_required
def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)

    if car.owner != request.user and not request.user.is_superuser:
        return redirect('car_detail', pk=car.pk)

    if request.method == 'POST':
        car.delete()
        return redirect('dashboard')

    return render(request, 'cars/car_confirm_delete.html', {'car': car})


def site_ads(request):
    cars = Car.objects.select_related('brand', 'owner').filter(is_featured=False, is_active=True)
    return render(request, 'cars/site_ads.html', {'cars': cars})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def signout_view(request):
    logout(request)
    return redirect('home')


@login_required
def send_message(request, pk):
    car = get_object_or_404(Car.objects.select_related('owner', 'brand'), pk=pk)

    if not car.owner or car.owner == request.user:
        return redirect('car_detail', pk=car.pk)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = car.owner
            message.car = car
            message.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = MessageForm()

    return render(request, 'cars/send_message.html', {'form': form, 'car': car})


@login_required
def toggle_favorite(request, pk):
    car = get_object_or_404(Car, pk=pk)

    if car.owner == request.user:
        return redirect('car_detail', pk=car.pk)

    favorite = Favorite.objects.filter(user=request.user, car=car).first()

    if favorite:
        favorite.delete()
    else:
        Favorite.objects.create(user=request.user, car=car)

    return redirect('car_detail', pk=car.pk)


@login_required
def dashboard(request):
    user = request.user

    active_ads = Car.objects.filter(owner=user, is_active=True)
    past_ads = Car.objects.filter(owner=user, is_active=False)
    incoming_messages = Message.objects.filter(receiver=user)
    favorite_items = Favorite.objects.filter(user=user)

    context = {
        'active_ads': active_ads,
        'past_ads': past_ads,
        'incoming_messages': incoming_messages,
        'favorite_items': favorite_items,
        'active_ads_count': active_ads.count(),
        'past_ads_count': past_ads.count(),
        'messages_count': incoming_messages.count(),
        'favorites_count': favorite_items.count(),
    }
    return render(request, 'cars/dashboard.html', context)
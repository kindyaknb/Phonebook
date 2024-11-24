from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Contact, Review
from .forms import ContactForm, UserRegisterForm, ReviewForm

@login_required
def contact_list(request):
    messages.info(request, "Будь ласка, увійдіть, щоб додати контакти.")
    contacts = Contact.objects.all()
    return render(request, 'phonebook/contact_list.html', {'contacts': contacts})

def base(request):
    return render(request, 'phonebook/base.html')

@login_required
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'phonebook/add_contact.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт створено для {username}! Ви можете увійти.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'phonebook/register.html', {'form': form})

# Вкладка "Відгуки"
def reviews_page(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш відгук успішно додано!')
            return redirect('reviews')  # Ім'я URL має бути коректним
    else:
        form = ReviewForm()

    reviews = Review.objects.all()
    return render(request, 'phonebook/reviews.html', {'reviews': reviews, 'form': form})

def reviews_view(request):
    # Отримуємо всі відгуки з бази даних
    reviews = Review.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Якщо форма дійсна, зберігаємо відгук в базу даних
            form.save()
            # Перенаправляємо на сторінку відгуків після успішного додавання
            return redirect('reviews')  # 'reviews' - ім'я URL для сторінки відгуків
    else:
        form = ReviewForm()

    return render(request, 'phonebook/reviews.html', {
        'reviews': reviews,
        'form': form,
    })
@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Відгук було успішно видалено.')
        return redirect('reviews')  # Повернення на сторінку "Відгуки"
    return render(request, 'phonebook/delete_review.html', {'review': review})
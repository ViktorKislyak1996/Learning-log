from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def register(request):
    # Регистрирует нового пользователя
    if request.method != 'POST':
        # Выводит пустую форму регистрации
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Выполнение входа и перенаправление на домашнюю страницу
            login(request, new_user)
            return redirect('learning_logs_app:index')


    context = {'form': form}
    return render(request, 'registration/register.html', context)
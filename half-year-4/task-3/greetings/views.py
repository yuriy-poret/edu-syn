from django.shortcuts import render #, redirect
from .forms import NameForm


def index(request):
    message = None
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            message = f"Привет, {name}! Ваше имя сохранено."
            form = NameForm()  # Очищаем форму после успешной отправки
    else:
        form = NameForm()

    return render(request, 'greetings/index.html', {'form': form, 'message': message})

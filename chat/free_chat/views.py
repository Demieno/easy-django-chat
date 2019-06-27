from django.shortcuts import render, redirect
from .models import Message
from .foms import MessageForm


def message(request):
    massage_list = Message.objects.all()
    message_form = MessageForm(request.POST)
    if request.method == 'POST':
        if message_form.is_valid():
            message_form.save()
            return redirect(request.get_full_path())

    return render(request, 'index.html', locals())

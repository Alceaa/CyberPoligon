from math import trunc

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.context_processors import request

from .forms import ImageForm
from .function import sanitaizer_text


def init(request):
    return render(
            request,
            'post.html'
        )

def creat_post(request):
    text = ''
    if request.method == "POST":
        form = request.POST.get("confirmationText")
        text = sanitaizer_text(form)
        print(form)
        print(text)
        # return redirect('view_post', text=text)
    return render(request, 'post.html', {'texts': text})

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'empty.html')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})
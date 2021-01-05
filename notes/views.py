from django.shortcuts import render, redirect
from django.http import HttpResponse
from notes.forms import RegisterForm, NoteForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'notes/index.html')


def register(req):
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            pw = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=pw)
            login(req, user)
            return redirect('notes:index')
    else:
        form = RegisterForm()
    return render(req, 'notes/register.html', {'form': form})


@login_required
def new(req):
    form = NoteForm()
    return render(req, 'notes/newNote.html', {'form': form})

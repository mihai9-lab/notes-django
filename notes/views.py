from django.shortcuts import render, redirect
from django.http import HttpResponse
from notes.forms import RegisterForm, NoteForm
from notes.models import Note
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(req):
    return render(req, 'notes/index.html')


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
    if req.method == 'POST':
        form = NoteForm(req.POST)
        if form.is_valid():
            note = Note(name=form.cleaned_data.get('name'), content=form.cleaned_data.get('content'), colorText=form.cleaned_data.get(
                'colorText'), colorBackground=form.cleaned_data.get('colorBackground'), fontSize=form.cleaned_data.get('fontSize'), userId=req.user)
            note.save()
            return redirect('notes:home')
    else:
        form = NoteForm()
    return render(req, 'notes/newNote.html', {'form': form})


@login_required
def home(req):
    notes = Note.objects.filter(userId=req.user.id, completed=False)
    return render(req, 'notes/home.html', {'notes': notes})

@login_required
def completed(req):
    notes = Note.objects.filter(userId=req.user.id, completed=True)
    return render(req, 'notes/completed.html', {'notes': notes})


@login_required
def edit(req, id):
    try:
        note = Note.objects.get(id=id, userId=req.user.id, completed=False)
        if req.method == 'POST':
            form = NoteForm(req.POST)
            if form.is_valid():
                note.name = form.cleaned_data.get('name')
                note.content = form.cleaned_data.get('content')
                note.colorText = form.cleaned_data.get('colorText')
                note.colorBackground = form.cleaned_data.get('colorBackground')
                note.fontSize = form.cleaned_data.get('fontSize')
                note.save()
                return redirect('notes:home')
        else:
            form = NoteForm(instance=note)
            return render(req, 'notes/editNote.html', {'form': form, 'id': id})
    except:
        return redirect('notes:home')


@login_required
def complete(req, id):
    try:
        note = Note.objects.get(id=id, userId=req.user.id, completed=False)
        if req.method == 'POST':
            note.completed = True
            note.save()
            return redirect('notes:home')
        else:
            return render(req, 'notes/complete.html', {'note': note, 'id': id})
    except:
        return redirect('notes:home')


@login_required
def delete(req, id):
    try:
        note = Note.objects.get(id=id, userId=req.user.id)
        if req.method == 'POST':
            note.delete()
            return redirect('notes:home')
        else:
            return render(req, 'notes/delete.html', {'note': note, 'id': id})
    except:
        return redirect('notes:home')

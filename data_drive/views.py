from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm, FolderForm, FileForm
from .models import Folder, File
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages

def register(request):
   if request.method == 'POST':
     form = RegistrationForm(request.POST)
     if form.is_valid():
       user = form.save()
       login(request, user)
       return redirect('folder_list')
   else:
     form = RegistrationForm()
   return render(request, 'login_register_form.html', {'form': form, 'page_title': 'Register', 'button_text':'Register'})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('folder_list')
    else:
        form = LoginForm()
    return render(request, 'login_register_form.html', {'form': form, 'page_title': 'Login', 'button_text':'Login'})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def folder_list(request, parent_folder_id=None):
    folders = Folder.objects.filter(owner=request.user, parent=parent_folder_id).order_by('-created_at')
    if parent_folder_id is not None:
       parent_folder = get_object_or_404(Folder, pk=parent_folder_id)
    else:
        parent_folder = None
    return render(request, 'folder_list.html', {'folders': folders, 'parent_folder': parent_folder})

@login_required
def folder_detail(request, folder_id):
    folder = get_object_or_404(Folder, pk=folder_id)
    if folder.owner != request.user:
        return HttpResponseForbidden("You are not allowed to view this folder")
    
    files = File.objects.filter(folder=folder).order_by('-created_at')
    return render(request, 'folder_detail.html', {'folder': folder, 'files':files})

@login_required
def file_detail(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    if file.owner != request.user:
        return HttpResponseForbidden("You are not allowed to view this file")
    
    return render(request, 'file_detail.html', {'file': file})

@login_required
def folder_create(request, parent_folder_id=None):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.owner = request.user
            if parent_folder_id:
                folder.parent = get_object_or_404(Folder, pk=parent_folder_id)
            folder.save()
            messages.success(request, "Folder created successfully!")
            if parent_folder_id:
                return redirect('folder_list', parent_folder_id=parent_folder_id)
            else:
                 return redirect('folder_list')
    else:
        form = FolderForm()
    
    if parent_folder_id is not None:
       parent_folder = get_object_or_404(Folder, pk=parent_folder_id)
    else:
        parent_folder = None

    return render(request, 'folder_form.html', {'form': form, 'parent_folder': parent_folder})


@login_required
def file_create(request, folder_id):
    folder = get_object_or_404(Folder, pk=folder_id)
    if folder.owner != request.user:
      return HttpResponseForbidden("You are not allowed to upload to this folder")
    
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.owner = request.user
            file.folder = folder
            file.save()
            messages.success(request, "File uploaded successfully!")
            return redirect('folder_detail', folder_id=folder_id)
    else:
        form = FileForm()
    return render(request, 'file_form.html', {'form': form, 'folder': folder})

@login_required
def folder_update(request, folder_id):
    folder = get_object_or_404(Folder, pk=folder_id)
    if folder.owner != request.user:
       return HttpResponseForbidden("You are not allowed to edit this folder")
    if request.method == 'POST':
        form = FolderForm(request.POST, instance=folder)
        if form.is_valid():
            form.save()
            messages.success(request, "Folder updated successfully!")
            return redirect('folder_detail', folder_id=folder_id)
    else:
        form = FolderForm(instance=folder)
    return render(request, 'folder_form.html', {'form': form, 'folder':folder})


@login_required
def file_update(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    if file.owner != request.user:
      return HttpResponseForbidden("You are not allowed to edit this file")

    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES, instance=file)
        if form.is_valid():
            form.save()
            messages.success(request, "File updated successfully!")
            return redirect('file_detail', file_id=file_id)
    else:
        form = FileForm(instance=file)
    return render(request, 'file_form.html', {'form': form, 'file':file})


@login_required
def folder_delete(request, folder_id):
    folder = get_object_or_404(Folder, pk=folder_id)
    if folder.owner != request.user:
        return HttpResponseForbidden("You are not allowed to delete this folder")
    if request.method == 'POST':
        folder.delete()
        messages.success(request, "Folder deleted successfully!")
        if folder.parent_id:
            return redirect('folder_list', parent_folder_id=folder.parent_id) # Redirect to parent folder list
        else:
            return redirect('folder_list')  # Redirect to root list
    return render(request, 'confirm_delete.html', {'item_type': 'folder','item': folder})

@login_required
def file_delete(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    if file.owner != request.user:
        return HttpResponseForbidden("You are not allowed to delete this file")
    if request.method == 'POST':
        folder_id = file.folder_id
        file.delete()
        messages.success(request, "File deleted successfully!")
        return redirect('folder_detail', folder_id=folder_id)
    return render(request, 'confirm_delete.html', {'item_type': 'file', 'item': file})

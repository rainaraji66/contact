from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm,UserDeleteForm
from . models import *




def register(request):
    
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'bag/register.html',{'form':form})
#login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        #p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid(): #and p_form.is_valid():
            u_form.save()
            #p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('crud-home')


    else:
        u_form = UserUpdateForm( instance=request.user)
        #p_form = ProfileUpdateForm( instance=request.user.profile)

    context ={
        'u_form': u_form,
        #'p_form': p_form
    }
    return render(request,'bag/profile.html', context)



def delete(request):
    if request.method == 'POST':
        #import pdb;pdb.set_trace();
        d_form = UserDeleteForm(request.POST, instance=request.user)
        user = request.user
        user.delete()
        messages.info(request, 'Your account has been deleted.')
        # form = UserRegisterForm()
        return redirect('register')
        # return request

    else:
        d_form = UserDeleteForm(instance=request.user)



    context ={
        'd_form': d_form,
        #'p_form': p_form
    }
    return render(request,'bag/delete.html', context)

 
    

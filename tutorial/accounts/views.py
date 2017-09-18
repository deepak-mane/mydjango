from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
# Create your views here.
def home(request):
	#return HttpResponse('Home page!!!')
	#return render(request, 'accounts/login.html')
	numbers = [1, 2, 3, 4, 5]
	name = 'Max Goodridge'
	args = {'myname': name, 'numbers': numbers}
	return render(request, 'accounts/home.html', args)

def register(request):
	if request.method =='POST':
		#form = UserCreationForm(request.POST)
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/accounts')
	else:
		#form = UserCreationForm()
		form = RegistrationForm
		args = {'form': form}
		return render(request, 'accounts/reg_form.html', args)

def view_profile(request):
	args = {'user': request.user}
	return render(request, 'accounts/profile.html', args)


def edit_profile(request):
	if request.method =='POST':
		#form = UserCreationForm(request.POST)
		form = UserChangeForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('/accounts/profile')
	else:	# This will be for the GET Request
		# form = UserCreationForm()
		form = UserChangeForm(instance=request.user)
		args = {'form': form}
		return render(request, 'accounts/edit_profile.html', args)

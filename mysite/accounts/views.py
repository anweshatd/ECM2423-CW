from django.shortcuts import render
from accounts.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

'''
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
'''

#need to fix

def SignUp(request):
    if request.method == 'POST':
        signupForm = UserCreationForm(request.POST)
        if signupForm.is_valid():
            signupForm.save()
            messages.success(request, 'Account created successfully')
            return redirect("login")
    else:
        signupForm = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': signupForm})
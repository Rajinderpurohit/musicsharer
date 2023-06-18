from django.shortcuts import redirect,render
from .models import CustomUser
from .models import Audio_store as astore
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from . import forms

#this function checks registered emails.
def testing(request):
    return HttpResponse(CustomUser.objects.filter(email=request.GET['email']).exists())
   
def login_page(request):
  if request.user.is_authenticated:
     return redirect('home')
  form = forms.LoginForm()
  message = ''
  if request.method == 'POST':
    form = forms.LoginForm(request.POST)
    if form.is_valid():
      user = authenticate(
         username=form.cleaned_data['username'],
         password=form.cleaned_data['password'],
         )
      if user is not None:
        login(request, user)
        return redirect('home')
      else:
         message = 'Login failed!'
    else:
       message='Form is not valid.'
  return render(request, 'login.html', context={'form': form, 'message': message})

def logout_user(request):
    if request.user.is_authenticated==False:
       return redirect('login')
    logout(request)
    return redirect('login')

def sign_page(request):
    form = forms.SignForm()
    message = ''
    if request.method == 'POST':
        form = forms.SignForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password1']
            user = CustomUser.objects.create_user(username,email, password)
            user.save()
            message = f'{email}! You have been registered.'
    return render(request, 'sign.html', context={'form': form, 'message': message})


#@login_required
#def home(request):
#   return render(request, 'home.html')

@login_required
def Audio_up_store(request):
  form=forms.AudioForm()
  if request.method=='POST':
    request.POST._mutable=True
    form=request.POST['uploaded_by']=request.user.email
    form=forms.CheckAudioForm(request.POST,request.FILES or None,request.user.email)
    if form.is_valid():
      form.save()
      return HttpResponse('success')
    else:
      print(form.errors)
      form=forms.AudioForm()
  return render(request,'upload.html',{'form':form})

@login_required
def home(request):
  public_audios = astore.objects.filter(uploaded_for='None',privacy='1').values()
  protected_audios = astore.objects.filter(uploaded_for__contains=request.user.email,privacy='2').values()
  private_audios = astore.objects.filter(uploaded_by=request.user.email,privacy='3').values()
  template = loader.get_template('home.html')
  context = {'public_audios': public_audios,'protected_audios': protected_audios,'private_audios': private_audios,}
  return HttpResponse(template.render(context, request))











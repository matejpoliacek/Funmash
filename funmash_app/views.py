from django.shortcuts import render
from django.http import HttpResponse

from funmash_app.models import Image, UserProfile

from funmash_app.forms import UserForm, UserProfileForm 
# plus ImageForm

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# register, login and logout stuff
# different from Rango where we also put in profile_form
def register(request):

    registered = False

    if request.method == 'POST':
        
        user_form = UserForm(data=request.POST)
        
        if user_form.is_valid():
           
            user = user_form.save()
           
            user.set_password(user.password)
            user.save()

            registered = True
        else:
           
            print(user_form.errors)
    else:
        
        user_form = UserForm()

    return render(request,
                  'funmash_app/register.html',
                  {'user_form': user_form,
                   'registered': registered})
    # user_profile_form will have to be included in 
    # UserProfile view ) in a similar manner as above

def login(request):
    
    if request.method == 'POST':
       
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
          
            if user.is_active:

                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'funmash_app/accountdisabled.html', {})
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return render(request, 'funmash_app/invalidlogin.html', {})
# TODO the above should be changed to templates
   
    else:

        return render(request, 'funmash_app/login.html', {})

@login_required
def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def index(request):
    context_dict = {}
    return render(request, 'funmash_app/index.html', context=context_dict)


def about(request):
    return render(request, 'funmash_app/about.html')


def change_password(request):
    return render(request, 'funmash_app/change_password.html')


def profile(request):
    return render(request, 'funmash_app/profile.html')


def top5(request):
    return render(request, 'funmash_app/top5.html')


# def addIssue(request):
#     if request.method == 'POST':
#         issue_form = IssueForm(request.POST, request.FILES)
#         if issue_form.is_valid():
#             issue = issue_form.save(commit=False)
#             issue.save()
#         else:
#             print(issue_form.errors)
#
#     issue_form = IssueForm()
#
#     return render(request, 'fixit/addIssue.html', {'issue_form': issue_form})
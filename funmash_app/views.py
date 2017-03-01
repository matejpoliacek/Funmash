from django.shortcuts import render
from django.http import HttpResponse

from funmash_app.models import Image, UserProfile

from funmash_app.forms import UserForm, UserProfileForm, ImageForm
## TODO plus ImageForm

from random import randint

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(request):
    context_dict = {}
    images = Image.objects.all()

    numOfImages = len(images)

    ranNum1 = randint(0, numOfImages-1)
    ranNum2 = randint(0, numOfImages-1)

    while (ranNum2 == ranNum1):
        ranNum2 = randint(0, numOfImages)

    firstImage = images[ranNum1]
    secondImage = images[ranNum2]

    context_dict = {'firstImage': firstImage, 'secondImage': secondImage}

    return render(request, 'funmash_app/index.html', context=context_dict)

# experimenting with how images are passed - modified urls as well (added index2)

# TODO index 2 has to redirect to a new view that midifies the image
# image 2 will redirect and process_image_source and pass it to index



def index2(request, image_name):
    image = Image.objects.get(name=image_name)
    image.ranking = image.ranking + 1
    image.save()

    return index(request)

# INDEX BACKUP:
# def index(request):
#   context_dict = {}
# return render(request, 'funmash_app/index.html', context=context_dict)



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

def user_login(request):
    
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


def about(request):
    return render(request, 'funmash_app/about.html')


def change_password(request):
    return render(request, 'funmash_app/change_password.html')


def profile(request):
#	form = UserProfileForm()
	
	#if request.method == 'POST':
		#form = UserProfileForm(request.POST)
		
		# Has valid information been provided to the form
		#if form.is_valid():
			#Save the new user to the database.
		#	form.save(commit=True)
	    #	return index(request)
		#else:
		#	print(form.errors)
			
    return render(request, 'funmash_app/profile.html')
#, {'form': form})


def top5(request):
    return render(request, 'funmash_app/top5.html')

def upload_pic(request):
    form = ImageForm
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    return render(request, 'funmash_app/profile.html', {'form': form})



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
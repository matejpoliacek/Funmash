from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from funmash_app.models import Image, UserProfile


from funmash_app.forms import UserForm, ImageForm
## TODO plus ImageForm

from random import randint

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User




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



def about(request):
    return render(request, 'funmash_app/about.html')


def change_password(request):
    return render(request, 'funmash_app/change_password.html')


@login_required
def profile(request):

    return render(request, 'funmash_app/profile.html')


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
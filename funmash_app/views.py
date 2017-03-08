from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from funmash_app.models import Image, UserProfile


from funmash_app.forms import UserForm
## TODO plus ImageForm

from random import randint

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage



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


def about(request):
    return render(request, 'funmash_app/about.html')


# helper method to create objects in the database
def add_img(name,source,ranking, ownerName):
    img = Image.objects.get_or_create(name=name)[0]
    img.source = source
    img.ranking = ranking
    img.owner = ownerName
    img.save()
    return img


@login_required
def profile(request):
    username = request.user.username
    if request.method == 'POST':
        images = Image.objects.all()
        numOfNext = len(images) + 1
        nameOfNext = str(numOfNext) + ".jpg"
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(nameOfNext, myfile)
        img = add_img(str(numOfNext), settings.MEDIA_URL + nameOfNext, 0, username)
        print(username)
        return HttpResponse(0)

    if request.method == 'GET':
        context_dict = {}
        user_images = []
        #need to reverse this order -->
        user_images = (Image.objects.filter(owner=username))

        context_dict['user_images1'] = user_images[0:3]
        context_dict['user_images2'] = user_images[3:6]
        return render(request, 'funmash_app/profile.html', context_dict)


def uploaded(request):
    username = request.user.username
    if request.method == 'GET':
        context_dict = {}
        user_images = []
        user_images = (Image.objects.filter(owner=username))
        context_dict['user_images1'] = user_images[0:3]
        context_dict['user_images2'] = user_images[3:6]
        return render(request, 'funmash_app/uploaded.html', context_dict)

def top5(request):
    return render(request, 'funmash_app/top5.html')


def like_picture(request):
    pic_name=None
    if request.method == 'GET':
        pic_name = request.GET['picture_name']
        ranking = 0
        if pic_name:

            pic = Image.objects.get(name=pic_name)
            if pic:
                ranking = pic.ranking + 1
                pic.ranking = ranking
                pic.save()

        return HttpResponse(0)

# Render part of html template which contains the first image
def render_pic1(request):
    if request.method == 'GET':
        context_dict = {}
        images = Image.objects.all()
        numOfImages = len(images)
        ranNum1 = randint(0, numOfImages - 1)
        firstImage = images[ranNum1]

        context_dict = {'firstImage': firstImage}

        return render(request, 'funmash_app/render_pic1.html', context=context_dict)

# Render part of html template which contains the first image
# Includes check to make sure the two images are not the same
def render_pic2(request):
    if request.method == 'GET':
        pic_name = request.GET['picture_name']
        pic_name = int(pic_name) - 1

        images = Image.objects.all()
        numOfImages = len(images)
        ranNum2 = randint(0, numOfImages - 1)

        while (ranNum2 == pic_name):
            ranNum2 = randint(0, numOfImages)
        context_dict = {}
        images = Image.objects.all()

        secondImage = images[ranNum2]

        context_dict = {'secondImage': secondImage}

        return render(request, 'funmash_app/render_pic2.html', context=context_dict)


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
        images = images.extra(select={'name': 'CAST(name AS INTEGER)'}).extra(order_by = ['name'])

        numOfNext = len(images) + 1

        #check if we need to run the loop, i.e. if thre is a discrepancy between
        #the number of images in database and the last filename
        if (images[len(images) - 1]) != len(images):
            print("trigger")
            for i in range(0, len(images)):
                test_name = i+1
                print(test_name)
                print(int(images[i].name))

                if test_name != int(images[i].name):
                    numOfNext = test_name
                    print("all the way")
                    break

        print(numOfNext)
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
        user_images = list(reversed(Image.objects.filter(owner=username)))

        last_image=user_images[0:6]

        #Number of images loaded for the first time the page loads, not neccesarily 6
        last_image=len(last_image)

        #first image is always 0 as we reload the page
        first_image=0

        context_dict['user_images1'] = user_images[0:3]
        context_dict['user_images2'] = user_images[3:6]
        context_dict['numOfImages'] = last_image
        context_dict['numOfFirstImage'] = first_image
        return render(request, 'funmash_app/profile.html', context_dict)

#view to refresh the last uploaded image
def uploaded(request):
    username = request.user.username
    if request.method == 'GET':
        context_dict = {}
        user_images = []
        #this is how we reverse, who could tell, the list is needed as reversed
        #is not outputting numbers in any structure
        user_images = list(reversed(Image.objects.filter(owner=username)))
        context_dict['user_images1'] = user_images[0:3]
        context_dict['user_images2'] = user_images[3:6]
        last_image = user_images[0:6]

        # Number of images loaded for the first time the page loads
        last_image = len(last_image)
        context_dict['numOfImages'] = last_image

        #first image is always zero here as well as we show the latest uploads
        first_image = 0
        context_dict['numOfFirstImage'] = first_image
        return render(request, 'funmash_app/uploaded.html', context_dict)

#view to see next images
def next_pic(request):
    username = request.user.username
    if request.method == 'GET':
        context_dict = {}
        user_images = []
        user_images = list(reversed(Image.objects.filter(owner=username)))
        #how many pictures from start we have shown previously
        #this now becomes our index of first image in next batch
        numOfPic=int(request.GET['numOfPic'])
        context_dict['user_images1'] = user_images[numOfPic:(numOfPic+3)]
        context_dict['user_images2'] = user_images[(numOfPic+3):(numOfPic+6)]
        first_image = numOfPic
        #increase picture number for next potential batch
        numOfPic=numOfPic+6
        last_image = len(user_images)

        #numOfPic cannot overstep number of images of user
        if numOfPic>last_image:
            numOfPic=last_image

        context_dict['numOfImages'] = numOfPic
        context_dict['numOfFirstImage'] = first_image
        return render(request, 'funmash_app/uploaded.html', context_dict)

#view to see previous images
def previous_pic(request):
    username = request.user.username
    if request.method == 'GET':
        context_dict = {}
        user_images = []
        user_images = list(reversed(Image.objects.filter(owner=username)))
        first_image=int(request.GET['numOfFirst'])
        numOfPic=first_image

        #This is the case when we get to the start, beacuse we want to show as many as 6 pictures
        if numOfPic<6:
            #check if user actually even has 6 pictures
            numOfPic=len(user_images[0:6])

        #as we are going to previous batch we decrease by 6
        first_image=first_image-6
        #first image can not be less than 0
        if first_image<0:
            first_image=0

        context_dict['user_images1'] = user_images[first_image:(first_image+3)]
        context_dict['user_images2'] = user_images[(first_image+3):(first_image+6)]

        context_dict['numOfImages'] = numOfPic
        context_dict['numOfFirstImage'] = first_image
        return render(request, 'funmash_app/uploaded.html', context_dict)


def top5(request):
    image_list = Image.objects.order_by('-ranking')[:5]
    context_dict = {'topImages': image_list }
    return render(request, 'funmash_app/top5.html', context = context_dict)


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
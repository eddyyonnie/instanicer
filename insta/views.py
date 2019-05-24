import datetime as dt
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Profile,Image,Comment,instaLetterRecipients
from .forms import NewImageForm,NewCommentForm,instaLetterForm,NewProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def welcome(request):
    images=Image.objects.all()
    tot='collo'
    return render(request, 'welcome.html',{'images':images,'tot':tot})

@login_required(login_url='/accounts/login/')
def today(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            
            
            form = NewCommentForm()
            recipient = instaLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('welcome')
    else:
        form = instaLetterForm()
        comments= Comment.objects.all()
        
    return render(request,'welcome.html',{ 'profile':profile,'form':form ,'comments':comments,})
    

  


def search_results(request):

    if 'profile' in request.GET and request.GET["Profile"]:
        search_term = request.GET.get("Profile")
        searched_profile = Profile.search_by_username(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"profiles": searched_profile})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})



def profile(request):
    current_user = request.user
  

    try:
        # profile = get_object_or_404(Profile,user=current_user)
       image=Image.objects.filter(profile_id=request.user.id)
       profile=Profile.objects.filter(identity_id=request.user.id)[0:1]
    except ObjectDoesNotExist:
       raise Http404()
    return render(request,'profile.html',{  'profile':profile,'image':image})
    

def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.identity = current_user
            profile.save()
        return redirect('welcome')
    else:
        form = NewProfileForm()
    return render(request,'edit_profile.html', {'form':form})

def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profile = Profile.objects.filter(identity__username = search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"profile": searched_profile})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def search_profile(request,profile_id):
    try :
        profile = Profile.objects.get(id = profile_id)

    except ObjectDoesNotExist:
        # raise Http404()
        return render(request, 'search_profile.html')

    return render(request, 'search_profile.html', {'profile':profile})

@login_required(login_url='/accounts/login/')
def image(request):
   current_user = request.user
   if request.method == 'POST':
       form = NewImageForm(request.POST, request.FILES)
       if form.is_valid():
           image = form.save(commit = False)
           image.profile = current_user
           image.save()
       return redirect('today')
   else:
       form = NewImageForm()
   return render(request,'newImage.html', {'form':form})



# Create your views here.

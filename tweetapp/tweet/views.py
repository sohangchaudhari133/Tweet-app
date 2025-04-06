from django.shortcuts import render,redirect,get_object_or_404
from .forms import TweetForm,UserRegistrationForm
from .models import Tweet
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})

@login_required
def tweet_create(request):
    if request.method == 'POST':
        # request.FILES is used to handle file uploads
        # request.POST is used to handle form data
        form = TweetForm(request.POST,request.FILES)
        if form.is_valid():
        
          tweet = form.save(commit=False)
        # Set the user to the currently logged-in user
        tweet.user = request.user
        # Save the tweet instance to the database
        tweet.save()
        return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_create.html', {'form': form})

@login_required
def tweet_edit(request, tweet_id):
    # here tweet gets the tweet object with the given id and user
    # if the user is not the owner of the tweet, a 404 error is raised
    tweet = get_object_or_404(Tweet,pk = tweet_id,user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST,request.FILES, instance=tweet)
        if form.is_valid():
          tweet = form.save(commit=False)
          tweet.user = request.user
          tweet.save()
        return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, "tweet_create.html",{'form': form})

@login_required
def tweet_delete(request,tweet_id):
    tweet = get_object_or_404(Tweet,pk = tweet_id,user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # set the user to the currently logged-in user
            # cleaned_data is used to get the cleaned data from the form
            # set_password is used to hash the password
            user.set_password(form.cleaned_data['password1'])
            user.save()
            # login is used to log the user in after registration
            login(request,user)
        return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
        print(form.errors)

    return render(request,'registration/register.html',{'form':form})
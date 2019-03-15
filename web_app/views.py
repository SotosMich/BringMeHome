from django.shortcuts import render
from django.http import HttpResponse
from web_app.forms import UserForm, UserProfileForm, PostForm, CommentForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from web_app.models import Post, User, UserProfile
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.


def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    post_list = Post.objects.order_by('-date')[:6]
    context_dict = {'posts': post_list}

    request.session.set_test_cookie()

    # Call the helper function to handle the cookies
    visitor_cookie_handler(request)

    # Obtain our Response object early so we can add cookie information.
    response = render(request, 'web_app/index.html', context_dict)

    # Return response back to the user, updating any cookies that need changed.
    return response


def found_posts(request):
    post_list = Post.objects.order_by('-date').filter(status=1)
    context_dict = {'posts': post_list}

    response = render(request, 'web_app/found_posts.html', context_dict)
    return response


def lost_posts(request):
    post_list = Post.objects.order_by('-date').filter(status=2)
    context_dict = {'posts': post_list}

    response = render(request, 'web_app/lost_posts.html', context_dict)
    return response


def about(request):
    request.session.set_test_cookie()

    # Call the helper function to handle the cookies
    visitor_cookie_handler(request)

    # Obtain our Response object early so we can add cookie information.
    response = render(request, 'web_app/about.html')

    # Return response back to the user, updating any cookies that need changed.
    return response


def register(request):
    # A boolean value for telling the template
    # whether the registration was successful.
    # Set to False initially. Code changes value to
    # True when registration succeeds.
    registered = False
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves,
            # we set commit=False. This delays saving the model
            # until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user
            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and
            # put it in the UserProfile model.
            if 'photo' in request.FILES:
                profile.photo = request.FILES['photo']
            # Now we save the UserProfile model instance.
            profile.save()
            # Update our variable to indicate that the template
            # registration was successful.
            registered = True
        else:
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            print(user_form.errors, profile_form.errors)
    else:
        # Not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.
        user_form = UserForm()
        profile_form = UserProfileForm()
        # Render the template depending on the context
    return render(request,
                  'web_app/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed
        # to request.POST['<variable>'], because the
        # request.POST.get('<variable>') returns None if the
        # value does not exist, while request.POST['<variable>']
        # will raise a KeyError exception.
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.

    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'web_app/login.html', {})


@login_required
def user_delete(request):
    user = request.user
    user.delete()
    deleted = True

    return render(request,
                  'web_app/accounts/profile.html',
                  {'deleted': deleted})


# @login_required
# def edit_profile(request):
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=request.user)

#         if form.is_valid():
#             form.save()
#             return redirect(reverse('accounts:view_profile'))
#     else:
#         form = EditProfileForm(instance=request.user)
#         args = {'form': form}
#         return render(request, 'accounts/edit_profile.html', args)

# def edit_profile(request, pk=None):
#     updated = False

#     if request.method == 'POST':
#         profile_form = EditProfileForm(data=request.POST)
#         if profile_form.is_valid():
#             change = UserProfile.objects.get(id=request.user.userprofile.id)
#             change.endtime=datetime.now()
#             change.save()
#             profile = profile_form.save(commit=False)
#             profile.save()
#             updated = True
#             args = {'updated': updated}
#             # return render(request, 'web_app/accounts/profile.html', args)
#             return HttpResponseRedirect(reverse('edit_profile'))
#         else:
#              updated = False
#              args = {'updated': updated}
#             #  return render(request, 'web_app/accounts/profile.html', args)
#              return HttpResponseRedirect(reverse('edit_profile'))
#     else:
#         if pk:
#             user = User.objects.get(pk=pk)
#         else:
#             user = request.user
#         args = {'user': user}
#         return render(request, 'web_app/accounts/profile.html', args)


@login_required
def edit_profile(request):

    if request.method == 'POST':
        profile_form = UserProfileForm(data=request.POST)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.save()
        else:
            print(profile_form.errors)
    else:
        profile_form = UserProfileForm()

        return HttpResponseRedirect('web_app/accounts/profile.html')



@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('index'))


def view_user(request, userID):
    if userID:
        profile = User.objects.get(pk=userID)
    args = {'profile': profile}
    return render(request, 'web_app/accounts/user.html', args)


@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'web_app/accounts/profile.html', args)


# A helper method
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


# Updated the function definition
def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,
                                               'last_visit',
                                               str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')

    # If it's been more than a day since the last visit...
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        # update the last visit cookie now that we have updated the count
        request.session['last_visit'] = str(datetime.now())
    else:
        # set the last visit cookie
        request.session['last_visit'] = last_visit_cookie

    # Update/set the visits cookie
    request.session['visits'] = visits


@login_required
def add_post(request):
    post_added = False
    form = PostForm(request.POST or None, request.FILES or None)
    # if request.method == 'POST':
    if request.method == 'POST':
        if form.is_valid():

            if request.user:
                post = form.save(commit=False)
                post.userId = request.user
                post.save()
                post_added = True
            form = PostForm()
            return render(request,
                          'web_app/add_post.html',
                          {'post_form': form,
                           'post_added': post_added})
        else:
            print(form.errors)
    else:
        form = PostForm()

    return render(request,
                  'web_app/add_post.html',
                  {'post_form': form})


@login_required
def show_post(request, postId):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    form = CommentForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():

            if request.user:
                comment = form.save(commit=False)
                comment.userId = request.user
                post = Post.objects.get(postId=postId)
                comment.postId = post
                comment.save()

                return HttpResponseRedirect('/web_app/post/' + postId)
        else:
            print(form.errors)
    else:
        form = CommentForm()

    try:
        post = Post.objects.get(postId=postId)
        comments = post.comments.all().order_by('-date')
    except Post.DoesNotExist:
        post = None

        # context_dict['comments'] = None
    return render(request, 'web_app/post.html', {'post': post,
                                                 'comment_form': form,
                                                 'comments': comments})


def map(request):
    response = render(request, 'web_app/map.html')
    return response

from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from.models import Complaint,feedback,Profile,News,plogin
from .forms import UserRegisterForm, UserLoginForm,UserComplaintForm,UserFeedbackForm,UserUpdateForm,ProfileUpdateForm,policeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from Police.models import wanted,Missing
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    return render(request,'Usersapp/layout.html')

def phome(request):
    return render(request,'Usersapp/phome.html')

@login_required
def ViewComplaint(request):
    username = request.session['username']
    data = Complaint.objects.all().filter( username=username)
    return render(request,'Usersapp/viewComplaint.html',{'datas': data})


def home(request):

    paginate_by = 2
    context = {
        'news': News.objects.all()
    }
    return render(request,'Usersapp/home.html',context)

class PostListView(ListView):
    model = News
    template_name = 'Usersapp/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'news'
    ordering = ['-date_posted']
    paginate_by = 2

@login_required
def usershome(request):
    return render(request,'Usersapp/usershome.html')




@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'Usersapp/profile.html', context)
    

    


@login_required
def complaint(request):
    if request.method == 'POST':
        form = UserComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Complaint has been created for {username}!')
            return redirect('home')
    else:
        form = UserComplaintForm()

        
    return render(request,'Usersapp/Complaint.html', {'form': form})



@login_required
def feedback(request):
    if request.method == 'POST':
        form = UserFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Complaint has been created for {username}!')
            return redirect('home')
    else:
        form = UserFeedbackForm()

        
    return render(request,'Usersapp/feedback.html', {'form': form})
    

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'Usersapp/register.html', {'form': form})


def login_request(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                
                request.session['username']=username
                messages.info(request, f"You are now logged in as {username}")
                return redirect('usershome')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = UserLoginForm()
    return render(request, 'Usersapp/login.html', {'form': form})


def logout_request(request):
    logout(request)
    
    return render(request,'Usersapp/home.html')

@login_required
def Mwanted(request):
    data_list = wanted.objects.all()

    paginator = Paginator(data_list, 2)
    page = request.GET.get('page')
    datas = paginator.get_page(page)
    return render(request,'Usersapp/wanted.html',{'datas': datas})

@login_required
def pmissing(request):

    missing_list = Missing.objects.all()
    paginator = Paginator(missing_list, 2)
    page = request.GET.get('page')
    datas = paginator.get_page(page)
    return render(request,'Usersapp/missingpeople.html',{'datas': datas})


def plogin_request(request):
    try:
        if request.method == 'POST':
            form = policeForm(request.POST)
            if form.is_valid():
                username= form.cleaned_data.get('username')
                password= form.cleaned_data.get('password')
                m = plogin.objects.all().get( username=username,password=password)
                if m.password == form.cleaned_data.get('password'):
                    request.session['username']=username
                    request.session['password']=password
                return redirect('phome')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            form = policeForm()
        return render(request, 'Usersapp/Policelogin.html', {'form': form})
    except plogin.DoesNotExist:
        messages.error(request, "Invalid username or password.")
        form = policeForm()
        return render(request, 'Usersapp/Policelogin.html', {'form': form})

                
            


        
        



               
    
    


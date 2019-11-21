from django.urls import path
from. import views
from.views import PostListView

urlpatterns = [
    
    path('', PostListView.as_view(), name='home'),
    path('complaint/',views.complaint, name='complaint'),
    path('viewcomplaint/',views.ViewComplaint, name='ViewComplaint'),
    path('plogin/',views.plogin_request, name='plogin'),
    path('login/',views.login_request, name='login'),
    path('profile/',views.profile, name='profile'),
    path('logout/',views.logout_request, name='logout'),
    path('usershome/',views.usershome, name='usershome'),
    path('feedback/',views.feedback, name='feedback'),
    path('register/',views.register, name='register'),
    path('Mwanted/',views.Mwanted, name='Mwanted'),
    path('pmissing/',views.pmissing, name='pmissing'),
    path('phome/',views.phome, name='phome')
]
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',home,name='home'),
    path('login/',Login.as_view(),name='login'),
    path('signup/',Signup.as_view(),name='signup'),
    path('logout/',logout_view,name='logout'),
    path('showquestions/',ShowQuestion.as_view(),name='showquestions'),
    path('add-questions/',AddQuestion.as_view(),name='add-questions'),
    path('showall-admin-question/',showadmin_question,name='showall-admin-question'),
    path('delete/<int:queno>',delete,name='delete'),
    path('edit/<int:queno>',Edit.as_view(),name='edit'),
    path('myprofile/',profile,name='myprofile'),
    path('edit-profile/',EditProfile.as_view(),name='edit-profile'),
    path('check-name/',check_name),
    path('guid/',guid,name='guid'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

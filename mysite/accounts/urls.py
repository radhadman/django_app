from django.urls import path

#from . import views


#urlpatterns = [
#    path('signup/', views.SignUp.as_view(), name='signup'),
#]


from django.conf.urls import url
from . import views as accounts_views

urlpatterns = [
   
    url(r'^signup/$', accounts_views.signup, name='signup'),
]

from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views
from two_factor.urls import urlpatterns as tf_urls
from django.conf.urls import url
from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls


urlpatterns = [
	url(r'', include(tf_twilio_urls)),
	url(r'', include(tf_urls)),
	path('', PostListView.as_view(), name='blog_home'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
	path('about/', views.about, name='blog_about'),
]



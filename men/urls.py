from django.urls import path
from .import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('feedback/', views.feedback, name='feedback'),
    path('login/', views.MyprojectLoginView.as_view(), name='login'),
    path('registration/', views.RegisterUserView.as_view(), name='registration'),
    path('logout/', views.MyProjectLogout.as_view(), name='logout'),
    path('post/<slug:post_slug>/', views.MenPost.as_view(), name='post'),
    path('category/<int:cat_id>/', views.MenCategory.as_view(), name='category'),
]

"""
URL configuration for blogsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import mainPage, AddReview, profilePage, detailPage, EditReview, DeleteReview, AddRecommendation, ViewRecommendations
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainPage,name='main'),
    path('profile/',profilePage,name='profile'),
    path('profile/addreview',login_required(AddReview.as_view()),name='add'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),

    path('details/<id>/',detailPage,name='details'),
    path('profile/edit/<id>',login_required(EditReview.as_view()),name='edit'),
    path('profile/delete/<id>',login_required(DeleteReview.as_view()),name='delete'),

    path('recommend/',AddRecommendation.as_view(),name='rec'),
    path('profile/recommendations/',ViewRecommendations.as_view(),name='recs'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

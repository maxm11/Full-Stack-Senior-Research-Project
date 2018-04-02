"""djangoSRP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, reverse
from django.contrib.auth import views as auth_views

from SRP import views, tasks

app_name = 'srp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='SRP/login.html'), name="login"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='SRP/login.html'), name="login"),
    path('login/', auth_views.LoginView.as_view(template_name='SRP/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse('login'))),
    path('entity/new/create/', views.createEntity, name='createEntity'),
    path('entity/new/create/create/', views.create, name='create'),
    path('entity/<int:entity_id>/', views.dashEntity, name='dashEntity'),
    path('entity/<int:entity_id>/list/', views.experienceList, name='experienceList'),
    path('entity/<int:entity_id>/search/noun/', views.noun_search, name='noun_search'),
    path('entity/<int:entity_id>/edit/', views.editEntity, name='editEntity'),
    path('entity/<int:entity_id>/experience/add/', views.addExperience, name='addExperience'),
    path('entity/<int:entity_id>/add/', views.add, name='eadd'),
    path('entity/<int:entity_id>/experience/<int:experience_id>/', views.dashExperience, name='dashExperience'),
    path('entity/<int:entity_id>/experience/<int:experience_id>/list/', views.sentenceList, name='sentenceList'),
    path('task/expintake', tasks.experience_intake, name="experienceIntake")
]

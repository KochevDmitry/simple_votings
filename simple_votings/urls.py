"""simple_votings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from main import views
from django.contrib.auth import views as auth_views

from main.views import get_menu_context

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='index'),
    path('time/', views.time_page, name='time'),
    path('votings/', views.votings_page, name='votings'),
    path('voting_info/', views.voting_info_page, name='voting_info'),
    path('add_voting/', views.add_voting, name='add_voting'),
    path('result_voting/', views.result_voting, name='result_voting'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            extra_context={
                'menu': get_menu_context(),
                'pagename': 'Авторизация'
            }
        )
    ),
    path('logout/', auth_views.LogoutView.as_view())
]

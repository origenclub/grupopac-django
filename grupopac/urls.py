"""grupopac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth.views import LoginView, logout_then_login
from django.urls import path, include
from django.conf.urls import handler404

from app.views import welcome, about, contact, page_404, portfolio

# from django.contrib.auth import login

from django.conf import settings
from django.conf.urls.static import static

handler404 = page_404

urlpatterns = [
    # path('admin/', admin.site.urls),

    path('', welcome, name="welcome"),
    path('nosotros/', about, name="about"),
    path('contactanos/', contact, name="contact"),
    path('portafolio/', portfolio, name="portfolio"),

    path('panel/', include(('app.urls', 'app'))),

    path('panel/login/', LoginView.as_view(template_name='auth/login.html'), name="login"),
    path('panel/logout/', logout_then_login, name="logout")

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

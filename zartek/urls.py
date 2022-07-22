"""zartek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path,include
from rest_framework import routers

from zartekapp import views
from zartekapp.views import itemlist,createuserview

router=routers.SimpleRouter()
router.register('task',itemlist)
router.register('completed_itemlist',views.completed_itemlist)
router.register('due_itemlist',views.due_itemlist)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.createuserview.as_view(),name='user'),
    path('api_auth/',include('rest_framework.urls')),
    path('',include(router.urls))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Taskserializers,userserializers
from .models import Task
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
# Create your views here.

class itemlist(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset=Task.objects.all().order_by('post_name')
    serializer_class = Taskserializers
class due_itemlist(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id').filter(completed=False)
    serializer_class = Taskserializers
class completed_itemlist(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id').filter(completed=True)
    serializer_class = Taskserializers
class createuserview(CreateAPIView):
    model=get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = userserializers


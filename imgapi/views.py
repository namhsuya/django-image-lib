from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from .models import Image
from rest_framework import viewsets
from .serializers import ImageSerializer
# from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.decorators import action
          
class GetImageViewSet(viewsets.ModelViewSet):
    
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['uploaded_by']
    # filter_fields = ('show__uploaded_by')
    # filter_backends = (filters.DjangoFilterBackend,)
    
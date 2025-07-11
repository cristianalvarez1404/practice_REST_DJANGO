from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .models import Blog,Comment
from .serializers import BlogSerializer,CommentSerializer

# Create your views here.
class BlogsView(generics.ListCreateAPIView):
  queryset = Blog.objects.all()
  serializer_class = BlogSerializer

class BlogsView(generics.RetrieveUpdateDestroyAPIView):
  pass

class CommentsView(generics.ListCreateAPIView):
  pass
class CommentsView(generics.RetrieveUpdateDestroyAPIView):
  pass
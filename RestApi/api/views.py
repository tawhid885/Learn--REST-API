from django.shortcuts import render
from rest_framework import generics

from myapp.models import Quote,QuoteCategory
from .serialaizers import QuoteSerializers,QuoteCategorySerializers 


class QuoteApiView(generics.ListAPIView):
    queryset=Quote.objects.all()
    serializer_class= QuoteSerializers


class QuoteCategoryApiView(generics.ListAPIView):
    queryset=QuoteCategory.objects.all()
    serializer_class=QuoteCategorySerializers

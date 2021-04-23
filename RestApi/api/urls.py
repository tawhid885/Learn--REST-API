from django.urls import path
from .views import QuoteApiView,QuoteCategoryApiView

urlpatterns = [
    path('', QuoteCategoryApiView.as_view()),
    path('quotes/', QuoteApiView.as_view()),
]

from django.urls import path,include

# from .views import ArticleList,ArticleDetail,ArticleListGenerics
from .views import ArticleViewSet,GenericViewSet,ModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('article',ArticleViewSet,basename='article')
# router.register('article',GenericViewSet,basename='article')
router.register('article',ModelViewSet,basename='article')

urlpatterns=[
    path('viewset/',include(router.urls)),
    # path('viewset/<int:pk>/',include(router.urls)),
    # path('articles/',ArticleList.as_view(),name='article-list'),  
    # path('detail/<str:id>/',ArticleDetail.as_view(),name='article-detail'),  

    # path('article/<int:id>/',ArticleListGenerics.as_view(),name='article'),  
]
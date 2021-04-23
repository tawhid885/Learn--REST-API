from django.shortcuts import render,get_object_or_404
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

from rest_framework import generics
from rest_framework import mixins

from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from rest_framework import viewsets



#------------------------------viewsets----------------------------------
class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        article = Article .objects.all()
        serializer=ArticleSerializer(article, many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer =Article.objects.create(data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk =None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset,pk = pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def update(self,request,pk=None):
        article = Article.objects.get(pk = pk)
        serializer = ArticleSerializer(article , data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error , status = status.HTTP_400_BAD_REQUEST)



#------------------------------genericveiwsetes--------------------------

class GenericViewSet(viewsets.GenericViewSet,mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

#---------------------------Model viewsets---------------------------------
class ModelViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

#------------------------learning generics and mixins-------------------------------

# class ArticleListGenerics(generics.GenericAPIView, mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
#     serializer_class=ArticleSerializer
#     queryset=Article.objects.all()

#     lookup_field='id'

#     # authentication_classes =[SessionAuthentication,BasicAuthentication]
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     token =Token.objects.create(user=user.instance)
#     print(token.key)


#     def get(self,request,id=None):

#         if id:
#             return self.retrieve(request)
#         else:
#             return self.list(request)

#     def post(self,request):
#         return self.create(request)

#     def put(self,request,id=None):
#         return self.update(request,id)

#     def delete(self,request,id):
#         return self.destroy(request,id)





# # ----------------------Function based APIView------------------------- 

# # @api_view(['GET','POST'])
# # def ArticleList(request):
# #     if request.method=='GET':
# #         articles=Article.objects.all()
# #         serializer=ArticleSerializer(articles,many=True)
# #         return Response(serializer.data)

# #     elif request.method=='POST':
# #         serializer=ArticleSerializer(data=request.data)
        
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data,status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# # @api_view(['GET','POST','PUT','DELETE'])
# # def ArticleDetail(request,id):
# #     try:
# #         article=Article.objects.get(pk=id)
# #     except Article.DoesNotExist:
# #         return Response(status=status.HTTP_404_NOT_FOUND)
    
# #     if request.method == 'GET':
# #         serializer=ArticleSerializer(article)
# #         return Response(serializer.data)
     
# #     elif request.method=='PUT':
# #         serializer=ArticleSerializer(article,data=request.data)

# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# #     elif request.method=='POST':
# #         # data=JSONParser().parse(request)
# #         serializer=ArticleSerializer(data=request.data)

# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data,status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# #     elif request.method=='DELETE':
# #         article.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)



# # ---------------------class based APIView-----------------------


# class ArticleList(APIView):
#     def get(self,request):
#         article=Article.objects.all()
#         serializer=ArticleSerializer(article,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer=ArticleSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# class ArticleDetail(APIView):
#     def get_object(self,id):
#         try:
#             return Article.objects.get(id=id)
#         except Article.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
    
#     def get(self,request,id):
#         article=self.get_object(id)
#         serializer=ArticleSerializer(article)
#         return Response(serializer.data)

#     def put(self,request,id):
#         article=self.get_object(id)
#         serializer=ArticleSerializer(article,data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    
#     def delete(self,request,id):
#         article= self.get_object(id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


    



    

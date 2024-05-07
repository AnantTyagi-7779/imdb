from django.http import HttpResponse, JsonResponse
from django.http import Http404
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.


# def movie_list(request):
#     movie_list=WatchList.objects.all()
#     serialized=WatchListSerializer(movie_list, many=True)
#     return JsonResponse(serialized.data, safe=False)

# def movie_detail(request,pk):
#     movie=WatchList.objects.get(pk=pk)
#     serialized=WatchListSerializer(movie)
#     return JsonResponse(serialized.data)

# @api_view(['GET','POST'])
# def stream_list(request, format=None):

#     if request.method == 'GET':
#         stream_list=StreamPlatform.objects.all()
#         serialized=StreamPlatformSerializer(stream_list, many=True)
#         return Response(serialized.data)
    
#     elif request.method=='POST':
#         _data = request.data
#         serializer = StreamPlatformSerializer(data=_data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serialized.data, 
#             status=status.HTTP_201_CREATED)
#         return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)




# @api_view(['GET','PUT','DELETE '])
# def stream_detail(request,pk,format=None):
#     try:
#         stream_platform=StreamPlatform.objects.get(pk=pk)
#     except StreamPlatform.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = StreamPlatformSerializer(stream_platform)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         _data=request.data
#         serializer = StreamPlatformSerializer(stream_platform, data=_data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

#     elif request.method == 'DELETE':
#         stream_platform.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)

class StreamPlatformList(APIView):
    """
    List all StreamPlatforms, or create a new StreamPlatform.
    """
    def get(self,request,format=None):
        stream_list=StreamPlatform.objects.all()
        serialized=StreamPlatformSerializer(stream_list, many=True)
        return Response(serialized.data)

    def post(self,request,format=None):
        _data = request.data
        serializer = StreamPlatformSerializer(data=_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serialized.data, 
            status=status.HTTP_201_CREATED)
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)

class StreamPlatformDetail(APIView):

    """
    Retrieve, update or delete a StreamPlatform instance.
    """
    def get_object(self, pk):
        try:
            return StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        stream_platform = self.get_object(pk)
        serializer = StreamPlatformSerializer(stream_platform)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        stream_platform = self.get_object(pk)
        _data=request.data
        serializer = StreamPlatformSerializer(stream_platform, data=_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,pk,format=None):
        stream_platform = self.get_object(pk)
        stream_platform.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

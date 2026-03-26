from .models import Student
from .serializers import StuSerializer
from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class StudentViewSet(viewsets.ViewSet):

    def list(self, request):
        snippets = Student.objects.all()
        serializer = StuSerializer(snippets, many=True)
        return Response(serializer.data)


    def create(self, request):
        serializer = StuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        snippet = Student.objects.get(pk=pk)
        serializer = StuSerializer(snippet)
        return Response(serializer.data)

    def update(self, request, pk=None):
        snippet = Student.objects.get(pk=pk)
        serializer = StuSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        snippet = Student.objects.get(pk=pk)
        serializer = StuSerializer(snippet, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Short code

# class StudentViewSet(viewsets.ModelViewSet):
#     """
#     A simple ViewSet for viewing and editing accounts.
#     """
#     queryset = Student.objects.all()
#     serializer_class = StuSerializer
    
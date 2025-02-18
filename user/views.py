from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationUserSerialiazer


class RegistrationUserView(generics.CreateAPIView):
    serializer_class = RegistrationUserSerialiazer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

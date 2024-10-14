from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from django.contrib.auth import authenticate, login

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import StudentAccountCreation
from .serializers import StudentAccountSerializer, LoginSerializer

from rest_framework import status

# your_app/views.py
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer




class StudentAccountCreateView(generics.CreateAPIView):
    queryset = StudentAccountCreation.objects.all()
    serializer_class = StudentAccountSerializer
    permission_classes = [AllowAny]

class StudentAccountListView(generics.ListAPIView):
    queryset = StudentAccountCreation.objects.all()
    serializer_class = StudentAccountSerializer
    permission_classes = [IsAuthenticated]

class StudentAccountDetailView(generics.RetrieveAPIView):
    queryset = StudentAccountCreation.objects.all()
    serializer_class = StudentAccountSerializer
    permission_classes = [IsAuthenticated]

class StudentAccountUpdateView(generics.UpdateAPIView):
    queryset = StudentAccountCreation.objects.all()
    serializer_class = StudentAccountSerializer
    permission_classes = [IsAuthenticated]

# delete from administration
class StudentAccountDeleteView(generics.DestroyAPIView):
    queryset = StudentAccountCreation.objects.all()
    serializer_class = StudentAccountSerializer
    permission_classes = [IsAdminUser]

# soft delete at user side
class DeleteStudentAccount(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user=self.request.user
        user.is_deleted = True
        user.save()
        return Response({"result":"user deleted."})


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            student_id = serializer.validated_data.get('student_id')
            password = serializer.validated_data['password']

            if username:
                user = authenticate(username=username, password=password)
            elif student_id:
                user = authenticate(student_id=student_id, password=password)
            else:
                return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

            if user is not None:
                login(request, user)
                return Response({'detail': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.

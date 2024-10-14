
from rest_framework import viewsets, status
from .serializers import StudentProfileSetUpSerializer
from .models import StudentProfileSetUp
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class StudentProfileSetUpViewSet(viewsets.ModelViewSet):
    queryset = StudentProfileSetUp.objects.all()
    serializer_class = StudentProfileSetUpSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Using the serializer with the context of the authenticated user
        serializer = StudentProfileSetUpSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()  # This will automatically assign the student
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

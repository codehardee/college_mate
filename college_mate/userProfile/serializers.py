from rest_framework import serializers
from .models import StudentProfileSetUp
from authentication.models import StudentAccountCreation

class StudentProfileSetUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfileSetUp
        fields = ['unique_student_id','about', 'interests', 'profile_picture', 'portfolio', 'social_media', 'skills',
                  'certificate', 'education']
        print("student profile details......................")

        def create(self, validated_data):
            request = self.context['request']
            student = request.user  # Get the authenticated user
            validated_data['student'] = student  # Assign the student automatically
            return super().create(validated_data)

        # def create(self, validated_data):
        #     request = self.context['request']
        #     student_id = request.user.student_id  # Get the student_id from the authenticated user
        #     print("Student id.............", student_id)
        #     student = StudentAccountCreation.objects.get(student_id=student_id)  # Fetch the student instance
        #     validated_data['student'] = student  # Assign the student to the profile setup
        #     return super().create(validated_data)

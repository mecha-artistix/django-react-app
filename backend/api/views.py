from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer, NoteSerializer
from .models import Note


# Create your views here.
# create view for creating a note
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)



# create view for destroy/delete a note
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
        



# create view to register user
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() # to look in to all of the obj while creating a new user to make sure we dont create a user thats already there
    serializer_class = UserSerializer # to tell the view what kind of data we need to accept to make a new user which in this case is username and password
    permission_classes = [AllowAny] # to allow anyone even non auth users to use and create a user

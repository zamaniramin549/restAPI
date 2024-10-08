from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import HelloSerializer, ProfileSerializer, ProfileFeedItemSerializer
from .models import User, ProfileFeedItem
from .permissions import UpdateOwnProfile, UpdateOwnStatus

class HelloAPIView(APIView):
    
    serializer_class = HelloSerializer
    
    def get(self, request, format= None):
        
        an_apiview = [
            'some test going on here.',
            'what is going one?'
        ]
        
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    def post(self, request):
        
        serializer= self.serializer_class(data= request.data)
        
        if serializer.is_valid():
            first_name= serializer.validated_data.get('first_name')
            email= serializer.validated_data.get('email')
            message= f'Hello {first_name} with {email} email address.'
            return Response({'message': message})
        return Response(
            serializer.errors,
            status= status.HTTP_400_BAD_REQUEST
        )
        
    def put(self, request, pk= None):
        return Response({'Message': 'PUT'})
    
    def delete(self, request, pk= None):
        return Response({'Message': 'DELETe'})
    
    def patch(self, request, pk= None):
        return Response({'Message': 'PATCH'})
    
    
class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('first_name', 'email')
    
class UserLoginAPIView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES    
    
    
class ProfileFeedItemApiView(viewsets.ModelViewSet):
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        UpdateOwnStatus,
        IsAuthenticatedOrReadOnly,
        # IsAuthenticated
        )
    
    def perform_create(self, serializer):
        serializer.save(user_profile = self.request.user)
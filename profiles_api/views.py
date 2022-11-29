from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """ Test API View """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Return a list of APIViews features """
        an_apiviews = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similer to a traditional Django View',
        'Gives you most control over you application logic',
        'is mapped manully to urls',
        ]
        return Response({'message':'Hello!', 'an_apiviews':an_apiviews})
        # return Response(an_apiviews)


    def post(self, request, format=None):
        """ create a hello message with our Name """
        #json_data = json.loads(request.body) # if request coming from another application
        #serializer = self.serializer_class(data=json_data)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            # name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Handling Update Object """
        return Response({"method":"PUT"})

    def patch(self, request, pk=None):
        """ Handle a partial update of an object """
        return Response({"method":"PATCH"})

    def delete(self, request, pk=None):
        """ Delete an Object """
        return Response({"method":"Delete"})

class HelloViewSet(viewsets.ViewSet):
    """ Test API viewsSets """
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """ Return a Hello message """
        a_viewset = [
            'user action (list, create, retrive, update, partial_update, )',
            'Automatically maps to URL using Routers',
            'Provide more funcality with less code',
        ]
        return Response({'message':'Hello', 'a_viewset':a_viewset})

    def create(self,request):
        """ create a new hello message """
        serializer= self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its id """
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing object an object"""
        return Response({'http_method':'Delete'})


class UserProfileViewset(viewsets.ModelViewSet):
    """Handle crateing and updating profile"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """ Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

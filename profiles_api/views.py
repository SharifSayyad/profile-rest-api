from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


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


    def post(self, request, format=None):
        """ create a hello message with our Name """
        # import json
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

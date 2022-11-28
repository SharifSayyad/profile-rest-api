from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Test API View """

    def get(self, request, format=None):
        """ Return a list of APIViews features """
        an_apiviews = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similer to a traditional Django View',
        'Gives you most control over you application logic',
        'is mapped manully to urls',
        ]
        return Response({'message':'Hello!', 'an_apiviews':an_apiviews})

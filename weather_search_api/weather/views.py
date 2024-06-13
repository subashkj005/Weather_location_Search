from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Locations
from .serializers import LocationSerializer


class SearchLocationAPIView(APIView):
    
    def post(self, request):
        keyword = request.data.get('keyword', None)
        if keyword is None:
            return Response(content={'error':"Keyword should be provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            locations = Locations.objects.get(location__icontains=keyword)
            
            serializer = LocationSerializer(locations)
            
            return Response(content={'data':serializer.data}, status=status.HTTP_200_OK)
            
            
        except Locations.DoesNotExist:
            return Response(content={'error':"Location doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response(content={'error':"Location doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .diagraai import get_diagram

class DiagramView(APIView):
    def get(self, request):
        if "topic" not in self.request.GET:
            return Response({
                "error": "You must provide a topic as URL query"
            })
        else:
            output = get_diagram(self.request.GET["topic"])
            return Response({
                "output": output,
            })
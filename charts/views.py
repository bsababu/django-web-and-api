from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

@login_required
def dashboard(request):
    return render(request, 'charts/dashboard.html')

class ChartData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = [
            { "key": "Category A", "y": 40 },
            { "key": "Category B", "y": 30 },
            { "key": "Category C", "y": 20 },
            { "key": "Category D", "y": 10 }
        ]
        return Response(data)
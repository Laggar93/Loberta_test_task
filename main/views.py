import rest_framework.status
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Links
from .serializers import CheckStatusSerializer
from .services import StatusCheckService


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    queryset = Links.objects.all()
    context_object_name = 'links'


class CheckStatusView(APIView):
    service = StatusCheckService()
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = CheckStatusSerializer(data=request.data)

        if serializer.is_valid():
            data = self.service.call(data=serializer.data)
            return Response(data)

        return Response(serializer.errors, status=rest_framework.status.HTTP_400_BAD_REQUEST)


from django.shortcuts import render

# Create your views here.


from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')

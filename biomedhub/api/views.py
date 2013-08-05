# -*- coding: utf-8 -*-
# Copyright (C) 2013 Luís A. Bastião Silva and Universidade de Aveiro
#
# Authors: Luís A. Bastião Silva <bastiao@ua.pt>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


from django.http import HttpResponse

from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework import renderers
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils import simplejson
# import json
import md5
from django.views.decorators.csrf import csrf_exempt

from rest_framework.permissions import AllowAny, IsAuthenticated

# Import Search Engine 

from searchengine.search_indexes import CoreEngine
from api.models import *


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders it's content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(('GET', 'POST', 'PUT', 'OPTIONS', 'HEAD'))
def api_root(request, format=None):
    return Response({
        'search': reverse('search', request=request),
        'metadata': reverse('metadata', request=request),
        'stats': reverse('stats', request=request),
        'validate': reverse('validate', request=request),

    })

class MetaDataView(APIView):
    """
    Class to insert or update data values of one fingerprint
    Method POST: to insert a new field and value
    Method PUT: to update a value that already exists
    Note: both methods check if field value already exists and, if exists, it is updated,
    otherwise the field is created and the value added
    """

    # Example request
    # curl -H "Content-Type: application/json" -X POST -d "{\"uid\":12,\"token\":\"asdert\"}" http://192.168.1.3:8000/api/metadata -H "Authorization: Token c6e25981c67ae45f98bdb380b0a9d8164e7ec4d1" -v

    authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.AllowAny,)
    # permission_classes = (permissions.IsAuthenticated,)
    parser_classes((JSONParser,))

	  def get(self, request, *args, **kw):
        # Process any get params that you may need
        # If you don't need to process get params,
        # you can skip this part
        get_arg1 = request.GET.get('arg1', None)
        get_arg2 = request.GET.get('arg2', None)

        result = {'myValue': 'lol', 'myValue2': 'lol', }
        response = Response(result, status=status.HTTP_200_OK)
        return response


    def post(self, request, *args, **kw):

        # If authenticated
        if request.auth:
            user = request.user
            data = request.DATA
            result = validate_and_save(user, data)
            result['status'] = 'authenticated'
            result['method'] = 'POST'
            result['user'] = str(user)

        # NOT authenticated
        else:
            result = {'status': 'NOT authenticated', 'method': 'POST'}

        response = Response(result, status=status.HTTP_200_OK)
        return response

    def put(self, request, *args, **kw):

        # If authenticated
        if request.auth:
            user = request.user
            data = request.DATA
            result = validate_and_save(user, data)
            result['status'] = 'authenticated'
            result['method'] = 'PUT'
            result['user'] = str(user)

        # NOT authenticated
        else:
            result = {'status': 'NOT authenticated', 'method': 'PUT'}
        response = Response(result, status=status.HTTP_200_OK)

        return response


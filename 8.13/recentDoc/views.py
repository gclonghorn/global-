from rest_framework import status, mixins, viewsets, authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import Document
from team.models import Team
from rest_framework.response import Response
from django.db.models import Q



class RecentDocViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Recent.objects.all()
    serializer_class = RecentDocSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def list(self, request, *args, **kwargs):
        deldocuments = Document.objects.filter(status=2)
        self.queryset = Recent.objects.filter(~Q(document__in=deldocuments), user=request.user).order_by('-read_time')[
                        :10]
        queryset = self.filter_queryset(self.queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

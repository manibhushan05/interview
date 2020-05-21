from datetime import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, generics, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from users.filters import CustomUserFilter
from users.models import CustomUser
from users.serializers import CustomUserSerializer
from utils.helpers import get_or_none
from utils.responses import success_response, error_response
from utils.search import CustomSearch


class CustomUserListView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    filter_backends = (CustomSearch, filters.OrderingFilter, DjangoFilterBackend)
    filter_class = CustomUserFilter
    ordering_fields = ('-id',)
    search_fields = ('id', 'name')
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        queryset = self.filter_queryset(self.get_queryset())

        data = {"status": "Success", "msg": "User List"}
        print(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data["data"] = serializer.data
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        data["data"] = serializer.data
        return Response(data)

    def get_queryset(self):
        return CustomUser.objects.order_by('-id')


class UserViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        request.data["created_by"] = self.request.user.username
        request.data["last_modified_by"] = self.request.user.username
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(
                status=status.HTTP_201_CREATED,
                msg='User is created',
                data=serializer.data
            )
        return error_response(status=status.HTTP_400_BAD_REQUEST, msg='Invalid data', data=serializer.errors)

    def retrieve(self, request, pk=None):
        """
            :param request:
            :param pk:
            :return:
        """
        instance = get_or_none(model=CustomUser, id=pk)
        if isinstance(instance, CustomUser):
            serializer = CustomUserSerializer(instance=instance)
            return success_response(data=serializer.data, status=status.HTTP_200_OK, msg='success')
        return error_response(
            data={},
            msg='User does not exists with id = {}'.format(pk),
            status=status.HTTP_404_NOT_FOUND
        )

    def update(self, request, pk=None):
        """
            :param request:
            :param pk:
            :return:
        """
        request.data["last_modified_by"] = self.request.user.username
        instance = get_or_none(CustomUser, id=pk)
        if not isinstance(instance, CustomUser):
            return error_response(data={}, msg='User does not exists with id = {}'.format(pk),
                                  status=status.HTTP_404_NOT_FOUND)
        serializer = CustomUserSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(status=status.HTTP_202_ACCEPTED, msg='User is updated',
                                    data=serializer.data)
        return error_response(status=status.HTTP_400_BAD_REQUEST, msg='Invalid data', data=serializer.errors)

    def partial_update(self, request, pk=None):
        """
            :param request:
            :param pk:
            :return:
        """
        request.data["last_modified_by"] = self.request.user.username
        instance = get_or_none(CustomUser, id=pk)
        if not isinstance(instance, CustomUser):
            return error_response(data={},
                                  msg='User does not exists with id = {}'.format(pk),
                                  status=status.HTTP_404_NOT_FOUND)
        serializer = CustomUserSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return success_response(status=status.HTTP_202_ACCEPTED, msg='User is updated', data=serializer.data)
        return error_response(status=status.HTTP_400_BAD_REQUEST, msg='Invalid data', data=serializer.errors)

    def destroy(self, request, pk=None):
        """
            :param request:
            :param pk:
            :return:
        """
        request.data["last_modified_by"] = self.request.user.username
        instance = get_or_none(CustomUser, id=pk)
        if not isinstance(instance, CustomUser):
            return error_response(data={},
                                  msg='User does not exists with id = {}'.format(pk),
                                  status=status.HTTP_404_NOT_FOUND)

        serializer = CustomUserSerializer(
            instance=instance,
            data={"deleted": True, 'deleted_on': datetime.now()},
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return success_response(status=status.HTTP_202_ACCEPTED, msg='User is updated', data=serializer.data)
        return error_response(status=status.HTTP_400_BAD_REQUEST, msg='Invalid data', data=serializer.errors)

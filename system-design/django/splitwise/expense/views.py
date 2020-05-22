from datetime import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, generics, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from expense.filters import ExpenseFilter, ExpenseUserFilter, RepaymentFilter
from expense.models import Expense, Repayment, ExpenseUser
from expense.serializers import ExpenseSerializer, ExpenseUserSerializer, RepaymentSerializer
from utils.helpers import get_or_none
from utils.responses import success_response, error_response
from utils.search import CustomSearch


class ExpenseListView(generics.ListAPIView):
    serializer_class = ExpenseSerializer
    filter_backends = (CustomSearch, filters.OrderingFilter, DjangoFilterBackend)
    filter_class = ExpenseFilter
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
        return Expense.objects.order_by('-id')


class ExpenseViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        request.data["created_by"] = self.request.user.username
        request.data["last_modified_by"] = self.request.user.username
        serializer = ExpenseSerializer(data=request.data)
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
        instance = get_or_none(model=Expense, id=pk)
        if isinstance(instance, Expense):
            serializer = ExpenseSerializer(instance=instance)
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
        instance = get_or_none(Expense, id=pk)
        if not isinstance(instance, Expense):
            return error_response(data={}, msg='User does not exists with id = {}'.format(pk),
                                  status=status.HTTP_404_NOT_FOUND)
        serializer = ExpenseSerializer(instance=instance, data=request.data)
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
        instance = get_or_none(Expense, id=pk)
        if not isinstance(instance, Expense):
            return error_response(data={},
                                  msg='User does not exists with id = {}'.format(pk),
                                  status=status.HTTP_404_NOT_FOUND)
        serializer = ExpenseSerializer(instance=instance, data=request.data, partial=True)
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
        instance = get_or_none(Expense, id=pk)
        if not isinstance(instance, Expense):
            return error_response(data={},
                                  msg='User does not exists with id = {}'.format(pk),
                                  status=status.HTTP_404_NOT_FOUND)

        serializer = ExpenseSerializer(
            instance=instance,
            data={"deleted": True, 'deleted_on': datetime.now()},
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return success_response(status=status.HTTP_202_ACCEPTED, msg='User is updated', data=serializer.data)
        return error_response(status=status.HTTP_400_BAD_REQUEST, msg='Invalid data', data=serializer.errors)


class ExpenseUserListView(generics.ListAPIView):
    serializer_class = ExpenseUserSerializer
    filter_backends = (CustomSearch, filters.OrderingFilter, DjangoFilterBackend)
    filter_class = ExpenseUserFilter
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
        return ExpenseUser.objects.order_by('-id')


class ExpenseUserUserViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        request.data["created_by"] = self.request.user.username
        request.data["last_modified_by"] = self.request.user.username
        serializer = ExpenseUserSerializer(data=request.data)
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
        instance = get_or_none(model=ExpenseUser, id=pk)
        if isinstance(instance, ExpenseUser):
            serializer = ExpenseUserSerializer(instance=instance)
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
        instance = get_or_none(ExpenseUser, id=pk)
        if not isinstance(instance, ExpenseUser):
            return error_response(data={}, msg='User does not exists with id = {}'.format(pk),
                                  status=status.HTTP_404_NOT_FOUND)
        serializer = ExpenseUserSerializer(instance=instance, data=request.data)
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
        instance = get_or_none(ExpenseUser, id=pk)
        if not isinstance(instance, ExpenseUser):
            return error_response(data={},
                                  msg='User does not exists with id = {}'.format(pk),
                                  status=status.HTTP_404_NOT_FOUND)
        serializer = ExpenseUserSerializer(instance=instance, data=request.data, partial=True)
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
        instance = get_or_none(ExpenseUser, id=pk)
        if not isinstance(instance, ExpenseUser):
            return error_response(data={},
                                  msg='User does not exists with id = {}'.format(pk),
                                  status=status.HTTP_404_NOT_FOUND)

        serializer = ExpenseUserSerializer(
            instance=instance,
            data={"deleted": True, 'deleted_on': datetime.now()},
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return success_response(status=status.HTTP_202_ACCEPTED, msg='User is updated', data=serializer.data)
        return error_response(status=status.HTTP_400_BAD_REQUEST, msg='Invalid data', data=serializer.errors)


class RepaymentListView(generics.ListAPIView):
    serializer_class = RepaymentSerializer
    filter_backends = (CustomSearch, filters.OrderingFilter, DjangoFilterBackend)
    filter_class = RepaymentFilter
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
        return Repayment.objects.order_by('-id')


class RepaymentUserViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        request.data["created_by"] = self.request.user.username
        request.data["last_modified_by"] = self.request.user.username
        serializer = RepaymentSerializer(data=request.data)
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
        instance = get_or_none(model=Repayment, id=pk)
        if isinstance(instance, Repayment):
            serializer = RepaymentSerializer(instance=instance)
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
        instance = get_or_none(Repayment, id=pk)
        if not isinstance(instance, Repayment):
            return error_response(data={}, msg='User does not exists with id = {}'.format(pk),
                                  status=status.HTTP_404_NOT_FOUND)
        serializer = RepaymentSerializer(instance=instance, data=request.data)
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
        instance = get_or_none(Repayment, id=pk)
        if not isinstance(instance, Repayment):
            return error_response(data={},
                                  msg='User does not exists with id = {}'.format(pk),
                                  status=status.HTTP_404_NOT_FOUND)
        serializer = RepaymentSerializer(instance=instance, data=request.data, partial=True)
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
        instance = get_or_none(Repayment, id=pk)
        if not isinstance(instance, Repayment):
            return error_response(data={},
                                  msg='User does not exists with id = {}'.format(pk),
                                  status=status.HTTP_404_NOT_FOUND)

        serializer = RepaymentSerializer(
            instance=instance,
            data={"deleted": True, 'deleted_on': datetime.now()},
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return success_response(status=status.HTTP_202_ACCEPTED, msg='User is updated', data=serializer.data)
        return error_response(status=status.HTTP_400_BAD_REQUEST, msg='Invalid data', data=serializer.errors)

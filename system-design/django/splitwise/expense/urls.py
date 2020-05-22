from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from expense.views import ExpenseViewSet, ExpenseListView, ExpenseUserListView, RepaymentListView
from users.views import UserViewSet, CustomUserListView

router = DefaultRouter(trailing_slash=False)
router.register(r'expenses', ExpenseViewSet, basename='expenses')
router.register(r'expense-users', ExpenseViewSet, basename='expense-users')
router.register(r'repayments', ExpenseViewSet, basename='repayments')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = router.urls

urlpatterns += format_suffix_patterns([
    path('expense-list/', ExpenseListView.as_view(), name='users-list'),
    path('expense-user-list/', ExpenseUserListView.as_view(), name='users-list'),
    path('repayment-list/', RepaymentListView.as_view(), name='users-list'),
    path('user-list/', CustomUserListView.as_view(), name='users-list'),
])

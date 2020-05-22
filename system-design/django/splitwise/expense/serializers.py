from rest_framework import serializers

from expense.models import Expense, ExpenseUser, Repayment
from users.models import CustomUser


class CreateSerializerTemplate(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class ExpenseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    last_modified_at = serializers.DateTimeField(read_only=True)
    deleted = serializers.BooleanField(required=False)
    deleted_on = serializers.DateTimeField(allow_null=True, required=False)
    amount_currency = serializers.CharField(read_only=True)
    amount = serializers.DecimalField(allow_null=True, decimal_places=2, max_digits=10, required=False)
    description = serializers.CharField(max_length=255, required=False)
    date = serializers.DateField()
    category = serializers.CharField(max_length=10, required=False)
    status = serializers.ChoiceField(choices=(('pending', 'Pending'), ('settled', 'Settled'), ('deleted', 'Deleted')),
                                     required=False)
    created_by = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=CustomUser.objects.all(), required=False)
    last_modified_by = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=CustomUser.objects.all(),
                                                          required=False)

    def create(self, validated_data):
        instance = Expense.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        Expense.objects.filter(id=instance.id).update(**validated_data)
        return Expense.objects.get(id=instance.id)


class ExpenseUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    last_modified_at = serializers.DateTimeField(read_only=True)
    deleted = serializers.BooleanField(required=False)
    deleted_on = serializers.DateTimeField(allow_null=True, required=False)
    amount_currency = serializers.CharField(read_only=True)
    amount = serializers.DecimalField(allow_null=True, decimal_places=2, max_digits=10, required=False)
    description = serializers.CharField(max_length=255, required=False)
    date = serializers.DateField()
    category = serializers.CharField(max_length=10, required=False)
    status = serializers.ChoiceField(choices=(('pending', 'Pending'), ('settled', 'Settled'), ('deleted', 'Deleted')),
                                     required=False)
    created_by = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=CustomUser.objects.all(), required=False)
    last_modified_by = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=CustomUser.objects.all(),
                                                          required=False)

    def create(self, validated_data):
        instance = ExpenseUser.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        ExpenseUser.objects.filter(id=instance.id).update(**validated_data)
        return ExpenseUser.objects.get(id=instance.id)


class RepaymentSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    last_modified_at = serializers.DateTimeField(read_only=True)
    deleted = serializers.BooleanField(required=False)
    deleted_on = serializers.DateTimeField(allow_null=True, required=False)
    amount_currency = serializers.CharField(read_only=True)
    amount = serializers.DecimalField(allow_null=True, decimal_places=2, max_digits=10, required=False)
    description = serializers.CharField(max_length=255, required=False)
    date = serializers.DateField()
    category = serializers.CharField(max_length=10, required=False)
    status = serializers.ChoiceField(choices=(('pending', 'Pending'), ('settled', 'Settled'), ('deleted', 'Deleted')),
                                     required=False)
    created_by = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=CustomUser.objects.all(), required=False)
    last_modified_by = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=CustomUser.objects.all(),
                                                          required=False)

    def create(self, validated_data):
        instance = Repayment.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        Repayment.objects.filter(id=instance.id).update(**validated_data)
        return Repayment.objects.get(id=instance.id)

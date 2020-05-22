from django.core.exceptions import FieldError
from rest_framework import serializers

from users.models import CustomUser


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except (model.DoesNotExist, ValueError) as err:
        return None
    except model.MultipleObjectsReturned:
        return model.objects.filter(**kwargs).last()
    except TypeError:
        return None
    except FieldError:
        try:
            return model.objects.get(**kwargs)
        except (model.DoesNotExist, ValueError) as err:
            return None
        except model.MultipleObjectsReturned:
            return model.objects.filter(**kwargs).last()
        except TypeError:
            return None

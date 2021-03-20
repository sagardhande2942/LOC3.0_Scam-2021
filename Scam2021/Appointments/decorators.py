from django.core.exceptions import PermissionDenied
from Auth.models import Users

def user_is_doctor(function):
    def wrap(request, *args, **kwargs):
        user = Users.objects.get(pk=kwargs['user_id'])
        if user.is_doctor == True:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def user_is_patient(function):
    def wrap(request, *args, **kwargs):
        user = Users.objects.get(pk=kwargs['user_id'])
        if user.is_doctor == False:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
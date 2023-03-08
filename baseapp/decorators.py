from django.http import HttpResponse
from django.shortcuts import redirect

def not_allowed(not_allowed=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group=None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in not_allowed:
                return HttpResponse("You are unauthorized")
            else:
                return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator
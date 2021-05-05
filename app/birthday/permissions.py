from django.http import Http404
from django.shortcuts import render


class CurrentUserPermissionsMixin:
    def has_permissions(self):
        return self.get_object().user == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            return render(request, 'birthday/404.html')
        return super().dispatch(request, *args, **kwargs)

from rest_framework.permissions import BasePermission

SAFE_METHOD = ['GET', 'HEAD', 'OPTIONS']


class ModelPermissions(BasePermission):
    perms_map = {
        'GET': ['%(app_label)resources_api.list_%(model_name)resources_api'],
        'OPTIONS': ['%(app_label)resources_api.list_%(model_name)resources_api'],
        'HEAD': [],
        'POST': ['%(app_label)resources_api.add_%(model_name)resources_api'],
        'PUT': ['%(app_label)resources_api.change_%(model_name)resources_api'],
        'PATCH': ['%(app_label)resources_api.change_%(model_name)resources_api'],
        'DELETE': ['%(app_label)resources_api.delete_%(model_name)resources_api'],
    }
    authenticated_users_only = True

    def get_required_permissions(self, method, model_cls):
        kwargs = {
            'app_label': model_cls._meta.app_label,
            'model_name': model_cls._meta.model_name
        }
        return [perm % kwargs for perm in self.perms_map[method]]

    def has_permission(self, request, view):
        if request.method in SAFE_METHOD:
            return True
        if getattr(view, '_ignore_model_permissions', False):
            return True
        if hasattr(view, 'get_queryset'):
            queryset = view.get_queryset()
        else:
            queryset = getattr(view, 'queryset', None)

        assert queryset is not None, (
            'Cannot apply DjangoModelPermissions on a view that '
            'does not set `.queryset` or have a `.get_queryset()` method.'
        )
        perms = self.get_required_permissions(request.method, queryset.model)
        return (
                request.user and
                (request.user.is_authenticated or not self.authenticated_users_only) and
                request.user.has_perms(perms)
        )

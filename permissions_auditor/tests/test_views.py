"""Views used for testing."""
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import (
    login_required, permission_required, user_passes_test
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
)
from django.views.generic import View


class BaseView(View):
    pass


class LoginRequiredView(LoginRequiredMixin, View):
    pass


class PermissionRequiredView(PermissionRequiredMixin, View):
    permission_required = 'tests.test_perm'


class PermissionRequiredViewDocstring(PermissionRequiredMixin, View):
    permission_required = 'tests.test_perm'

    def has_permission(self):
        """Custom docstrings should be detected."""
        return super().has_permission()


class PermissionRequiredViewNoDocstring(PermissionRequiredMixin, View):
    permission_required = 'tests.test_perm'

    def has_permission(self):
        return super().has_permission()


class UserPassesTestView(UserPassesTestMixin, View):
    def test_func(self):
        return True


class UserPassesTestViewDocstring(UserPassesTestMixin, View):
    def test_func(self):
        """Custom docstrings should be detected."""
        return True


class UserPassesTestViewNoDocstring(UserPassesTestMixin, View):
    def test_func(self):
        return True


class UserPassesTestViewCustomFunc(UserPassesTestMixin, View):
    def get_test_func(self):
        return self.custom_test_func

    def custom_test_func(self):
        """Custom docstrings should be detected."""
        return True


# Function Based Views


def base_view(request):
    pass


@login_required
def login_required_view(request):
    pass


@permission_required('tests.test_perm')
def permission_required_view(request):
    pass


@staff_member_required
def staff_member_required_view(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def superuser_required_view(request):
    pass


@user_passes_test(lambda u: u.email is not None)
def user_passes_test_view(request):
    pass

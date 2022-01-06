from django.shortcuts import redirect
from django.urls import reverse


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and not self.__is_excluded_route(request):
            login_url: str = reverse('core-login-view')
            if request.path != '/' and request.path != reverse('dashboard-view'):
                return redirect('%s?next=%s' % (login_url, request.path))

            return redirect(login_url)

        response = self.get_response(request)

        return response

    def __is_excluded_route(self, request) -> bool:
        excluded = [
            request.path == reverse('core-login-view'),
            request.path == reverse('welcome-view'),
        ]

        return any(excluded)

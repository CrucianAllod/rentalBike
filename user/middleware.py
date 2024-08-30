from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from django.conf import settings
from django.http import JsonResponse

class JWTValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == 401 and settings.DEBUG:
            return JsonResponse({'detail': 'Unauthorized.'}, status=401)

        return response

    def process_exception(self, request, exception):
        if isinstance(exception, (InvalidToken, AuthenticationFailed)):
            return JsonResponse({'detail': 'Invalid token.'}, status=401)
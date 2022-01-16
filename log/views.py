from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from car.models import Car
from log.models import CarLog


@csrf_exempt
@require_http_methods(['POST'])
def daily_mileage_report(request, car_id: int):
    authorization_token = request.headers.get('authorization')
    if authorization_token:
        car = Car.objects.get(id=car_id)

        if str(car.token) == authorization_token:
            new_log = CarLog.objects.create(
                mileage=request.POST.get('mileage'),
                car=car,
            )

            new_log.save()
            return JsonResponse({
                "code": 200,
                "status": "success",
                "data": []
            }, status=200)

    return JsonResponse({
                "code": 403,
                "status": "Forbidden",
                "data": []
            }, status=403)

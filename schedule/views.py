from django.http import HttpResponse
from schedule.services.generate_schedule_service import GenerateScheduleService


def generate_schedule(request):
    generate_schedule_service = GenerateScheduleService()
    generate_schedule_service.generate()

    return HttpResponse({'status': 'success', 'code': 200}, content_type='application/json')

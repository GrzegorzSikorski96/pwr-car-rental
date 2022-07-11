import datetime
from unittest.mock import patch

from django.test import TestCase

from car.tests.helpers.sample_objects import sample_car, sample_engine
from core.tests.helpers.sample_objects import sample_user
from log.models import ServiceLog, CarLog, MessageLog
from log.tests.helpers.sample_objects import sample_car_log, sample_service_log, sample_message_log


class CarModelTestCase(TestCase):
    def setUp(self) -> None:
        self.user = sample_user(email='username@example.com')

    def test_should_create_service_log_after_car_was_created(self):
        car = sample_car()

        self.assertEqual(1, ServiceLog.objects.all().count())

        service_log: ServiceLog = car.services.first()

        self.assertEqual('Car added to rental system.', service_log.action)
        self.assertEqual('', service_log.description)
        self.assertEqual(1500, service_log.mileage)
        self.assertEqual(16500, service_log.next_service_mileage)
        self.assertEqual(
            datetime.date(service_log.created_at.year + 1, service_log.created_at.month, service_log.created_at.day),
            service_log.next_service_date
        )
        self.assertEqual(self.user, service_log.created_by)

    def test_should_remove_all_service_logs_and_messages_when_car_is_deleted(self):
        car = sample_car(mileage=154000)

        sample_car_log(car=car, mileage=156000)
        sample_car_log(car=car, mileage=157000)
        self.assertEqual(2, CarLog.objects.all().count())

        sample_service_log(car=car)
        sample_service_log(car=car)
        self.assertEqual(3, ServiceLog.objects.all().count())

        sample_message_log(car=car)
        sample_message_log(car=car)
        sample_message_log(car=car)
        self.assertEqual(3, MessageLog.objects.all().count())

        car.delete()

        self.assertEqual(0, CarLog.objects.all().count())
        self.assertEqual(0, ServiceLog.objects.all().count())
        self.assertEqual(0, MessageLog.objects.all().count())

    def test_should_return_last_service_log_for_car(self):
        car = sample_car()

        service_log = sample_service_log(car=car, next_service_mileage=16000, next_service_date='2023-01-03')

        self.assertEqual(service_log, car.last_service())

    def test_should_return_next_service_mileage(self):
        car = sample_car()

        sample_service_log(car=car, next_service_mileage=16000, next_service_date='2023-01-03')

        self.assertEqual(16000, car.next_service_mileage())

    def test_should_return_days_to_service(self):
        car = sample_car()

        sample_service_log(car=car, next_service_date='2022-12-25')
        sample_service_log(car=car, next_service_date='2023-01-28')

        with patch('car.models.datetime', wraps=datetime) as mock_datetime:
            mock_datetime.date.today.return_value = datetime.date(2023, 1, 3)
            self.assertEqual(25, car.days_to_service())

    def test_should_return_kilometers_to_service(self):
        car = sample_car(mileage=150000)

        sample_service_log(car=car, next_service_mileage=160000)

        self.assertEqual(10000, car.kilometers_to_service())

    def test_should_return_car_string_on_object_stringify(self):
        car = sample_car(manufacturer="Manufacturer", model='Model', registration_number="ASD")

        self.assertEqual("#%d - %s %s - %s" % (car.pk, car.manufacturer, car.model, car.registration_number),
                         car.__str__()
                         )


class EngineModelTestCase(TestCase):
    def test_should_return_car_string_on_object_stringify(self):
        engine = sample_engine(volume=123, horsepower=123, fuel_type='diesel')

        self.assertEqual("#%d - %s cc, %s hp, %s" % (engine.pk, engine.volume, engine.horsepower, engine.fuel_type),
                         engine.__str__()
                         )

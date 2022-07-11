import random
import re

from django.core.management import call_command
from django.http import HttpResponseRedirect, HttpResponse
from django.test import TestCase
from django.urls import reverse

from car.tests.helpers.sample_objects import sample_car
from core.choices.group_choices import GroupId
from core.tests.helpers.sample_objects import sample_user
from rent.tests.helpers.sample_objects import sample_rent

CAR_CLIENT_LIST_VIEW = reverse('client-cars-list-view')
CAR_EMPLOYEE_LIST_VIEW = reverse('dashboard-cars-list-view')


class PublicClientCarViewTestCase(TestCase):
    def test_anonymous_user_should_not_see_client_cars_list(self) -> None:
        response: HttpResponseRedirect = self.client.get(CAR_CLIENT_LIST_VIEW)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '%s?next=%s' % (reverse('core-login-view'), CAR_CLIENT_LIST_VIEW))


class PublicEmpolyeeCarViewTestCase(TestCase):
    def test_anonymous_user_should_not_see_employee_cars_list(self) -> None:
        response: HttpResponseRedirect = self.client.get(CAR_EMPLOYEE_LIST_VIEW)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '%s?next=%s' % (reverse('core-login-view'), CAR_EMPLOYEE_LIST_VIEW))


class PrivateEmployeeCarViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        call_command('create_user_groups_with_permissions')
        cls.user = sample_user(email='username@example.com', groups=[GroupId.EMPLOYEE])

        for i in range(1, 101):
            sample_car(
                manufacturer='Manufacturer_'+str(i),
                model='Model_'+str(i),
                mileage=random.randint(15000, 160000),
                air_conditioning=bool(random.randint(0, 1)),
                seats=random.randint(1, 5),
                trunk_volume=random.randint(1, 5),
                registration_number='DLB '+str(i),
            )

    def setUp(self):
        self.client.login(username='username@example.com', password='password')

    def test_employee_should_see_car_list_view(self):
        response: HttpResponse = self.client.get(reverse('dashboard-cars-list-view'))
        self.assertEqual(response.status_code, 200)

    def test_employee_should_see_all_cars(self):
        response: HttpResponse = self.client.get(reverse('dashboard-cars-list-view'))
        str_response: str = response.content.decode('utf-8')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(100, len(re.findall('Manufacturer_', str_response)))


class PrivateClientCarViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        call_command('create_user_groups_with_permissions')
        cls.user = sample_user(email='username@example.com', is_superuser=False, groups=[GroupId.CLIENT])

        for i in range(1, 5):
            sample_car(
                manufacturer='Manufacturer_'+str(i),
                model='Model_'+str(i),
                mileage=random.randint(15000, 160000),
                air_conditioning=bool(random.randint(0, 1)),
                seats=random.randint(1, 5),
                trunk_volume=random.randint(1, 5),
                registration_number='DLB '+str(i),
            )

        for i in range(9, 13):
            sample_car(
                manufacturer='Manufacturer_'+str(i),
                model='Model_'+str(i),
                mileage=random.randint(15000, 160000),
                air_conditioning=bool(random.randint(0, 1)),
                seats=random.randint(1, 5),
                trunk_volume=random.randint(1, 5),
                registration_number='DLB '+str(i),
            )

    def setUp(self):
        self.client.login(username='username@example.com', password='password')

        for i in range(6, 8):
            car = sample_car(
                manufacturer='Manufacturer_' + str(i),
                model='Model_' + str(i),
                mileage=random.randint(15000, 160000),
                air_conditioning=bool(random.randint(0, 1)),
                seats=random.randint(1, 5),
                trunk_volume=random.randint(1, 5),
                registration_number='DLB ' + str(i),
            )
            sample_rent(rented_car=car, rented_by=self.user)

    def test_client_should_see_car_list_view(self):
        response: HttpResponse = self.client.get(reverse('client-cars-list-view'))
        self.assertEqual(response.status_code, 200)

    def test_client_should_get_403_forbidden_error_when_enter_dashboard_car_list_view(self):
        response: HttpResponse = self.client.get(reverse('dashboard-cars-list-view'))
        self.assertEqual(response.status_code, 403)

    def test_client_should_see_only_rented_by_him_car_list_view(self):
        response: HttpResponse = self.client.get(reverse('client-cars-list-view'))
        str_response: str = response.content.decode('utf-8')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(2, len(re.findall('Manufacturer_', str_response)))

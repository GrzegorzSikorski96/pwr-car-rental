class CarStatus:
    RENTED_STATUS = 'rented'
    NEED_SERVICE_STATUS = 'need service'
    IN_SERVICE_STATUS = 'in service'
    READY_TO_RENT_STATUS = 'ready to rent'

    CAR_STATUS_CHOICES = [
        (RENTED_STATUS, 'Rented'),
        (NEED_SERVICE_STATUS, 'Need service'),
        (IN_SERVICE_STATUS, 'In service'),
        (READY_TO_RENT_STATUS, 'Ready to rent'),
    ]

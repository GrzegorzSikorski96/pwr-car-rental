class LogMessage:
    SERVICE_REQUESTED_BY_EMPLOYEE = 'service requested by employee'
    SERVICE_REQUESTED_BY_CLIENT = 'service requested by client'

    LOG_MESSAGE_CHOICES = [
        (SERVICE_REQUESTED_BY_EMPLOYEE, 'Service requested by employee'),
        (SERVICE_REQUESTED_BY_CLIENT, 'Service requested by client')
    ]


class LogAction:
    SERVICE_REQUESTED = 'service requested'

    LOG_ACTION_CHOICES = [
        (SERVICE_REQUESTED, 'service requested')
    ]

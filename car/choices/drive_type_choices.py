class DriveType:
    ALL_WHEEL_DRIVE_TYPE = 'all wheel drive'
    FOUR_WHEEL_DRIVE_TYPE = 'four wheel drive'
    FRONT_WHEEL_DRIVE_TYPE = 'front wheel drive'
    REAR_WHEEL_DRIVE_TYPE = 'rear wheel drive'

    DRIVE_TYPE_CHOICES = [
        (ALL_WHEEL_DRIVE_TYPE, 'All wheel drive'),
        (FOUR_WHEEL_DRIVE_TYPE, 'Four wheel drive'),
        (FRONT_WHEEL_DRIVE_TYPE, 'Front wheel drive'),
        (REAR_WHEEL_DRIVE_TYPE, 'Rear wheel drive'),
    ]

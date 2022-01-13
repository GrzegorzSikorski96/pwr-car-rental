class DrivetrainType:
    ALL_WHEEL_DRIVETRAIN_TYPE = 'all wheel drive'
    FOUR_WHEEL_DRIVETRAIN_TYPE = 'four wheel drive'
    FRONT_WHEEL_DRIVETRAIN_TYPE = 'front wheel drive'
    REAR_WHEEL_DRIVETRAIN_TYPE = 'rear wheel drive'

    DRIVETRAIN_TYPE_CHOICES = [
        (ALL_WHEEL_DRIVETRAIN_TYPE, 'All wheel drive'),
        (FOUR_WHEEL_DRIVETRAIN_TYPE, 'Four wheel drive'),
        (FRONT_WHEEL_DRIVETRAIN_TYPE, 'Front wheel drive'),
        (REAR_WHEEL_DRIVETRAIN_TYPE, 'Rear wheel drive'),
    ]

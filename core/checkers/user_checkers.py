def has_group(user, name: str) -> bool:
    if user is None:
        return False
    return user.groups.filter(name=name).exists()

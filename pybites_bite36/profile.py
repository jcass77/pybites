def get_profile(name, age, *args, **kwargs):
    if type(age) != int or len(args) > 5:
        raise ValueError

    profile = {
        "name": name,
        "age": age,
    }
    if args:
        profile["sports"] = sorted([*args])

    if kwargs:
        profile["awards"] = kwargs

    return profile

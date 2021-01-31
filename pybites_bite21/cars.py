import itertools
import re

cars = {
    "Ford": ["Falcon", "Focus", "Festiva", "Fairlane"],
    "Holden": ["Commodore", "Captiva", "Barina", "Trailblazer"],
    "Nissan": ["Maxima", "Pulsar", "350Z", "Navara"],
    "Honda": ["Civic", "Accord", "Odyssey", "Jazz"],
    "Jeep": ["Grand Cherokee", "Cherokee", "Trailhawk", "Trackhawk"],
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
    (original order)"""
    return ", ".join(cars["Jeep"])


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    return [models[0] for models in cars.values()]


def get_all_matching_models(cars=cars, grep="trail"):
    """return a list of all models containing the case insensitive
    'grep' string which defaults to 'trail' for this exercise,
    sort the resulting sequence alphabetically"""
    pat = re.compile(grep, flags=re.IGNORECASE)

    return sorted(
        [
            model
            for model in itertools.chain.from_iterable(cars.values())
            if pat.search(model)
        ]
    )


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
    sorted alphabetically"""
    return {manufacturer: sorted(models) for manufacturer, models in cars.items()}

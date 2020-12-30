names = "Julian Bob PyBites Dante Martin Rodolfo".split()
countries = "Australia Spain Global Argentina USA Mexico".split()


def enumerate_names_countries():
    """Outputs:
    1. Julian     Australia
    2. Bob        Spain
    3. PyBites    Global
    4. Dante      Argentina
    5. Martin     USA
    6. Rodolfo    Mexico"""
    for i, details in enumerate(zip(names, countries), start=1):
        name, country = details
        print((f"{i}. {name.ljust(11)}{country}"))

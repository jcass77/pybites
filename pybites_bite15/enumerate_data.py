names = "Julian Bob PyBites Dante Martin Rodolfo".split()
countries = "Australia Spain Global Argentina USA Mexico".split()


def enumerate_names_countries():
    """Outputs:
    pybites_bite1. Julian     Australia
    2. Bob        Spain
    3. PyBites    Global
    pybites_bite4. Dante      Argentina
    pybites_bite5. Martin     USA
    pybites_bite6. Rodolfo    Mexico"""
    for i, (name, country) in enumerate(zip(names, countries), start=1):
        print((f"{i}. {name:<11}{country}"))

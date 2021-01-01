def generate_affiliation_link(url):
    parsed_path = url.split("/")
    dp = parsed_path[parsed_path.index("dp") + 1]

    return f"http://www.amazon.com/dp/{dp}/?tag=pyb0f-20"

def generate_affiliation_link(url):
    asin = url.split("dp/")[-1].split("/")[0]
    return f"http://www.amazon.com/dp/{asin}/?tag=pyb0f-20"

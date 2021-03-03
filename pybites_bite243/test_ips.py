import json
import os
from pathlib import Path
from ipaddress import IPv4Network
from urllib.request import urlretrieve

import pytest

from ips import ServiceIPRange, parse_ipv4_service_ranges, get_aws_service_range

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network("192.0.2.8/29")


@pytest.fixture(scope="module")
def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH


class TestServiceIPRange:
    def test_str(self):

        ipr = ServiceIPRange("dummy_service", "dummy_region", IP)
        assert (
            str(ipr)
            == f"192.0.2.8/29 is allocated to the dummy_service service in the dummy_region region"
        )


def test_parse_ipv4_service_ranges_returns_all_prefixes(json_file):
    prefixes = json.loads(json_file.read_text())["prefixes"]
    ranges = parse_ipv4_service_ranges(json_file)

    assert len(ranges) == len(prefixes)


def test_parse_ipv4_service_ranges_handles_no_prefixes_available(tmp_path, json_file):
    data = json.loads(json_file.read_text())

    # Remove prefixes
    data["prefixes"] = []

    json_empty_file = Path(tmp_path, "ip-ranges-invalid.json")
    with open(json_empty_file, mode="w+") as f:
        json.dump(data, f)

    json_empty_file = Path(tmp_path, "ip-ranges-invalid.json")
    ranges = parse_ipv4_service_ranges(json_empty_file)

    assert len(ranges) == 0


def test_parse_ipv4_service_ranges_skips_invalid_addresses_without_raising_exception(
    tmp_path, json_file
):
    data = json.loads(json_file.read_text())

    # Create at least one invalid address entry
    data["prefixes"][0]["ip_prefix"] = "invalid_address"

    json_error_file = Path(tmp_path, "ip-ranges-invalid.json")
    with open(json_error_file, mode="w+") as f:
        json.dump(data, f)

    assert len(parse_ipv4_service_ranges(json_error_file)) == len(data["prefixes"]) - 1


def test_get_aws_service_range_returns_correct_ranges(json_file):
    prefixes = json.loads(json_file.read_text())["prefixes"]
    ranges = parse_ipv4_service_ranges(json_file)

    assert len(get_aws_service_range("13.248.118.1", ranges)) == 2


def test_get_aws_service_range_invalid_address_raises_exception():
    with pytest.raises(ValueError, match="Address must be a valid IPv4 address"):
        get_aws_service_range("invalide_address", [])


def test_get_aws_service_range_no_service_ranges_returns_empty_list():
    assert len(get_aws_service_range(str(IP.network_address), [])) == 0

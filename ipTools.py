from netaddr import *
import ipaddress
import iprange
import ipaddress


def separateRange(_ipRange: str, div: int):
    resultListRanges = []
    start, end = _ipRange.split('-')
    diff = int(ipaddress.IPv4Address(end)) - int(ipaddress.IPv4Address(start))
    while diff > div:
        resultListRanges.append(str(start) + '-' + str(ipaddress.ip_address(start) + div))
        start = ipaddress.ip_address(start) + div
        diff -= div
    resultListRanges.append(str(start) + '-' + str(end))
    return resultListRanges



if __name__ == '__main__':
    print('\n'.join(separateRange("5.139.0.4-5.139.45.122", 512)))


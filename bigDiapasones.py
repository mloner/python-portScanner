import socket
from multiprocessing import Pool
from netaddr import *

from datetime import datetime
import time


def port_scan(arg):
    host, port = arg

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        print(host, 'Port :', port, " TRY.")
        s.connect((host, port))
        print(host, 'Port :', port, "is open.")
        s.close()

        return port, True
    except (socket.timeout, socket.error):
        return port, False


if __name__ == '__main__':

    print('-' * 38)
    ipStart, ipEnd = input("Enter IP-IP: ").split("-")
    iprange = IPRange(ipStart, ipEnd)
    number = int(input('Number of processes: '))
    print('-' * 38)

    ports = [8000]
    '''[43, 80, 109, 110, 115, 118, 119, 143,
            194, 220, 443, 540, 585, 591, 1112, 1433, 1443, 3128, 3197,
            3306, 4000, 4333, 5100, 5432, 6669, 8000, 8080, 9014, 9200]'''
    pool = Pool(processes=number)

    start_time = datetime.now()
    for ip in iprange:
        host = str(ip)
        for port in pool.imap_unordered(port_scan, [(host, port) for port in ports]):
            pass

    print('\nScanning Completed in:' + str(datetime.now() - start_time), "seconds")
    input('Enter to exit')
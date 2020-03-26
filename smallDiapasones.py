import sys
import threading
import socket
from netaddr import *
from datetime import datetime

goodHosts = []
threads = []

debug_mode = False

def debug_print(msg):
    if debug_mode == True:
        print(msg)

def port_scan(port, host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        connection = s.connect((host, port))
        print(host, 'Port :', port, "is open.")
        goodHosts.append(str(host) + ' : ' + str(port))
        connection.close()
    except:
        pass


def main():
    start_time = datetime.now()

    debug_print('-' * 36)
    port = 22
    if len(sys.argv) > 1:
        line = sys.argv[1]
    else:
        file = open("ips.txt", "r")
        line = file.read()
        file.close()
    ipStart, ipEnd = line.split("-")
    iprange = IPRange(ipStart, ipEnd)
    debug_print(line)
    for ip in iprange:
        host = str(ip)
        t = threading.Thread(target=port_scan, args=(port, host))
        try:
            t.start()
            threads.append(t)
        except:
            debug_print('fail: ' + str(t.ident))
    for t in threads:
        t.join()
    if len(goodHosts) > 0:
        debug_print('good ips : ' + str(goodHosts))
    fileout = open("goodips.txt", "a")
    try:
        for el in goodHosts:
            fileout.write(el)
            fileout.write('\n')
    except:
        debug_print('Ошибка записи')
    finally:
        fileout.close()

    debug_print("elapsed time: " + str(datetime.now() - start_time))
    debug_print('-' * 36)


if __name__ == '__main__':
    main()

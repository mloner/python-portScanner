import os
import time
import ipTools

debug_mode = False

def debug_print(msg):
    if debug_mode == True:
        print(msg)
if __name__ == '__main__':
    file = open("ips.txt", "r")
    rangeList = []
    for range in file:
        if str(range)[-1] == str('\n'):
            range = range[:-1]
        lst = ipTools.separateRange(range, 512)
        for el in lst:
            rangeList.append(el)
    print(len(rangeList))
    for range in rangeList:
        cmd = 'python smallDiapasones.py ' + str(range)
        import subprocess
        PIPE = subprocess.PIPE
        p = subprocess.Popen(cmd, shell=True)
        p.wait()
    print('main script is done')
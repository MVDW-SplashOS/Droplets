import re
import subprocess
import time



devices = []



print("[INFO] Starting BAS Service...")




def check_new_devices():

    device_re = re.compile(b"Bus\s+(?P<bus>\d++)\s+Device\s+(?P<device>\d++).+?ID\s(?P<id>\w+:\w++)\s(?P<tag>.+)$", re.I | re.DOTALL)
    df = subprocess.check_output("lsusb")

    for i in df.split(b'\n'):
        if i:
            info = device_re.match(i)
            if info:
                dinfo = info.groupdict()
                dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
                if dinfo not in devices:
                    devices.append(dinfo)
                    print("[INFO] New Device: ", dinfo)
            
while True:
    check_new_devices()
    time.sleep(0.5)
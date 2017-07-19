#Lidar2 addr: 20:16:03:03:50:45
#uuid "00001101-0000-1000-8000-00805F9B34FB"

import bluetooth
from pprint import pprint

target_name = "Lidar2"
target_address = None

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    print('device ', bdaddr)
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

#service = find_service(address='00:yy:72:zz:bb:aa')
#pprint(service)

if target_address is not None:
    print("found target bluetooth device with address ", target_address)
else:
    print("could not find target bluetooth device nearby")

#services = bluetooth.find_service(address='20:16:03:03:50:45')
services = bluetooth.find_service(uuid="1101")

#services = bluetooth.find_service(uuid="00001101-0000-1000-8000-00805F9B34FB")

if len(services) > 0:
    print("found %d services on %s" % (len(services), target_name))
    print()
else:
    print("no services found")

pprint(services)

for svc in services:
    print("Service Name: %s"    % svc["name"])
    print("    Host:        %s" % svc["host"])
    print("    Description: %s" % svc["description"])
    print("    Provided By: %s" % svc["provider"])
    print("    Protocol:    %s" % svc["protocol"])
    print("    channel/PSM: %s" % svc["port"])
    print("    svc classes: %s "% svc["service-classes"])
    print("    profiles:    %s "% svc["profiles"])
    print("    service id:  %s "% svc["service-id"])
    print()

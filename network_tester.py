import socket
import csv
import enum
import netifaces as nf
from datetime import datetime
from time import sleep

FREQUENCY_SECS = 3

def getGateway():
    try:
        gateway = nf.gateways()['default'][nf.AF_INET][0]
        return gateway
    except KeyError:
        return None

def isReachable(ip_addr):
    try:
        return socket.gethostbyaddr(ip_addr)
    except socket.herror:
        return None

now = datetime.now().strftime("%d-%m-%Y %H_%M_%S")
f = open(now + ".csv", 'w')
csv_writer = csv.writer(f, dialect='excel')
csv_writer.writerow(['Timestamp', 'Connection status'])

print("Beginning internet monitor")

while True:
    sleep(FREQUENCY_SECS)
    timestamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    if getGateway() is None:
        csv_writer.writerow([timestamp, 'No Connection'])
        print(timestamp + ": No Connection")
    elif isReachable('8.8.8.8') is None:
        csv_writer.writerow([timestamp, 'Connection to Router'])
        print(timestamp + ": Connection to Router")
    else:
        csv_writer.writerow([timestamp, 'Connection to Internet'])
        print(timestamp + ": Connection to Internet")
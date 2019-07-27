import socket
import csv
import netifaces as nf
from datetime import datetime
from time import sleep
from tkinter import Tk
import tkinter.filedialog as fileDialog

FREQUENCY_SECS = 5

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

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
saveFile = fileDialog.asksaveasfile(defaultextension='.csv') # show an "Open" dialog box and return the path to the selected file
print("Setting save location to {saveFile.name}")

csv_writer = csv.writer(saveFile, dialect='excel')
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
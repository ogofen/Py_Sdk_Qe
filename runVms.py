#!/usr/bin/python
from ovirtsdk.api import API
from ovirtsdk.xml import params
from sdk_connect import Connect
import sys
api = Connect()

def runVms(self):
    """	run all VM's"""

    VMs = api.vms.list()
    for VM in VMs:
        VM.start()

if __name__ == "__main__":
    runVms("name")


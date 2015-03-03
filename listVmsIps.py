#!/usr/bin/python
import ovirtsdk.xml.params as params
import ovirtsdk.api
import sys
from sdk_connect import Connect
api = Connect()
def listVmsIps():
    """ list all VM's and their ips """

    for VM in api.vms.list():
        ga = VM.get_guest_info()
        ip = ga.ips.ip[0].get_address()
        print "%s ip is -> %s" %(VM.get_name(),ip)


if __name__ == "__main__":
        listVmsIps()

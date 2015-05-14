#!/usr/bin/python
import ovirtsdk.xml.params as params
import ovirtsdk.api
import sys
from sdk_connect import connect
from time import sleep
import pudb

def removedomainbyname(domain_name):
    """ removes a domain """

    api = connect(False)
    sd = api.datacenters.list()[0].storagedomains.get(domain_name)
    sd.deactivate()
    while sd.get_status().get_state() != 'maintenance':
        sd = api.datacenters.list()[0].storagedomains.get(domain_name)
        sleep(1)
    sd.delete()
    sleep(1)
    sd = api.storagedomains.get(domain_name)
    sd.delete(api.hosts.list()[0])

if __name__ == "__main__":
    removedomainbyname("nfs")
    print "operation successful"
    sys.exit(0)

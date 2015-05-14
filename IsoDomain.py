#!/usr/bin/python
from ovirtsdk.xml import params
import sdk_connect
import sys

def iso_create(path_, address_, api):
    storage_nfs = params.StorageDomain(data_center=api.datacenters.list()[0],
                                       type_='iso',
                                       storage=params.Storage(type_='nfs', address=address_,
                                                              path=path_),
                                       host=params.Host(name=api.hosts.list()[0].get_name()))
    newsd = api.storagedomains.add(storage_nfs)
    api.datacenters.list()[0].storagedomains.add(newsd)

if __name__ == "__main__":
    api = sdk_connect.connect()
    iso_create('/RHEV/ogofen/iso-domain-ogofen', '10.35.160.108', api)
    print "Finished successfully"
    sys.exit(0)

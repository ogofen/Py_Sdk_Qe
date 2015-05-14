#!/usr/bin/python
from ovirtsdk.xml import params
import sdk_connect
api = sdk_connect.connect()


def nfs_create(path_, address_):

    storage_nfs = params.StorageDomain(data_center=api.datacenters.list()[0], type_='data',
                                       storage=params.Storage(type_='nfs', address=address_, path=path_),
                                       host=params.Host(name=api.hosts.list()[0].get_name()), name=path_)
    newsd = api.storagedomains.add(storage_nfs)
    api.datacenters.list()[0].storagedomains.add(newsd)

if __name__ == "__main__":
    nfs_create('/RHEV/ogofen/11', '10.35.160.108')

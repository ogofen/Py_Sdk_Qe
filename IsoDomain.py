#!/usr/bin/python
from ovirtsdk.api import API
from ovirtsdk.xml import params
import time
import sdk_connect
api = sdk_connect.Connect()

def Iso_Create(path_,address_):
    storage_nfs = params.StorageDomain(
            data_center=api.datacenters.list()[0],
            type_='iso',
            storage=params.Storage(type_='nfs',
                address=address_,path=path_),
            host=params.Host(
                name=api.hosts.list()[0].get_name()))
    NewSd = api.storagedomains.add(storage_nfs)
    api.datacenters.list()[0].storagedomains.add(NewSd)

if __name__ == "__main__":
    Iso_Create('/RHEV/ogofen/rhevm-3-iso','10.35.160.108')

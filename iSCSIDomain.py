#!/usr/bin/python
import ovirtsdk.xml.params as params
import ovirtsdk.api
import sys
from sdk_connect import connect

def iscsi_create_(domain_name, i):
    """ lets create an iSCSI domain """

    api = connect()
    host1 = api.hosts.list()[0]
    storage_ = host1.storage.list()
    iscsi_storage = params.Storage(type_='iscsi',
                                   volume_group=params.VolumeGroup())
    SD = params.StorageDomain(name=domain_name, format='True',
                              host=host1, type_='data', storage_format='v3')
    storage_len = len(storage_)
    lun_list = list()
    for x in range(0, storage_len):
        try:
            if storage_[x].get_type() is None:
                raise Exception('Bug: FiberChannel type is None')
            if storage_[x].get_type() == 'nfs':
                raise Exception('nfs?')
            if storage_[x].get_type() == 'glusterfs':
                raise Exception('gluster?')
                raise Exception('gluster?')
        except Exception, e:
            print "caught", e
            continue
        else:
            lun_list.append(storage_[x].get_logical_unit()[0])
    try:
        if len(lun_list) == 0:
            raise Exception("operation stopped, Discover and Login to sessions"
                            "first")
    except Exception, e:
        print e
        return
    else:
        storage = list()
        print "we are here"
        storage.append(lun_list[i])
        iscsi_storage.set_logical_unit(storage)
        SD.set_storage(iscsi_storage)
    try:
        print "we finally"
        newsd = api.storagedomains.add(SD)
    except Exception, e:
        print "A problem caught during creating the domain --->", e
        return
    api.datacenters.list()[0].storagedomains.add(newsd)


def iSCSI_Create(domain_name):
    """ lets create an iSCSI domain """

    api = connect()
    host1 = api.hosts.list()[0]
    storage_ = host1.storage.list()
    iscsi_storage = params.Storage(type_='iscsi',
                                   volume_group=params.VolumeGroup())
    SD = params.StorageDomain(name=domain_name, format='True',
                              host=host1, type_='data', storage_format='v3')
    storage_len = len(storage_)
    lun_list = list()
    for x in range(0, storage_len):
        try:
            if storage_[x].get_type() is None:
                raise Exception('Bug: FiberChannel type is None')
            if storage_[x].get_type() == 'nfs':
                raise Exception('nfs?')
            if storage_[x].get_type() == 'glusterfs':
                raise Exception('gluster?')
                raise Exception('gluster?')
        except Exception, e:
            print "caught", e
            continue
        else:
            lun_list.append(storage_[x].get_logical_unit()[4])
    try:
        if len(lun_list) == 0:
            raise Exception("operation stopped, Discover and"
                            "Login to sessions first")
    except Exception, e:
        print e
        return
    else:
        print "Creating iSCSI Domain"
        firstindex = None
        Storage = list()
        for index in range(0, len(lun_list)):
            print lun_list[index].get_status()
            if lun_list[index].get_status() == 'free':
                print "we are here"
                if firstindex is not None:
                    Storage.append(lun_list[FirstIndex])
                    Storage.append(lun_list[index])
                    iscsi_storage.set_logical_unit(Storage)
                    SD.set_storage(iscsi_storage)
                    print "we are here"
                    break
                firstindex = index
    try:
        print "we finally"
        NewSd = api.storagedomains.add(SD)
    except Exception, e:
        print "A problem caught during creating the domain --->", e
        return
    api.datacenters.list()[0].storagedomains.add(NewSd)
if __name__ == "__main__":
    iscsi_create_("iSCSIAutomate1", 2)

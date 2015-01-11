#!/usr/bin/python
import ovirtsdk.xml.params as params
import ovirtsdk.api
import sys
import pudb
#pudb.set_trace()
from sdk_connect import Connect
api = Connect()
def Fcp_Create(domain_name,lun_interval):
    """ lets create an iSCSI domain """

    host1 = api.hosts.list()[0]
    storage_ = host1.storage.list()
    fcp_storage = params.Storage(type_='fcp',
            volume_group=params.VolumeGroup())
    SD = params.StorageDomain(name=domain_name,format='True',
            host=host1,type_='data',storage_format='v3')
    storage_len = len(storage_)
    Lun_list = list()
    for x in range (0,storage_len):
        try:
            if storage_[x].get_type() == None:
                Lun_list.append(storage_[x].get_logical_unit()[0])
            if storage_[x].get_type() == 'nfs':
                raise Exception('nfs?')
            if storage_[x].get_type() == 'glusterfs':
                raise Exception('gluster?')
        except Exception,e:
            print "caught", e
            continue
    try:
        if len(Lun_list) == 0:
            raise Exception('operation stopped, no Fc Luns')
    except Exception,e:
        print e
        return
    else:
        fcp_storage.set_logical_unit(Lun_list[lun_interval[0]:
            lun_interval[1]])
    SD.set_storage(fcp_storage)
    try:
        NewSd = api.storagedomains.add(SD)
    except Exception,e:
        print "A problem caught during creating the domain --->",e
        return
    api.datacenters.list()[0].storagedomains.add(NewSd)
if __name__ == "__main__":
        Fcp_Create("Fcp_Domain_1",[5,7])

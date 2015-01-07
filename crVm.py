#!/usr/bin/python
from ovirtsdk.api import API
from ovirtsdk.xml import params
import time
def checkit(self):
    """	Build a connection string from a dictionary of parameters.Returns string."""

    u = 'https://10.35.161.36/ovirt-engine/api'
    user = 'admin@internal'
    password = 'qum5net'
    api = API(url=u, password=password, username=user, insecure=True)
    sd_iscsi=api.storagedomains.list()[0]
    print sd_iscsi.get_name()
    vm_str="vm__"
    for i in range(10):
        vm_str="vm_"
        vm_str+=str(i)
        param=params.VM(name=vm_str,cluster=api.clusters.list()[0],template=api.templates.get(name='Blank'))
        api.vms.add(param)
        b=params.Disk(storage_domains=params.StorageDomains(storage_domain=[sd_iscsi]),size=3368709119,type_='data',interface='virtio',format='cow')
        vm=api.vms.get(name=vm_str)
        vm.disks.add(b)
        #tmp_str="template_"
        #tmp_str+=str(i)
        #time.sleep(15)
        #api.templates.add(params.Template(name=tmp_str,vm=vm))
if __name__ == "__main__":
    checkit("name")

#!/usr/bin/python
from ovirtsdk.api import API
from ovirtsdk.xml import params
from sdk_connect import Connect
import sys
api = Connect()

def checkDisksGrowth(self):
    """	Build a connection string from a dictionary of parameters.Returns string."""

    iso = api.storagedomains.get('rhevm-3-iso-lion')
    file = iso.files.get('RHEL-7-SERVER-dvd1.iso')
    for SD in api.storagedomains.list():
        print SD.get_name()
        vm_str = "vm_"
        vm_str +=SD.get_name()
        network = params.Network(name='rhevm') 
        nic = params.NIC(name='eth0',network=network,interface='e1000')
        os = params.OperatingSystem(boot=[params.Boot(dev='cdrom'),])
        param=params.VM(name=vm_str,cluster=api.clusters.list()[0],
                template=api.templates.get(name='Blank'),os=os)
        api.vms.add(param)
        a = params.Disk(storage_domains=params.StorageDomains(storage_domain=[SD]),
            size=7368709119,type_='data',interface='virtio',format='cow')
        vm=api.vms.get(name=vm_str)
        cd = vm.get_cdroms().list()[0]
        cd.set_file(file)
        cd.update()
        vm.nics.add(nic)
        try:
            V = vm.disks.add(a)
            print V
        except Exception,e:
            print e
    #tmp_str="template_"
    #tmp_str+=str(i)
    #time.sleep(15)
    #api.templates.add(params.Template(name=tmp_str,vm=vm))
if __name__ == "__main__":
    print sys.argv
    checkDisksGrowth("name")

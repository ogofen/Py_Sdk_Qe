#!/usr/bin/python
from ovirtsdk.api import API
from ovirtsdk.xml import params
from sdk_connect import Connect
import sys
import time
api = Connect()

def checkDisksGrowth(self):
    """	Build a connection string from a dictionary of parameters.Returns string."""

    for SD in api.storagedomains.list():
        counter=0
        print SD.get_name()
        if SD.get_type() != 'data':
            print SD.get_type()
            continue
        vm_header = "CobblerVM_"
        vm_name = vm_header+str(counter)
        while api.vms.get(vm_name) is not None:
            counter +=1
            vm_name = vm_header+str(counter)
        vm_tmp_name = vm_name+'tmp'
        network = params.Network(name='rhevm') 
        nic = params.NIC(name='eth0',network=network,interface='virtio')
        admin_vm_manager_perm = params.Permission(api.roles.get('UserVmManager'),user=api.users.get('admin'))
        kernel = 'iso://RHEL-7-x86_64-vmlinuz' 
        initrd = 'iso://RHEL-7-x86_64-initrd.img'
        kspath = 'https://www.dropbox.com/s/6hbd36lzxeue7bt/ks.cfg?dl=0'
        cmdline = 'dhcpclass=ipa-lab-vms ks=https://www.dropbox.com/s/6hbd36lzxeue7bt/ks.cfg?dl=0 loglevel=debug network kssendmac noverifyssl poweroff'
        os = params.OperatingSystem(kernel=kernel,initrd=initrd,cmdline=cmdline)
        param=params.VM(name=vm_tmp_name,cluster=api.clusters.list()[0],os=os,
                template=api.templates.get(name='Blank'))
        api.vms.add(param)
        param=params.VM(name=vm_name,cluster=api.clusters.list()[0],
                template=api.templates.get(name='Blank'))
        vm = api.vms.add(param)
        vm.nics.add(nic)
        a = params.Disk(storage_domains=params.StorageDomains(storage_domain=[SD]),
            size=7368709119,type_='data',interface='virtio',format='cow',bootable='True')
        vm = api.vms.get(name=vm_tmp_name)
       #i vm.permissions.add(admin_vm_manager_perm)
        vm.nics.add(nic)
        try:
            V = vm.disks.add(a)
        except Exception,e:
            print e
        time.sleep(13)
        vm.start()
        time.sleep(90)
        vm=api.vms.get(name=vm_tmp_name)
        while vm.get_status().get_state() != 'down':
            vm=api.vms.get(name=vm_tmp_name)
            time.sleep(1)
        detach = params.Action()
        detach.set_detach('True')
        d = vm.disks.list()[0]
        d.deactivate()
        time.sleep(7)
        d.delete(detach)
        time.sleep(5)
        vm.delete()
        vm = api.vms.get(name=vm_name)
        vm.disks.add(api.disks.get(d.get_name()))
        time.sleep(5)
        vm.disks.list()[0].activate()
        time.sleep(5)
        vm.start()
        return

    #tmp_str="template_"
    #tmp_str+=str(i)
    #time.sleep(15)
    #api.templates.add(params.Template(name=tmp_str,vm=vm))
if __name__ == "__main__":
    print sys.argv
    checkDisksGrowth("name")

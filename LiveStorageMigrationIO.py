#!/usr/bin/python
from ovirtsdk.api import API
from ovirtsdk.xml import params
from sdk_connect import Connect
import sys
import time
api = Connect()

def LiveStorageMigrationTest():
    """	Build a connection string from a dictionary of parameters.Returns string."""

    for SD in api.storagedomains.list():
        counter=0
        print SD.get_name()
        if SD.get_type() != 'data':
            print SD.get_type()
            continue
        vm_header = "LiveStorageMigrateVM_"
        vm_name = vm_header+str(counter)
        while api.vms.get(vm_name) is not None:
            counter +=1
            vm_name = vm_header+str(counter)
        network = params.Network(name='rhevm') 
        nic = params.NIC(name='eth0',network=network,interface='virtio')
        admin_vm_manager_perm = params.Permission(api.roles.get('UserVmManager'),user=api.users.get('admin'))
        kernel = 'iso://RHEL-7-x86_64-vmlinuz' 
        initrd = 'iso://RHEL-7-x86_64-initrd.img'
        kspath = 'https://www.dropbox.com/s/6hbd36lzxeue7bt/ks.cfg?dl=0'
        cmdline = 'ks=https://www.dropbox.com/s/6hbd36lzxeue7bt/ks.cfg?dl=0 loglevel=debug network kssendmac noverifyssl poweroff'
        os = params.OperatingSystem(kernel=kernel,initrd=initrd,cmdline=cmdline)
        param=params.VM(name=vm_name,cluster=api.clusters.list()[0],os=os,
                template=api.templates.get(name='Blank'))
        api.vms.add(param)
        a = params.Disk(storage_domains=params.StorageDomains(storage_domain=[SD]),
            size=7368709119,type_='data',interface='virtio',format='cow',bootable='True')
        vm = api.vms.get(name=vm_name)
        vm.nics.add(nic)
       #i vm.permissions.add(admin_vm_manager_perm)
        try:
            V = vm.disks.add(a)
        except Exception,e:
            print e
        time.sleep(13)
        vm.start()
        time.sleep(100)
        vm=api.vms.get(name=vm_name)
        for SD_target in api.storagedomains.list():
            print SD_target.get_name()
            if SD.get_name() != SD_target.get_name() and SD_target.get_storage().get_type() == SD.get_storage().get_type():
                print SD_target.get_name()
                a = params.Action()
                a.set_storage_domain(SD_target)
                vm.disks.list()[0].move(a)
                return
            continue
        while vm.get_status().get_state() != 'down':
            vm=api.vms.get(name=vm_name)
            time.sleep(1)
        os = vm.get_os()
        os.set_kernel('')
        os.set_cmdline('')
        os.set_initrd('')
        vm.update()
        time.sleep(7)
        vm.start()
        return

    #tmp_str="template_"
    #tmp_str+=str(i)
    #time.sleep(15)
    #api.templates.add(params.Template(name=tmp_str,vm=vm))
if __name__ == "__main__":
    LiveStorageMigrationTest()

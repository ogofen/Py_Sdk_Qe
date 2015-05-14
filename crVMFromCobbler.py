#!/usr/bin/python
from ovirtsdk.xml import params
from sdk_connect import connect
from IsoDomain import iso_create
import time
import sys
import pudb

def create_vm(api):
    """	Build a connection string from a dictionary of parameters.Returns
    string."""

    if api.domains.get('Iso_Domain'):
        print "haha"
        iso_create('/RHEV/ogofen/iso-domain-ogofen', '10.35.160.108')
    for SD in api.storagedomains.list():
        counter = 0
        print SD.get_name()
        if SD.get_type() != 'data':
            print SD.get_type()
            continue
        sd = SD
        break
    vm_header = "CobblerVM_"
    vm_name = vm_header + str(counter)
    while api.vms.get(vm_name) is not None:
        counter += 1
        vm_name = vm_header + str(counter)
    network = params.Network(name=api.networks.list()[0].get_name())
    nic = params.NIC(name='eth0', network=network, interface='virtio')
    kernel = 'iso://RHEL-7-x86_64-vmlinuz'
    initrd = 'iso://RHEL-7-x86_64-initrd.img'
    cmdline = "ks=https://www.dropbox.com/s/6hbd36lzxeue7bt/ks.cfg?dl=0"\
            "loglevel=debug network kssendmac noverifyssl poweroff"
    os = params.OperatingSystem(kernel=kernel, initrd=initrd,
                                cmdline=cmdline)
    param = params.VM(name=vm_name, cluster=api.clusters.list()[0], os=os,
                      template=api.templates.get(name='Blank'))
    api.vms.add(param)
    a = params.Disk(storage_domains=params.StorageDomains(storage_domain=[sd]),
                    size=7368709117, type_='data', interface='virtio',
                    format='cow', bootable='True')
    vm = api.vms.get(name=vm_name)
    vm.nics.add(nic)
# 'ivm.permissions.add(admin_vm_manager_perm)'
    try:
        vm.disks.add(a)
    except Exception, e:
        print e
    time.sleep(13)
    vm.start()
    time.sleep(90)
    vm = api.vms.get(name=vm_name)
    while vm.get_status().get_state() != 'down':
        vm = api.vms.get(name=vm_name)
        time.sleep(1)
    os = vm.get_os()
    os.set_kernel('')
    os.set_cmdline('')
    os.set_initrd('')
    vm.update()
    time.sleep(7)
    vm.start()
    return 0

    # tmp_str="template_"
    # tmp_str+=str(i)
    # time.sleep(15)
    # api.templates.add(params.Template(name=tmp_str,vm=vm))

if __name__ == "__main__":
    api = connect()
    create_vm(api)
    sys.exit(0)

from ovirtsdk.api import API
from ovirtsdk.xml import params
import time
def checkit(self):
    """	Build a connection string from a dictionary of parameters.Returns string."""

    u = 'https://10.35.161.37/api'
    user = 'admin@internal'
    password = '123456'
    api = API(url=u, password=password, username=user, insecure=True)
    sd_nfs = api.storagedomains.list()[1]
    sd_iscsi=api.storagedomains.list()[0]
    print sd_nfs.get_name()
    print sd_iscsi.get_name()
    vm_str="vm_"
    for i in range(11):
        vm_str="vm_"
        vm_str+=str(i)
        param=params.VM(name=vm_str,cluster=api.clusters.get(name='Default'),template=api.templates.get(name='Blank'))
        api.vms.add(param)
        a=params.Disk(storage_domains=params.StorageDomains(storage_domain=[sd_nfs]),size=3368709120,type_='data',interface='virtio',format='raw')
        b=params.Disk(storage_domains=params.StorageDomains(storage_domain=[sd_iscsi]),size=3368709119,type_='data',interface='virtio',format='raw')
        vm=api.vms.get(name=vm_str)
        vm.disks.add(a)
        vm.disks.add(b)
        #tmp_str="template_"
        #tmp_str+=str(i)
        #time.sleep(15)
        #api.templates.add(params.Template(name=tmp_str,vm=vm))
if __name__ == "__main__":
    checkit("name")

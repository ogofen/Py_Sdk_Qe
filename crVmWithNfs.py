from ovirtsdk.api import API
from ovirtsdk.xml import params

from sdk_connect import connect
api = connect()

def checkit(self):
    """	Build a connection string from a dictionary of parameters.Returns string."""

    sd_nfs = api.storagedomains.list()[0]
    print sd_nfs.get_name()
    t=params.Template(name='Blank')
    for i in range(3):
        vm_str = "vm__"
        vm_str += str(i)
        param=params.VM(name=vm_str,cluster=api.clusters.list()[1],template=t)
        api.vms.add(param)
        a=params.Disk(storage_domains=params.StorageDomains(storage_domain=[sd_nfs]), size=3368709120,
                      type_='data', interface='virtio', format='cow')
        vm=api.vms.get(name=vm_str)
        vm.disks.add(a)
        #tmp_str="template_"
        #tmp_str+=str(i)
        #time.sleep(15)
        #api.templates.add(params.Template(name=tmp_str,vm=vm))
if __name__ == "__main__":
    checkit("name")

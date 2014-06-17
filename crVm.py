from ovirtsdk.api import API
from ovirtsdk.xml import params

def checkit(self):
    """	Build a connection string from a dictionary of parameters.Returns string."""

    u = 'https://10.35.163.66/api'
    user = 'admin@internal'
    password = 'qum5net'
    api = API(url=u, password=password, username=user, insecure=True)
    sd_nfs = api.storagedomains.list()[1]
    sd_iscsi=api.storagedomains.list()[0]
    print sd_nfs.get_name()
    sd_iscsi.get_name()
    for i in range(11):
        param=params.VM(name=str(i),cluster=api.clusters.get(name='Default'),template=api.templates.get(name='Blank'))
        api.vms.add(param)
        a=params.Disk(storage_domains=params.StorageDomains(storage_domain=[sd_nfs]),size=3368709120,type_='data',interface='virtio',format='raw')
        b=params.Disk(storage_domains=params.StorageDomains(storage_domain=[sd_iscsi]),size=3368709119,type_='data',interface='virtio',format='cow')
        vm=api.vms.get(name=str(i))
        vm.disks.add(a)
        vm.disks.add(b)

if __name__ == "__main__":
    checkit("name")

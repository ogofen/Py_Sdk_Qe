
from ovirtsdk.api import API
from ovirtsdk.xml import params
import time
u = 'https://10.35.161.36/ovirt-engine/api'
user = 'admin@internal'
password = 'qum5net'
api = API(url=u, password=password, username=user, insecure=True)
storage_nfs = params.StorageDomain(type_='data',storage=params.Storage(type_='nfs',address='10.35.160.108',path='/RHEV/ogofen/1'),host=params.Host(name=api.hosts.list()[0].get_name()))
api.storagedomains.add(storage_nfs)


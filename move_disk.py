api.disks.list()[0]
# OUT: <ovirtsdk.infrastructure.brokers.Disk object at 0x19f2c90>
a = api.disks.list()[0]
[a.get_name() for a in api.storagedomains.list()]
# OUT: ['ISO_DOMAIN', 'nfs_1', 'nfs_2', 'ovirt-image-repository']
[a.get_name(), a.get_id() for a in api.storagedomains.list()]
# OUT:   File "<input>", line 1
# OUT:     [a.get_name(), a.get_id() for a in api.storagedomains.list()]
# OUT:                                 ^
# OUT: SyntaxError: invalid syntax
[(a.get_name(), a.get_id()) for a in api.storagedomains.list()]
# OUT: [('ISO_DOMAIN', '2df95da3-3be3-4470-b2e9-535efc84f855'), ('nfs_1', '86e9c373-bf9b-42c2-8bb3-4f6e506525e9'), ('nfs_2', 'bdc50f25-cec2-4ee7-a120-4ff2d74094b4'), ('ovirt-image-repository', '072fbaa1-08f3-4a40-9f34-a5ca22dd1d74')]
a = api.disks.list()[0]
a.get_storage_domains()[0]
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: 'StorageDomains' object does not support indexing
a.get_storage_domains()
# OUT: <ovirtsdk.xml.params.StorageDomains object at 0x1e39c90>
x = a.get_storage_domains()
x.get_storage_domain()
# OUT: [<ovirtsdk.xml.params.StorageDomain object at 0x1e39cd0>]
x.get_storage_domain()[0].get_id()
# OUT: '86e9c373-bf9b-42c2-8bb3-4f6e506525e9'
sd = api.storagedomains.get(name='nfs_2')
action = params.Action()
action.set_storage_domain(sd)
a.move(action=action)
# OUT: <ovirtsdk.xml.params.Action object at 0x1e3ea10>

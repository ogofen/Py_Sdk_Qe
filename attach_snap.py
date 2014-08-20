import ovirtsdk.api
import ovirtsdk.xml
from ovirtsdk.xml import params
import logging

api = ovirtsdk.api.API(
    url="https://10.35.161.36/api",
    username="admin@internal",
    password="qum5net",
    insecure=True,
    debug=False
)
logging.basicConfig()
log = logging.getLogger()

# Find the snapshot that contains the disk that we want to backup:
vm = api.vms.get("vm_snapshot")
snaps = vm.snapshots.list(all_content=True)
snap = None
configuration_data = None
for current in snaps:
    if current.get_description() == "ds":
        snap = current
        configuration_data = current.get_initialization().get_configuration().get_data()
        log.error(configuration_data)
        break

# Find the disk of that we want to backup:
disks = snap.disks.list()
disk = disks[0]


#newVm = params.VM(name="new", cluster=api.clusters.get(name='Default'))
#newVm.initialization = params.Initialization()
#newVm.initialization.configuration = params.Configuration()
#newVm.initialization.configuration.set_type("ovf")
#newVm.initialization.configuration.set_data(configuration_data)
#my_vm = api.vms.add(newVm)
# Find the backup appliance:
appliance = api.vms.get("ori")
print disk.get_name()
# Attach the disk to the backup appliance:
appliance.disks.add(disk)

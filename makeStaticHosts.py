__author__ = 'ogofen'

from ovirtsdk.xml import params
import time
from sdk_connect import connect
api = connect()


def make_vms_static():
    """	make all VM's network a static one"""

    for host in api.hosts.list():
        print host.get_name()
        host.deactivate()
        while host.get_status().get_state() != 'maintenance':
            host = host.update()
            time.sleep(1)
            print host.get_status().get_state()
        time.sleep(10)
        for nic in host.nics.list():
            if nic.get_status().get_state() == 'up':
                print nic.get_name()
                nic.set_boot_protocol('static')
                nic.update()
                print "done"
        host.commitnetconfig(params.Action())
        time.sleep(10)
        host.activate()


if __name__ == "__main__":
    make_vms_static()
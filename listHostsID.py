yu__author__ = 'ogofen'
from sdk_connect import connect

api = connect()


def listhostsid():
    """ list all VM's and their ips """

    for host in api.hosts.list():
        print "host %s id is -> %s" %(host.get_name(),host.get_id())


if __name__ == "__main__":
        listhostsid()
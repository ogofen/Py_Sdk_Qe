from ovirtsdk.api import API


def connect(*args):
    """ This Function connects To our engine,classes and db
    """
    udict = ['', 'https://ovirt-gofen-1.scl.lab.tlv.redhat.com/api',
             'https://ovirt-gofen-2.scl.lab.tlv.redhat.com/api',
             'http://localhost:8080/api']
    u = input("enter setup number:")
    url = udict[u]
    user = 'admin@internal'
    password = 'qum5net'
    if len(args) > 0:
        return API(url=url, password=password, username=user, insecure=True, debug=True)
    return API(url=url, password=password, username=user, insecure=True)

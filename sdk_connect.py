from ovirtsdk.api import API
from ovirtsdk.xml import params

def Connect():
    """ This Function connects To our engine,classes and db
    """
    u = 'https://ovirt-gofen-1.scl.lab.tlv.redhat.com/api'
    insecure=True
    user = 'admin@internal'
    password = 'qum5net'
    return API(url=u, password=password, username=user, insecure=True)

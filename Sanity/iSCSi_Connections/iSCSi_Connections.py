import re
from ovirtsdk.api import API
from ovirtsdk.xml import params

def Connect():
    """ This Function connects To our engine,classes and db
    """
    u = 'https://10.35.161.36/api'
    insecure=True
    user = 'admin@internal'
    password = 'qum5net'
    return API(url=u, password=password, username=user, insecure=True)

def get_Engine_ListofLuns(lun_list):
    """ Gets dict name lun_dict, and return it,initialized with logical
    unit object that correspond with host's address (which is a string)
    """
    api = Connect()
    for Host in api.hosts.list():
        lun_list[Host.get_address()]=list()
        for Storage in Host.storage.list():
            lun_list[Host.get_address()].append(Storage.get_logical_unit())

def get_HostIqnList(iqn):
    """ Gets an empty list and returns it full with hosts
    iqn strings
    """

    with open('/root/Sanity/sessions.log','r') as f:
        while True:
            line = f.readline()
            if line == '':
                break
            elif re.search('flash', re.split(' ',line)[-1], flags = 1) != None:
                iqn.append(re.split(' ',line)[-2])
                continue
            iqn.append(re.split(' ',line)[-1])
            iqn[-1] = iqn[-1].rsplit()

if __name__ == "__main__":
    iqn=list()
    get_HostIqnList(iqn)
    print len(iqn)
    print iqn
#    get_IqnList(iqn)
#    print iqn

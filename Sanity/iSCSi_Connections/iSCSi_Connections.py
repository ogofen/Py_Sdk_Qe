import re
import os
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

def get_HostIqnList(host_name):
    """ Gets an empty list and returns it full with hosts
    iqn strings
    """

    iqn = list()
    with open('/root/Sanity/%s' %host_name,'r') as f:
        while True:
            line = f.readline()
            if line == '':
                break
            elif re.search('flash', re.split(' ',line)[-1], flags = 1) != None:
                iqn.append(re.split(' ',line)[-2])
                continue
            iqn.append(re.split(' ',line)[-1])
            iqn[-1] = iqn[-1].rsplit()
    return iqn

def get_HostsNames(api,names):
    """ Gets oVirt's api and an empty list and returns it full with hosts names
    """

    HOSTSList = api.hosts.list()
    for HOSTS in HOSTSList:
        print HOSTS.get_name()
        names.append(HOSTS.get_name())

if __name__ == "__main__":
    api = Connect()
    names=list()
    get_HostsNames(api,names)
    for n in names:
        os.system("./check-iSCSiConnections %s" % n)
        iq = get_HostIqnList(n)
        print iq
#    print len(iqn)
#    print iqn
#    get_IqnList(iqn)
#    print iqn

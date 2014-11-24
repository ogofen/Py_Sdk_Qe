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

class iSCSiConnections():
    ''' class to check iSCSi connections
    '''


    def __init__(self):
        self.api = Connect()
        self.storageconnections = list()
        self.hostsIqn = dict()
        self.hostsIp = list()

    def get_HostIqnList(self,host_address):
        """ Gets an empty list and returns it full with hosts
        iqn strings
        """
        os.system("./session.ini %s" % host_address)
        iqn = list()
        with open('/tmp/%s' %host_address,'r') as f:
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

    def start(self):
        """ Gets dict name lun_dict, and return it,initialized with logical
        unit object that correspond with host's address (which is a string)
        """
        for Host in self.api.hosts.list():
            self.hostsIp.append(Host.get_address())
            self.hostsIqn[Host.get_address()] = list()
            self.hostsIqn[Host.get_address()] = self.get_HostIqnList(Host.get_address())
        for Storage in self.api.storagedomains.get("iSCSi_1").storageconnections.list():
            self.storageconnections.append(Storage.get_target())

    def compareHosts(self):
        for i in range(0,len(self.hostsIp)-1):
            for j in range(1,len(self.hostsIp) -i):
                flag = cmp(self.hostsIqn[self.hostsIp[i]],self.hostsIqn[self.hostsIp[i+j]])
                if flag == 1:
                    return len(self.hostsIqn[self.hostsIp[i]]) == len(self.hostsIqn[self.hostsIp[i+j]])
                else:
                    return flag

 #   def compareHostsTodb(self):

if __name__ == "__main__":
    connection = iSCSiConnections()
    connection.start()
    print connection.compareHosts()
#    print len(iqn)
#    print iqn
#    get_IqnList(iqn)
#    print iqn

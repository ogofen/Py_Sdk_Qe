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

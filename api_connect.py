from ovirtsdk.api import API
from ovirtsdk.xml import params
u = 'https://10.35.161.37/api'
user = 'admin@internal'
password = 'qum5net'
api = API(url=u, password=password, username=user, insecure=True)

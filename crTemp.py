from ovirtsdk.api import API
from ovirtsdk.xml import params

def checkit(self):
    """	Build a connection string from a dictionary of parameters.Returns string."""

    u = 'https://10.35.161.36/ovirt-engine/api'
    user = 'admin@internal'
    password = 'qum5net'
    api = API(url=u, password=password, username=user, insecure=True)
    sd_nfs = api.storagedomains.list()[1]
    sd_iscsi=api.storagedomains.list()[0]
    print sd_nfs.get_name()
    print sd_iscsi.get_name()
    for i in range(10):
        tmp_str="template_"
        tmp_str+=str(i)
        api.templates.add(params.Template(name=tmp_str,vm=api.vms.list()[i]))
if __name__ == "__main__":
    checkit("name")

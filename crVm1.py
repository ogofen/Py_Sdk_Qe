bfrom ovirtsdk.api import API
from ovirtsdk.xml import params

def checkit(self):
    """	Build a connection string from a dictionary of parameters.Returns string."""

    u = 'https://10.35.161.37/api'
    user = 'admin@internal'
    password = 'qum5net'
    api = API(url=u, password=password, username=user, insecure=True)
    sd_nfs = api.storagedomains.list()[1]
    sd_iscsi=api.storagedomains.list()[0]
    print sd_nfs.get_name()
    print sd_iscsi.get_name()
    vm_str="vm_"
    for i in range(11):
        tmp_str="template_"
        tmp_str+=str(i)
        vm=api.vms.get(name=tmp_str)
        temp_par=params.Template(name=tmp_str,vm=vm)
        api.templates.add(temp_par)
if __name__ == "__main__":
    checkit("name")

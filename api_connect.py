from ovirtsdk.api import API
from ovirtsdk.xml import params
import sdk_connect
import sys

if len(sys.argv) > 1:
    if sys.argv[1] == "debug":
        api = sdk_connect.connect(True)
else:
    api = sdk_connect.connect()

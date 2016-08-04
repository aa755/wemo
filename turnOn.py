from miranda import upnp
conn = upnp()
resp = conn.sendSOAP('wemo:49153', 'urn:Belkin:service:basicevent:1', 
     'http://wemo:49153/upnp/control/basicevent1', 
     'SetBinaryState', {'BinaryState': (1, 'Boolean')})
print resp

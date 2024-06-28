from jinja2.nativetypes import NativeEnvironment
import group
import json


fname = 'etcd-csr.json'
env = NativeEnvironment()
f = open(fname+'.j2', 'r')
c = f.read()
t = env.from_string(c)
result = t.render(groups=group.groups)
c = result
if type(result)==dict:
    c = json.dumps(result)
with open(fname, "w") as fh:
    fh.write(c)

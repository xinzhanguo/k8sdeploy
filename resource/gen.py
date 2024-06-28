from jinja2.nativetypes import NativeEnvironment
import group
import json
import sys
import yaml

def gen(fname: str, afile: str):
    prime_service = {}
    if afile!="":
        with open(afile, 'r') as af:
            prime_service = yaml.safe_load(af)
    env = NativeEnvironment()
    f = open(fname+'.j2', 'r')
    c = f.read()
    t = env.from_string(c, globals=prime_service)
    result = t.render(groups=group.groups)
    c = result
    if type(result)==dict:
        c = json.dumps(result)
    with open(fname, "w") as fh:
        fh.write(c)

def main():
    if len(sys.argv)==2:
        gen(sys.argv[1], "")
    if len(sys.argv)==3:
        gen(sys.argv[1], sys.argv[2])


main()
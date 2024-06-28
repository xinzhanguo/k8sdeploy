from jinja2.nativetypes import NativeEnvironment
import group
import json
import sys


def gen(fname: str):
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

def main():
    if len(sys.argv)>=2:
        gen(sys.argv[1])

main()

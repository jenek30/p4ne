import re
from ipaddress import IPv4Interface
import glob


def classify(s):


    m = re.match("^ ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", s)
    if m:
        return {"ip":IPv4Interface(str(m.group(1)) + "/" + str(m.group(2)))}


    return ("NONE",)

ips = set()

for fname in glob.glob("e:/обучение/lab/*.log"):
    with open(fname) as f:
        for current_line in f:
            c = classify(current_line)
            if "ip" in c:
                ips.add(c)


print(ips)


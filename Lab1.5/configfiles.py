import glob

ips = set()
for fname in glob.glob("e:/обучение/lab/*.log"):
    with open(fname) as f:
        for cur_line in f:
            cur_line = cur_line.lstrip()
            if "ip address" in cur_line:

                cur_line = cur_line.replace("ip address", "").rstrip().rstrip("sub").lstrip("no").lstrip("guest")

                ips.add(cur_line)

for ip in ips:
    print(ip.lstrip())





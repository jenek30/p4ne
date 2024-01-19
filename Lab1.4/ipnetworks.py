import ipaddress
import random


net1 = ipaddress.IPv4Network((random.randint(0x0b000000, 0xdf000000),random.randint(8, 24)), strict=False)


class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self, p_start=0, p_end=32):
        ipaddress.IPv4Network.__init__(self,
                             (random.randint(0x0B000000, 0xDF000000),
                              random.randint(p_start, p_end)),
                             strict=False
                             )

    def regular(self):
        if self.is_global and not (self.is_link_local or self.is_loopback or self.is_multicast or self.is_private or self.is_reserved or self.is_unspecified):
            return True
        return False

    def key_value(self):
        return int(self.netmask) * 2 ** 32 + int(self.network_address)

networks = set()
while len(networks) < 50:
    net = IPv4RandomNetwork(8,24)
    if net.regular():
        networks.add(net)

for net in sorted(networks, key=IPv4RandomNetwork.key_value):
    print(net)
print("Количество сетей для испоьзования", + len(networks))
import ipaddress

# ipv4 = ipaddress.ip_address('192.168.0.1')
# print(dir(ipv4))
"""
['_ALL_ONES', '__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', 
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
'__slots__', '__str__', '__sub__', '__subclasshook__', '__weakref__', '_check_int_address', '_check_packed_address', 
'_constants', '_explode_shorthand_ip_string', '_get_address_key', '_ip', '_ip_int_from_prefix', '_ip_int_from_string', 
'_make_netmask', '_max_prefixlen', '_netmask_cache', '_parse_octet', '_prefix_from_ip_int', '_prefix_from_ip_string', 
'_prefix_from_prefix_string', '_report_invalid_netmask', '_reverse_pointer', '_split_addr_prefix', 
'_string_from_ip_int', '_version', 'compressed', 'exploded', 'is_global', 'is_link_local', 'is_loopback', 
'is_multicast', 'is_private', 'is_reserved', 'is_unspecified', 'max_prefixlen', 'packed', 'reverse_pointer', 'version']
"""

# print(ipv4.is_loopback)  # False
# print(ipv4.is_multicast)  # False
# print(ipv4.is_reserved)  # False
# print(ipv4.is_private)  # True
#
#
# ip1 = ipaddress.ip_address('192.168.1.0')
# ip2 = ipaddress.ip_address('192.168.1.255')
#
# if ip1 > ip2:
#     print(True)
#
# print(str(ip1))  # 192.168.1.0
# print(int(ip1))  # 3232235776
# print(ip1 + 5)  # 192.168.1.5
# print(ip1 - 5)  # 192.168.0.251


subnet = ipaddress.ip_network('80.0.1.0/28')
ba = subnet.broadcast_address
print(ba)  # 80.0.1.15

print('list hosts', list(subnet.hosts()))
# [IPv4Address('80.0.1.1'), IPv4Address('80.0.1.2'), IPv4Address('80.0.1.3'), IPv4Address('80.0.1.4'),
# IPv4Address('80.0.1.5'), IPv4Address('80.0.1.6'), IPv4Address('80.0.1.7'), IPv4Address('80.0.1.8'),
# IPv4Address('80.0.1.9'), IPv4Address('80.0.1.10'), IPv4Address('80.0.1.11'), IPv4Address('80.0.1.12'),
# IPv4Address('80.0.1.13'), IPv4Address('80.0.1.14')]

print('list subnets', list(subnet.subnets()))  # [IPv4Network('80.0.1.0/29'), IPv4Network('80.0.1.8/29')]

print('subnet[1]', subnet[1])  # 80.0.1.1

ipv4_int = ipaddress.ip_interface('10.0.1.1/24')
print('ip', ipv4_int.ip)  # ip 10.0.1.1
print('netmask', ipv4_int.netmask)  # netmask 255.255.255.0
print('network', ipv4_int.network)  # network 10.0.1.0/24



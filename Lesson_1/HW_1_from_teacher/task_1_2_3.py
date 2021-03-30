import subprocess
from tabulate import tabulate


def host_ping(addr) -> bool:
    # return subprocess.call(["ping", "-c", "1", str(addr)]) == 0
    # response will be
    """
    PING google.com (172.217.23.238): 56 data bytes
    64 bytes from 172.217.23.238: icmp_seq=0 ttl=116 time=5.995 ms

    --- google.com ping statistics ---
    1 packets transmitted, 1 packets received, 0.0% packet loss
    round-trip min/avg/max/stddev = 5.995/5.995/5.995/0.000 ms
    """

    return subprocess.call(["ping", "-c", "1", str(addr)], stdout=subprocess.DEVNULL) == 0
    # response will be
    # Process finished with exit code 0

    # return subprocess.call("ping", "-n", "1") == 0  # for Windows


# print('res is : ', host_ping('google.com'))  # res is :  True

#  =============================================


def host_range_ping(addresses):
    res = {}
    for addr in addresses:
        res[addr] = host_ping(addr)
    return res


# print(host_range_ping(['google.com', 'yahoo.com', 'foo.bar']))  # {'google.com': True, 'yahoo.com': True, 'foo.bar': False}

#  =============================================


def print_host_table(ping_results):
    columns = ['Host', 'Status']
    table_data = {
        (k, 'Reachable' if v else 'Unreachable') for k, v in ping_results.items()
    }
    return tabulate(table_data, headers=columns)


if __name__ == '__main__':
    res = host_range_ping(['google.com', 'yahoo.com', 'foo.com'])
    table = print_host_table(res)
    print(table)
"""
Host        Status
----------  -----------
foo.com     Unreachable
yahoo.com   Reachable
google.com  Reachable
"""

"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
"""

import os
import ipaddress
import subprocess
import platform
FILE_NAME = 'host_ping_result.txt'


def host_ping(ip_list):
    columns = ['Available host', 'Not available host']
    common_list = []
    for ip in ip_list:
        if platform.system() == 'Darwin':
            # create an ip address from the given list of IPs
            # address = ipaddress.ip_address(ip)
            # args = ['ping', '-i', '1', '-c', '2', address]  # если использовать ipaddress для перевода в IP адресс, то возникает ошибка TypeError: expected str, bytes or os.PathLike object, not IPv4Address. Как ее обойти?
            args = ['ping', '-i', '1', '-c', '2', ip]
            ping_proc = subprocess.Popen(args, stdout=subprocess.PIPE)
            # get a statistic about the pinging
            out = str(ping_proc.communicate()[0].decode("utf-8"))
            # here we print the statistic about the pinging
            print(out)
            # check the return code, if it's 0, the the service is UP, else is DOWN
            if ping_proc.returncode == 0:
                with open(FILE_NAME, 'w+', encoding='utf-8') as file:
                    file.write(f'{ip} - Available \n')
                print(f'The host "{ip}" is UP \n')
            else:
                with open(FILE_NAME, 'w+', encoding='utf-8') as file:
                    file.write(f'{ip} - Not Available \n')
                print(f'The host "{ip}" is DOWN \n')
        else:
            print('The OS is not MacOS, it is not supported')



if __name__ == '__main__':
    ips_list = ['213.219.213.213', '89.208.84.144', '5.61.239.67']
    addresses_list = ['crm.geekbrains.space', 'ya.ru', 'google.com']
    host_ping(ips_list)

"""
Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2.
Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате
(использовать модуль tabulate). Таблица должна состоять из двух колонок
"""

import os
import ipaddress
import subprocess
import platform
from tabulate import tabulate

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
                common_list.append({'Available host': ip})
            else:
                with open(FILE_NAME, 'w+', encoding='utf-8') as file:
                    file.write(f'{ip} - Not Available \n')
                print(f'The host "{ip}" is DOWN \n')
                common_list.append({'Not available host': ip})
        else:
            print('The OS is not MacOS, it is not supported')
    print('The summary table about availability of hosts: ')
    print(tabulate(common_list, headers='keys', tablefmt="grid"))


def host_range_ping():
    while True:
        init_ip = input('Enter primary IP address to start scanning: ')
        splitted_oct = init_ip.split('.')
        last_oct = splitted_oct.pop()
        first_three_oct = ".".join(splitted_oct)
        number_addresses_range = (input('How many addresses should be scanned?: '))
        list_ip = []
        if number_addresses_range.isnumeric():
            if int(last_oct) + int(number_addresses_range) < 254:
                for x in range(int(number_addresses_range)):
                    list_ip.append(first_three_oct + '.' + str(x))
            else:
                print('Looks like the number of the last octet is higher than 254, try rerun again')
        else:
            print('You entered not a number')
        print(list_ip)
        break
    print('Please wait the result of checking of availability for defined hosts')
    host_ping(list_ip)


if __name__ == '__main__':
    ips_list = ['213.219.213.213', '89.208.84.144', '5.61.239.67']
    addresses_list = ['crm.geekbrains.space', 'ya.ru', 'google.com']
    host_ping(ips_list)


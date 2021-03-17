"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
"""

import ipaddress
from task_1 import host_ping

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
    host_range_ping()

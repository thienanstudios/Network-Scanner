import subprocess
import re


def scan_network():
    command = ['sudo', 'arp-scan', '-l', '-r', '5']
    new_list = []
    users_mac = []
    valid_manuf = []

    out = subprocess.check_output(command)
    regex_mac = re.compile(ur'(?:[0-9a-fA-F]:?){12}')
    mac_list = re.indall(regex_mac, out)

    split = out.splitlines()
    split = split[2:-3]

    for x in range(len(split)):
        num = split[x].rfind('\t')
        new_list.append(split[x][num + 1:])

    index = 0
    for x in new_list:
        if x in valud_manuf:
            users_mac.append(mac_list[index])
        index += 1

    return users_mac
    
def count():
    len(scan_network())


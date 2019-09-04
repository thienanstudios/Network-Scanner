# arp-scan -l -r 5

import subprocess
from subprocess import Popen, PIPE

List = []

command = ['arp-scan', '-l', 'r', '5']

p = subprocess.Popen(command)

text = p.stdout.read()
retcode = p.wait()

List.extend(text)

for i in range(len(List))
    print List[i]



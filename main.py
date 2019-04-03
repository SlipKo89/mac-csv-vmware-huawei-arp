import sys
import csv

print ("Read file arp.csv")
with open('/home/slipko/PycharmProjects/arp-vm/arp.csv') as arp:
    reader = csv.reader(arp,delimiter=';')
    arp_list = list(reader)

print ("Read file vm_mac.csv")
with open('/home/slipko/PycharmProjects/arp-vm/vm_mac.csv') as vm:
    reader = csv.reader(vm,delimiter=';')
    vm_list = list(reader)

a = len(arp_list)
print ("Lenght of arp.csv= " ,a)

b = len(vm_list)
print ("Lenght of vm.csv= " ,b)

# Reformat vm_list mac address
i = 0
while i < b:
    g = vm_list[i][1].split(":")
    str='{0}''{1}'"-"'{2}''{3}'"-"'{4}''{5}'.format(g[0],g[1],g[2],g[3],g[4],g[5])
    vm_list[i][1]=str
    #print (vm_list[i][1],vm_list[i][0])
    i = i + 1

# Find eq in 2 lists
i = 0
hop = 0

while i < a:
    n = 0
    while n < b:
        if arp_list[i][1] == vm_list[n][1]:
            print (arp_list[i][0],arp_list[i][1],vm_list[n][0],vm_list[n][1])
            hop = hop + 1
        n = n + 1
    i = i + 1
#    i = i + 1
#
print (hop)


interfaces=['Ethernet0/0            unassigned      YES unset  up                    up      ', 'Ethernet0/1            unassigned      YES unset  up                    up      ', 'Ethernet0/2            unassigned      YES unset  up                    up      ', 'Ethernet0/3            unassigned      YES unset  up                    up      ', 'Vlan1                  192.168.1.3     YES NVRAM  up                    up']

interfaces=[item.split()[0] for item in interfaces ]

print(interfaces)

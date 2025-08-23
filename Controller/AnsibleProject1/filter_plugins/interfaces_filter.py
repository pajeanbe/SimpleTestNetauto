import re

def find_unused_interfaces_on_cisco_nodes(data):
    unused_interfaces = []
    current_interface = None
    buffer = []

    for line in data:
        # Detect interface line
        if re.match(r'^\s*(Ethernet|FastEthernet|GigabitEthernet|TenGigabitEthernet|Vlan)\d+(/\d+)*', line):
            if current_interface and buffer:
                if is_unused(buffer):
                    unused_interfaces.append(current_interface)
            current_interface = line.strip()
            buffer = []
        else:
            buffer.append(line.strip())

    # Check last interface
    if current_interface and buffer:
        if is_unused(buffer):
            unused_interfaces.append(current_interface)

    return unused_interfaces

def is_unused(lines):
    for line in lines:
        if line.startswith("Total"):
            # Extract packet counts
            numbers = re.findall(r'\d+', line)
            if len(numbers) >= 4:
                pkts_in, pkts_out = int(numbers[0]), int(numbers[2])
                return min(pkts_in,pkts_out)==0
    return False

class FilterModule(object):
    def filters(self):
        return {
            'find_unused_interfaces_on_cisco_nodes': find_unused_interfaces_on_cisco_nodes
        }



"""
# Example usage
data = [
    "Ethernet0/0",
    "          Switching path    Pkts In   Chars In   Pkts Out  Chars Out",
    "               Processor      15164    2010806      66427    7033162",
    "             Route cache          0          0          0          0",
    "                   Total      15164    2010806      66427    7033162",
    "Ethernet0/1",
    "          Switching path    Pkts In   Chars In   Pkts Out  Chars Out",
    "               Processor          0          0      48120    3557499",
    "             Route cache          0          0          0          0",
    "                   Total          0          0      48120    3557499",
    "Ethernet0/2",
    "          Switching path    Pkts In   Chars In   Pkts Out  Chars Out",
    "               Processor          0          0      48119    3557059",
    "             Route cache          0          0          0          0",
    "                   Total          0          0      48119    3557059",
    "Ethernet0/3",
    "          Switching path    Pkts In   Chars In   Pkts Out  Chars Out",
    "               Processor          0          0      48114    3559000",
    "             Route cache          0          0          0          0",
    "                   Total          0          0      48114    3559000",
    "Vlan1",
    "          Switching path    Pkts In   Chars In   Pkts Out  Chars Out",
    "               Processor      12302     847713      18493    3489683",
    "             Route cache          0          0          0          0",
    "                   Total      12302     847713      18493    3489683"
]

unused = find_unused_interfaces(data)
print("Unused interfaces:", unused)

"""
def get_unused_interfaces(interface_data):
    """
    Parses 'show interfaces' output and returns a list of interfaces
    with 0 input and 0 output packets.
    """
    unused = []
    for block in interface_data.split('\n\n'):
        lines = block.strip().splitlines()
        if not lines:
            continue
        name_line = lines[0]
        ifname = name_line.split()[0]
        input_line = next((l for l in lines if 'packets input' in l), '')
        output_line = next((l for l in lines if 'packets output' in l), '')
        if 'packets input 0' in input_line and 'packets output 0' in output_line:
            unused.append(ifname)
    return unused

class FilterModule(object):
    def filters(self):
        return {
            'get_unused_interfaces': get_unused_interfaces
        }
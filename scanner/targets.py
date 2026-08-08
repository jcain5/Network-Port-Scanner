import ipaddress


def expand_targets(target: str) -> list[str]:
    if "/" in target:
        network = ipaddress.ip_network(target)
        if network.version == 4:
             usable_hosts = max(network.num_addresses - 2 , 0)
             if usable_hosts > 256:
                 raise ValueError("Network contains more than 256 usable hosts")

        return [str(address) for address in network.hosts()]

    
    address = ipaddress.ip_address(target)
    return [str(address)]
expand_targets("192.168.0.2")
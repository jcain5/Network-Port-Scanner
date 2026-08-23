import ipaddress


def expand_targets(target: str) -> list[str]:
    if "/" in target:
        network = ipaddress.ip_network(target)

        hosts = list(network.hosts())

        if len(hosts) > 256:
            raise ValueError("Network contains more than 256 usable hosts")

        return [str(address) for address in network.hosts()]

    address = ipaddress.ip_address(target)
    return [str(address)]

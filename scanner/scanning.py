import socket
from datetime import datetime


def scan_port(address: str, port: int, timeout: float = 1.0) -> str:
    try:
        with socket.create_connection((address, port), timeout=timeout):
            return "OPEN"
    except ConnectionRefusedError:
        return "CLOSED"
    except socket.timeout:
        return "TIMEOUT"
    except OSError:
        return "UNREACHABLE"


def scan_host(target: str, services: dict[int, str], timeout: float = 1.0) -> list[dict]:
    results = []
    scan_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for port, service in services.items():
        status = scan_port(target, port, timeout)

        results.append({
            "timestamp": scan_time,
            "target": target,
            "port": port,
            "service": service,
            "status": status,
        })

        print(f"[{status}] {target}: {port} ({service})")
    return results
import socket
import struct
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


def scan_host(target: str, services: dict[int, str], timeout: float = 1.0, protocol: str = "tcp") -> list[dict]:
    results = []
    scan_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for port, service in services.items():
        if protocol == "udp":
            status = scan_udp_port(target, port, timeout)
        else:
            status = scan_port(target, port, timeout)

        results.append({
            "timestamp": scan_time,
            "target": target,
            "port": port,
            "service": service,
            "status": status,
        })

    return results

def scan_udp_port(
        target: str,
        port: int,
        timeout: float = 1.0,
) -> str:
    with socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM,
    ) as sock:
        sock.settimeout(timeout)

        try:
            sock.sendto(
                b"",
                (target, port),
            )

            data, address = sock.recvfrom(1024)

            return "OPEN"

        except socket.timeout:
            return "OPEN|FILTERED"

        except ConnectionRefusedError:
            return "CLOSED"

        except OSError as error:
            return "UNREACHABLE"


def encode_dns_name(domain: str) -> bytes:
    encoded = b""

    for label in domain.split("."):
        encoded += bytes([len(label)])
        encoded += label.encode("ascii")

    encoded += b"\x00"

    return encoded

def build_dns_query(domain: str)-> bytes:
    transaction_id = 0x1234
    flags = 0x0100
    question_count = 1
    answer_count = 0
    authority_count = 0
    additional_count = 0

    header = struct.pack(
        "!HHHHHH",
        transaction_id,
        flags,
        question_count,
        answer_count,
        authority_count,
        additional_count,
    )
    question_name = encode_dns_name(domain)

    question_tail = struct.pack(
            "!HH",
            1,
                1,
    )

    return header + question_name + question_tail

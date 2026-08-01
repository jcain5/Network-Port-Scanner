import ipaddress
import socket
import time
import csv
from datetime import datetime


def validate_ip(address: str) -> bool:
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False


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


def save_results(
    results: list[dict],
    filename: str = "scan_results.csv",
    mode: str = "a",
) -> None:
    fieldnames = ["timestamp", "target", "port", "service", "status"]

    with open(filename, mode, newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        if mode == "w" or csv_file.tell() == 0:
            writer.writeheader()

        writer.writerows(results)


def main() -> None:
    services = {
        21: "FTP",
        22: "SSH",
        23: "TELNET",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        135: "MS-RPC",
        139: "NETBIOS-SSN",
        143: "IMAP",
        389: "LDAP",
        443: "HTTPS",
        445: "SMB",
        465: "SMTPS",
        587: "SMTP-SUBMISSION",
        636: "LDAPS",
        993: "IMAPS",
        995: "POP3S",
        1433: "MSSQL",
        2049: "NFS",
        3306: "MYSQL",
        3389: "RDP",
        5432: "POSTGRESQL",
        5900: "VNC",
        5985: "WINRM-HTTP",
        5986: "WINRM-HTTPS",
        8006: "PROXMOX",
        8080: "HTTP-ALT",
        8443: "HTTPS-ALT",
    }

    target = input("Target IP: ").strip()

    if not validate_ip(target):
        print("Invalid IP Address")
        return

    print(f"\nScanning Target: {target}")
    print("-" * 40)

    start_time = time.perf_counter()
    results = scan_host(target, services)

    elapsed_time = time.perf_counter() - start_time
    print(f"\nScan completed in {elapsed_time:.2f} seconds.")

    save_mode = input("Append to existing CSV? (Y/N): ").strip().lower()
    mode = "a" if save_mode == "y" else "w"

    save_results(results, mode=mode)
    print("Results saved to scan_results.csv")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScan cancelled by user.")

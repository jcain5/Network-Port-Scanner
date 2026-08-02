import argparse
import time

from scanner.validation import validate_ip
from scanner.scanning import scan_host
from scanner.services import SERVICES
from scanner.reporting import save_results

def positive_timeout(value: str) -> float:
    try:
        timeout = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(
            "Timeout must be a number"
        )

    if timeout <= 0:
        raise argparse.ArgumentTypeError(
            "Timeout must be greater than 0."
        )
    if timeout > 60:
        raise argparse.ArgumentTypeError(
            "Timeout must be 60 seconds or less"
        )

    return timeout

def parse_ports(value: str) -> list[int]:
    ports = []

    for item in value.split(","):
        item =item.strip()

        try:
            port = int(item)
        except ValueError:
            raise argparse.ArgumentTypeError(
                f"Invalid port: {item}"
            )
        if not 1<=port<=65535:
            raise argparse.ArgumentTypeError(
                f"Port must be between 1 and 65535: {port}"
            )

        ports.append(port)
    return ports


def parse_arguments(
        arguments: list[str] | None = None,
) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scan common TCP ports on an authorized target."
    )

    parser.add_argument(
        "--target",
        required=True,
        help="IPv4 or IPv6 address to scan.",
    )
    parser.add_argument(
        "--timeout",
        type=positive_timeout,
        default=1.0,
        help="Connection timeout in seconds greater than 0 and up to 60",
    )
    parser.add_argument(
        "--ports",
        type=parse_ports,
        help="Comma separated TCP ports, for example: 22,80,443",
    )
    parser.add_argument(
        "--output",
        default="scan_results.csv",
        help="CSV output file name (default: scan_results.csv)",
    )

    file_mode_group = parser.add_mutually_exclusive_group()

    file_mode_group.add_argument(
        "--append",
        dest="file_mode",
        action="store_const",
        const="a",
        help="Append results to the output CSV",
    )
    file_mode_group.add_argument(
        "--overwrite",
        dest="file_mode",
        action="store_const",
        const="w",
        help="Overwrite the output CSV",
    )
    parser.set_defaults(file_mode="a")

    return parser.parse_args(arguments)


def main() -> None:
    args = parse_arguments()
    target = args.target.strip()
    services = SERVICES

    if args.ports:
        services = {
            port: SERVICES.get(port, "UNKNOWN")
            for port in args.ports
        }

    if not validate_ip(target):
        print("Invalid IP Address")
        return

    print(f"\nScanning Target: {target}")
    print("-" * 40)

    start_time = time.perf_counter()
    results = scan_host(target, services, timeout=args.timeout)

    elapsed_time = time.perf_counter() - start_time
    print(f"\nScan completed in {elapsed_time:.2f} seconds.")

    save_results(
        results,
        filename=args.output,
        mode=args.file_mode,
    )

    print(f"Results saved to {args.output}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScan cancelled by user.")

import argparse
import time
from concurrent.futures import ThreadPoolExecutor

from scanner.scanning import scan_host
from scanner.services import SERVICES
from scanner.reporting import save_results
from scanner.targets import expand_targets

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


def positive_workers(value: str) -> int:
    try:
        workers = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(
            "Workers must be an integer"
        )
    if workers < 1:
        raise argparse.ArgumentTypeError(
            "Workers must be at least 1"
        )
    if workers > 32:
        raise argparse.ArgumentTypeError(
            "Workers must be 32 or less"
        )

    return workers


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
    parser.add_argument(
        "--workers",
        type=positive_workers,
        default=8,
        help="Number of concurrent host workers(default: 8)",
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
    targets = expand_targets(args.target.strip())
    services = SERVICES

    if args.ports:
        services = {
            port: SERVICES.get(port, "UNKNOWN")
            for port in args.ports
        }

    all_results = []
    start_time = time.perf_counter()

    with ThreadPoolExecutor(max_workers = args.workers) as executor:
        futures = []

        for target in targets:
            print(f"\nScanning target: {target}")
            print("-" * 40)

            future = executor.submit(
                scan_host,
                target,
                services,
                timeout = args.timeout
            )

            futures.append(future)
        for future in futures:
            all_results.extend(future.result())

    elapsed_time = time.perf_counter() - start_time
    print(f"\nScanning completed in {elapsed_time:.2f} seconds.")

    save_results(
        all_results,
        filename = args.output,
         mode = args.file_mode,
    )

    print(f"Results saved to {args.output}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScan cancelled by user.")

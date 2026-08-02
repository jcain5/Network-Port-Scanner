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



def parse_arguments() -> argparse.Namespace:
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
        help="Connection timeout in seconds from 0 to 60 (default: 1.0)",
    )

    return parser.parse_args()


def main() -> None:
    

    args = parse_arguments()
    target = args.target.strip()

    if not validate_ip(target):
        print("Invalid IP Address")
        return

    print(f"\nScanning Target: {target}")
    print("-" * 40)

    start_time = time.perf_counter()
    results = scan_host(target, SERVICES, timeout=args.timeout)

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

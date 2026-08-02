import time

from scanner.validation import validate_ip
from scanner.scanning import scan_host
from scanner.services import SERVICES
from scanner.reporting import save_results

def main() -> None:
    

    target = input("Target IP: ").strip()

    if not validate_ip(target):
        print("Invalid IP Address")
        return

    print(f"\nScanning Target: {target}")
    print("-" * 40)

    start_time = time.perf_counter()
    results = scan_host(target, SERVICES)

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

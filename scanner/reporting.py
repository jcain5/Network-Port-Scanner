import csv

def save_results(
    results: list[dict],
    filename: str = "scan_results.csv",
    mode: str = "a",
) -> None:
    if mode not in ("a", "w"):
        raise ValueError("Mode must be 'a' or 'w'.")

    fieldnames = ["timestamp", "target", "port", "service", "status"]

    with open(filename, mode, newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        if mode == "w" or csv_file.tell() == 0:
            writer.writeheader()

        writer.writerows(results)

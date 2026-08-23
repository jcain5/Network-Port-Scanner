Network Port Scanner

A modular Python TCP port scanner built as a hands-on networking, security, and software engineering portfolio project.

The scanner supports single-host and authorized CIDR network scanning, common or user-selected TCP ports, service mapping, connection-status classification, configurable concurrent host scanning, and CSV reporting.

Use this project only on systems and networks you own or have explicit authorization to test.

Project Status

Phase 3 Complete: Concurrent Multi-Host Lab Scanner

The project has progressed from a single-file learning script into a tested, modular command-line application capable of scanning individual hosts or authorized IPv4 CIDR ranges with scope controls and configurable concurrency.

Completed Capabilities

IPv4 and IPv6 address validation

Single-host TCP scanning

IPv4 CIDR target expansion

Authorized multi-host subnet scanning

Maximum scope of 256 usable hosts per CIDR scan

Common service identification

OPEN, CLOSED, TIMEOUT, and UNREACHABLE handling

Configurable connection timeout

Custom comma-separated TCP port selection

Configurable concurrent host workers

Worker validation from 1 through 32

Ordered post-scan terminal output

Scan duration measurement

CSV report generation

Append and overwrite report modes

Custom output filenames

Modular scanner package

Automated unit and integration-style tests

Mocked socket and multi-host tests

Command-line parser tests

Sanitized documentation examples

Standard-library-only implementation

Project Structure

Network-Port-Scanner/
├── main.py
├── scanner/
│   ├── __init__.py
│   ├── reporting.py
│   ├── scanning.py
│   ├── services.py
│   ├── targets.py
│   └── validation.py
├── tests/
│   ├── test_arguments.py
│   ├── test_main.py
│   ├── test_scanning.py
│   ├── test_targets.py
│   └── test_validation.py
├── .gitignore
├── LICENSE
└── README.md

Requirements

Python 3.10 or newer

No third-party packages required

Installation

git clone https://github.com/jcain5/Network-Port-Scanner.git
cd Network-Port-Scanner

Optional virtual environment:

Windows PowerShell

py -m venv .venv
.\.venv\Scripts\Activate.ps1

macOS or Linux

python3 -m venv .venv
source .venv/bin/activate

Usage

Help

py main.py --help

Scan a single host

py main.py --target 192.0.2.10

Scan selected ports

py main.py --target 192.0.2.10 --ports 22,80,443

Use a custom timeout

py main.py --target 192.0.2.10 --timeout 0.5

Scan an authorized CIDR range

py main.py --target 192.0.2.0/28 --ports 53,80,443

Configure host workers

py main.py --target 192.0.2.0/28 --ports 53,80,443 --timeout 0.5 --workers 8

Overwrite a report

py main.py --target 192.0.2.10 --ports 22,80,443 --output sample_scan.csv --overwrite

Append to a report

py main.py --target 192.0.2.10 --ports 22,80,443 --output sample_scan.csv --append

The addresses 192.0.2.0/24, 198.51.100.0/24, and 203.0.113.0/24 are reserved for documentation and examples.

Command-Line Options

--target TARGET

Required IPv4 address, IPv6 address, or supported IPv4 CIDR range.

--timeout TIMEOUT

Connection timeout in seconds.

Greater than 0

Maximum 60 seconds

Default: 1.0

--ports PORTS

Comma-separated TCP ports. Each port must be between 1 and 65535.

--output OUTPUT

CSV output filename.

Default: scan_results.csv

--workers WORKERS

Concurrent host workers.

Minimum: 1

Maximum: 32

Default: 8

--append

Append scan results to the output CSV.

--overwrite

Replace the output CSV with the latest scan.

--append and --overwrite are mutually exclusive.

Example Output

Scanning target: 192.0.2.1
----------------------------------------

Scanning target: 192.0.2.2
----------------------------------------
[TIMEOUT] 192.0.2.1: 53 (DNS)
[OPEN] 192.0.2.1: 80 (HTTP)
[TIMEOUT] 192.0.2.1: 443 (HTTPS)
[TIMEOUT] 192.0.2.2: 53 (DNS)
[TIMEOUT] 192.0.2.2: 80 (HTTP)
[TIMEOUT] 192.0.2.2: 443 (HTTPS)

Scanning completed in 1.53 seconds.
Results saved to scan_results.csv

Scan Statuses

Status

Meaning

OPEN

A TCP connection was successfully established

CLOSED

The target actively refused the connection

TIMEOUT

The target did not respond before the timeout expired

UNREACHABLE

The host or network could not be reached

A timeout does not prove that a port is open or closed. It may indicate firewall filtering, packet loss, routing problems, or a non-responsive host.

CIDR Scope Controls

CIDR scanning is intentionally constrained for responsible lab use.

The scanner:

Expands supported IPv4 CIDR ranges into usable host addresses

Handles /31 and /32 networks

Rejects CIDR ranges containing more than 256 usable hosts

Concurrency

Phase 3 introduced host-level concurrency using Python's ThreadPoolExecutor.

Each worker scans one host while that host's selected ports are checked sequentially. Worker count is controlled with --workers.

Worker results are collected before they are printed, keeping terminal output ordered rather than allowing multiple threads to print simultaneously.

Performance Evidence

Measured during authorized local-lab testing:

Scenario

Scan Time

/28, sequential baseline

21.30 s

/28, 4 workers

6.17 s

/28, 8 workers

3.04 s

/24, 32 workers

12.31 s

The /28 tests used 14 usable hosts, three TCP ports per host, and a 0.5 second timeout.

The /24 test exercised 254 usable hosts and three TCP ports per host with 32 workers.

CSV Output

Default output:

scan_results.csv

Example:

timestamp,target,port,service,status
2026-08-23 18:00:00,192.0.2.1,53,DNS,TIMEOUT
2026-08-23 18:00:00,192.0.2.1,80,HTTP,OPEN
2026-08-23 18:00:00,192.0.2.1,443,HTTPS,TIMEOUT

Real scan results should not be committed to a public repository. Local scan reports such as scan_results.csv and *_scan.csv should remain excluded by .gitignore.

Running Tests

Windows

py -m unittest discover -v

macOS or Linux

python3 -m unittest discover -v

Current result:

Ran 45 tests

OK

Some parser tests intentionally print command-line errors before the final OK. Those tests verify invalid argument combinations are rejected.

Test Coverage

The automated suite covers:

IPv4 and IPv6 validation

Invalid address handling

Single-target expansion

IPv4 CIDR expansion

/31 and /32 handling

CIDR host-limit enforcement

OPEN, CLOSED, TIMEOUT, and UNREACHABLE

Mocked socket behavior

Timeout validation

Port-list validation

Worker-count validation

Required CLI arguments

Default and custom worker values

Append/overwrite conflicts

Multi-host scan submission

Combined multi-host results

Thread-pool worker configuration

Learning Objectives

This project demonstrates practical experience with:

Python functions and type hints

Modules and packages

TCP sockets

Exception handling

ipaddress

argparse

CSV file handling

unittest

Dependency mocking

Input validation

ThreadPoolExecutor

Concurrent host-level workloads

Performance measurement

Scope controls

Git and GitHub workflows

Responsible security-tool development

Development Roadmap

Phase 1: Core Scanner

Completed:

Single-host TCP scanning

Common service mapping

Status handling

CSV output

Basic documentation

Phase 2: Modular Command-Line Application

Completed:

Package refactor

Automated tests

--target

--timeout

--ports

--output

--append

--overwrite

Parser-level tests

Non-interactive execution

Phase 3: Multi-Host Lab Scanning

Completed:

CIDR input

Authorized subnet iteration

Multi-host result collection

Scope controls

Concurrent host scanning

Configurable worker count

Worker-count validation

Ordered post-scan output

Performance measurement

Expanded automated testing

Phase 4: Data Visualization and Reporting

Planned:

Scan summaries

Host and service summaries

Summary charts

Host-to-service visualizations

Historical scan comparisons

Baseline deviation displays

Dashboard-style reporting

Phase 5: AI-Assisted Interpretation

Planned:

Plain-English scan summaries

Baseline deviation analysis

Unusual service-pattern detection

Host role comparisons

Risk and attention scoring

AI-assisted report explanations

The AI layer will interpret scanner data rather than replace the scanner's deterministic network logic.

Ethical Use

This project is intended for:

Personal home labs

Authorized training environments

Systems owned by the operator

Networks where explicit testing permission has been granted

Do not use this scanner against public systems, third-party networks, or infrastructure without authorization.

Limitations

This project performs TCP connect scans against individual hosts or authorized IPv4 CIDR ranges within its scope limit.

It does not currently include:

UDP scanning

Operating-system detection

Service-version detection

Vulnerability exploitation

Stealth scanning

Authentication testing

Internet-wide scanning

ICMP or ARP host discovery

Vulnerability scoring

This is an educational and defensive lab tool, not a replacement for mature tools such as Nmap.

License

This project is licensed under the MIT License. See LICENSE for details.

Author

Jeremy Cain

Portfolio: https://www.jeremymcain.com
GitHub: https://github.com/jcain5
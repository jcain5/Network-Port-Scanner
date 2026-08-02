Network Port Scanner

A modular Python TCP port scanner built as a hands-on networking, security, and software engineering portfolio project.

The scanner validates a target IP address, checks selected TCP ports, identifies common services, records scan results, and supports command-line options for repeatable lab use.

Use this project only on systems and networks you own or have explicit authorization to test.

Project Status

Phase 2: Command-Line Interface and Testing

Current progress: approximately 85% complete

Completed

IPv4 and IPv6 address validation

TCP connection scanning

Common service identification

OPEN, CLOSED, TIMEOUT, and UNREACHABLE status handling

Scan duration measurement

CSV report generation

Append and overwrite report modes

Modular scanner package structure

Command-line target selection

Configurable connection timeout

Timeout validation

Custom comma-separated port selection

Port number validation

Automated unit tests

Mocked socket tests

Sanitized portfolio examples

GitHub-ready project structure

Remaining for Phase 2

Replace the interactive CSV prompt with command-line options

Add command-line output filename support

Add overwrite or append flags

Add parser-level tests

Finalize CLI documentation

Features

Validates IPv4 and IPv6 addresses before scanning

Scans a built-in list of common TCP services

Accepts custom TCP port lists

Supports configurable connection timeouts

Maps known ports to service names

Labels unrecognized ports as UNKNOWN

Displays results in the terminal

Saves results to CSV

Handles Ctrl+C cleanly

Uses Python's built-in testing framework

Project Structure

Network-Port-Scanner/
├── main.py
├── scanner/
│   ├── __init__.py
│   ├── reporting.py
│   ├── scanning.py
│   ├── services.py
│   └── validation.py
├── tests/
│   ├── test_arguments.py
│   ├── test_scanning.py
│   └── test_validation.py
├── .gitignore
├── LICENSE
└── README.md

Requirements

Python 3.10 or newer

No third-party packages required

Installation

Clone the repository:

git clone https://github.com/jcain5/Network-Port-Scanner.git
cd Network-Port-Scanner

Optional virtual environment:

Windows PowerShell

python -m venv .venv
.\.venv\Scripts\Activate.ps1

macOS or Linux

python3 -m venv .venv
source .venv/bin/activate

Usage

Display help:

python main.py --help

Scan the built-in service list:

python main.py --target 192.0.2.10

Set a custom timeout:

python main.py --target 192.0.2.10 --timeout 0.5

Scan selected ports:

python main.py --target 192.0.2.10 --ports 22,80,443

Combine custom ports and timeout:

python main.py --target 192.0.2.10 --ports 22,53,80,443 --timeout 0.5

Command-Line Options

--target TARGET
    Required target IPv4 or IPv6 address.

--timeout TIMEOUT
    Optional connection timeout in seconds.
    Must be greater than 0 and no more than 60.
    Default: 1.0

--ports PORTS
    Optional comma-separated list of TCP ports.
    Each port must be between 1 and 65535.

Example Output

Scanning Target: 192.0.2.10
----------------------------------------
[TIMEOUT] 192.0.2.10: 22 (SSH)
[OPEN] 192.0.2.10: 80 (HTTP)
[TIMEOUT] 192.0.2.10: 443 (HTTPS)

Scan completed in 1.04 seconds.

CSV Output

The scanner stores results in scan_results.csv.

timestamp,target,port,service,status
2026-08-01T22:45:00,192.0.2.10,22,SSH,TIMEOUT
2026-08-01T22:45:01,192.0.2.10,80,HTTP,OPEN
2026-08-01T22:45:01,192.0.2.10,443,HTTPS,TIMEOUT

Real scan results should not be committed to a public repository. Keep scan_results.csv in .gitignore.

Running Tests

Run the full test suite from the project root:

python -m unittest discover -s tests

Current expected result:

Ran 20 tests

OK

The exact count may increase as the project grows.

Test Coverage

The suite checks:

Valid and invalid IP addresses

OPEN, CLOSED, TIMEOUT, and UNREACHABLE scan outcomes

Valid integer and decimal timeouts

Zero, negative, excessive, and non-numeric timeouts

Valid custom port lists

Port lists containing spaces

Single-port input

Non-numeric ports

Ports below and above the valid range

Socket behavior is mocked where appropriate so unit tests do not depend on live services.

Learning Objectives

This project demonstrates:

Python functions and type hints

Modules and packages

TCP sockets

Exception handling

IP address validation

Command-line interfaces with argparse

CSV file handling

Unit testing with unittest

Dependency mocking

Git and GitHub workflows

Responsible security-tool development

Roadmap

Phase 1: Core Scanner

Single-host TCP scanning

Service mapping

Status handling

CSV output

Basic documentation

Phase 2: Modular CLI

Package refactor

Automated tests

--target

--timeout

--ports

Non-interactive report options

Expanded CLI documentation

Phase 3: Multi-Host Lab Scanning

Planned:

CIDR input

Authorized subnet iteration

Multi-host reporting

Summary statistics

Improved scan performance

Scope controls

Phase 4: Portfolio Polish

Planned:

Structured logging

Additional report formats

Improved terminal formatting

Expanded test coverage

Architecture diagram

Release tagging

Ethical Use

This project is intended for:

Personal home labs

Authorized training environments

Systems owned by the operator

Networks where explicit testing permission has been granted

Do not use this scanner against public systems, third-party networks, or infrastructure without authorization.

License

Licensed under the MIT License. See LICENSE for details.

Author

Jeremy Cain

Portfolio: https://www.jeremymcain.com

GitHub: https://github.com/jcain5
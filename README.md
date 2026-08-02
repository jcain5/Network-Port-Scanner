# Network Port Scanner

A modular Python TCP port scanner built as a hands-on networking, security, and software engineering portfolio project.

The scanner validates a target IP address, scans common or user-selected TCP ports, identifies services, classifies connection results, and saves reports to CSV through a command-line interface.

> Use this project only on systems and networks you own or have explicit authorization to test.

## Project Status

**Phase 2 Complete: Modular Command-Line Scanner**

The project has progressed from a single-file learning script into a tested, modular command-line application.

### Completed

- IPv4 and IPv6 address validation
- TCP connection scanning
- Common service identification
- OPEN, CLOSED, TIMEOUT, and UNREACHABLE status handling
- Scan duration measurement
- CSV report generation
- Append and overwrite report modes
- Custom output filenames
- Modular `scanner` package structure
- Command-line target selection
- Configurable connection timeout
- Timeout validation
- Custom comma-separated port selection
- Port number validation
- Mutually exclusive append and overwrite flags
- Automated unit tests
- Mocked socket tests
- Command-line parser tests
- Sanitized documentation examples
- GitHub-ready project structure

## Features

- Validates IPv4 and IPv6 addresses before scanning
- Scans a built-in list of common TCP services
- Accepts custom TCP port lists
- Supports configurable connection timeouts
- Maps known ports to service names
- Labels unrecognized ports as `UNKNOWN`
- Displays scan results in the terminal
- Saves results to a configurable CSV file
- Supports append and overwrite modes
- Rejects conflicting command-line options
- Handles Ctrl+C cleanly
- Uses only Python standard-library modules

## Project Structure

```text
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

Creating a virtual environment is optional but recommended.

Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
macOS or Linux
python3 -m venv .venv
source .venv/bin/activate
Usage

Display the help menu:

python3 main.py --help

On Windows, use:

python main.py --help
Scan the built-in common service list
python3 main.py --target 192.0.2.10
Set a custom timeout
python3 main.py \
  --target 192.0.2.10 \
  --timeout 0.5
Scan selected ports
python3 main.py \
  --target 192.0.2.10 \
  --ports 22,80,443
Combine custom ports and timeout
python3 main.py \
  --target 192.0.2.10 \
  --ports 22,53,80,443 \
  --timeout 0.5
Save to a custom output file
python3 main.py \
  --target 192.0.2.10 \
  --ports 22,80,443 \
  --output sample_scan.csv
Overwrite an existing report
python3 main.py \
  --target 192.0.2.10 \
  --ports 22,80,443 \
  --output sample_scan.csv \
  --overwrite
Append to an existing report
python3 main.py \
  --target 192.0.2.10 \
  --ports 22,80,443 \
  --output sample_scan.csv \
  --append

The addresses 192.0.2.0/24, 198.51.100.0/24, and 203.0.113.0/24 are reserved for documentation and examples.

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

--output OUTPUT
    Optional CSV output filename.
    Default: scan_results.csv

--append
    Append scan results to the output file.

--overwrite
    Replace the output file with the latest scan.

The --append and --overwrite options are mutually exclusive. The application rejects commands that include both.

Example Output
Scanning Target: 192.0.2.10
----------------------------------------
[TIMEOUT] 192.0.2.10: 22 (SSH)
[OPEN] 192.0.2.10: 80 (HTTP)
[TIMEOUT] 192.0.2.10: 443 (HTTPS)

Scan completed in 1.04 seconds.
Results saved to sample_scan.csv
Scan Statuses

The scanner returns one of four statuses for each TCP port:

Status	Meaning
OPEN	A TCP connection was successfully established
CLOSED	The target actively refused the connection
TIMEOUT	The target did not respond before the timeout expired
UNREACHABLE	The host or network could not be reached

A timeout does not prove that a port is open or closed. It may indicate firewall filtering, packet loss, routing problems, or a non-responsive host.

CSV Output

The default output file is:

scan_results.csv

Example:

timestamp,target,port,service,status
2026-08-02 15:00:00,192.0.2.10,22,SSH,TIMEOUT
2026-08-02 15:00:01,192.0.2.10,80,HTTP,OPEN
2026-08-02 15:00:01,192.0.2.10,443,HTTPS,TIMEOUT

Real scan results should not be committed to a public repository. The project .gitignore excludes local scan reports such as:

scan_results.csv
*_scan.csv
Running Tests

Run the complete test suite from the project root:

python3 -m unittest discover -s tests

On Windows:

python -m unittest discover -s tests

Current result:

Ran 27 tests

OK

Some parser tests intentionally generate command-line error messages before the final OK. Those tests verify that invalid argument combinations are rejected correctly.

Test Coverage

The automated suite covers:

Address validation
Valid IPv4 addresses
Valid IPv6 addresses
Invalid addresses
Port scanning
OPEN results
CLOSED results
TIMEOUT results
UNREACHABLE results
Mocked socket behavior
Timeout validation
Valid integer timeouts
Valid decimal timeouts
Zero values
Negative values
Values above the maximum
Non-numeric values
Port-list validation
Valid port lists
Port lists containing spaces
Single-port input
Non-numeric ports
Ports below the valid range
Ports above the valid range
Command-line parsing
Required target handling
Default timeout
Default output filename
Default append mode
Custom timeout, port, output, and file-mode arguments
Conflicting append and overwrite flags
Missing required target
Learning Objectives

This project demonstrates practical experience with:

Python functions
Type hints
Modules and packages
TCP sockets
Exception handling
IP address validation
Command-line interfaces with argparse
CSV file handling
Unit testing with unittest
Dependency mocking
Input validation
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
Updated documentation
Phase 3: Multi-Host Lab Scanning

Planned:

CIDR input
Authorized subnet iteration
Multi-host reporting
Host and service summaries
Improved scan performance
Scope controls
Expanded testing
Phase 4: Data Visualization

Planned:

Scan summary charts
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

This project currently performs TCP connect scans against one target at a time.

It does not currently include:

UDP scanning
Operating-system detection
Service-version detection
Vulnerability exploitation
Stealth scanning
Authentication testing
Internet-wide scanning

This is an educational and defensive lab tool, not a replacement for mature tools such as Nmap.

License

This project is licensed under the MIT License. See LICENSE for details.

Author

Jeremy Cain

Portfolio: https://www.jeremymcain.com
GitHub: https://github.com/jcain5

After replacing the current README:

```bash
git add README.md
git commit -m "Update README for completed Phase 2"
git push
make the above info a downloaded readme.md

README.md 

README.md
Document

README.md
Network Port Scanner

A modular Python TCP port scanner built as a hands-on networking, security, and software engineering portfolio project.

The scanner validates a target IP address, scans common or user-selected TCP ports, identifies services, classifies connection results, and saves reports to CSV through a command-line interface.

Use this project only on systems and networks you own or have explicit authorization to test.

Project Status

Phase 2 Complete: Modular Command-Line Scanner

The project has progressed from a single-file learning script into a tested, modular command-line application.

Completed
IPv4 and IPv6 address validation
TCP connection scanning
Common service identification
OPEN, CLOSED, TIMEOUT, and UNREACHABLE status handling
Scan duration measurement
CSV report generation
Append and overwrite report modes
Custom output filenames
Modular scanner package structure
Command-line target selection
Configurable connection timeout
Timeout validation
Custom comma-separated port selection
Port number validation
Mutually exclusive append and overwrite flags
Automated unit tests
Mocked socket tests
Command-line parser tests
Sanitized documentation examples
GitHub-ready project structure
Features
Validates IPv4 and IPv6 addresses before scanning
Scans a built-in list of common TCP services
Accepts custom TCP port lists
Supports configurable connection timeouts
Maps known ports to service names
Labels unrecognized ports as UNKNOWN
Displays scan results in the terminal
Saves results to a configurable CSV file
Supports append and overwrite modes
Rejects conflicting command-line options
Handles Ctrl+C cleanly
Uses only Python standard-library modules
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

Creating a virtual environment is optional but recommended.

Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
macOS or Linux
python3 -m venv .venv
source .venv/bin/activate
Usage

Display the help menu:

python3 main.py --help

On Windows, use:

python main.py --help
Scan the built-in common service list
python3 main.py --target 192.0.2.10
Set a custom timeout
python3 main.py \
  --target 192.0.2.10 \
  --timeout 0.5
Scan selected ports
python3 main.py \
  --target 192.0.2.10 \
  --ports 22,80,443
Combine custom ports and timeout
python3 main.py \
  --target 192.0.2.10 \
  --ports 22,53,80,443 \
  --timeout 0.5
Save to a custom output file
python3 main.py \
  --target 192.0.2.10 \
  --ports 22,80,443 \
  --output sample_scan.csv
Overwrite an existing report
python3 main.py \
  --target 192.0.2.10 \
  --ports 22,80,443 \
  --output sample_scan.csv \
  --overwrite
Append to an existing report
python3 main.py \
  --target 192.0.2.10 \
  --ports 22,80,443 \
  --output sample_scan.csv \
  --append

The addresses 192.0.2.0/24, 198.51.100.0/24, and 203.0.113.0/24 are reserved for documentation and examples.

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

--output OUTPUT
    Optional CSV output filename.
    Default: scan_results.csv

--append
    Append scan results to the output file.

--overwrite
    Replace the output file with the latest scan.

The --append and --overwrite options are mutually exclusive. The application rejects commands that include both.

Example Output
Scanning Target: 192.0.2.10
----------------------------------------
[TIMEOUT] 192.0.2.10: 22 (SSH)
[OPEN] 192.0.2.10: 80 (HTTP)
[TIMEOUT] 192.0.2.10: 443 (HTTPS)

Scan completed in 1.04 seconds.
Results saved to sample_scan.csv
Scan Statuses

The scanner returns one of four statuses for each TCP port:

Status	Meaning
OPEN	A TCP connection was successfully established
CLOSED	The target actively refused the connection
TIMEOUT	The target did not respond before the timeout expired
UNREACHABLE	The host or network could not be reached

A timeout does not prove that a port is open or closed. It may indicate firewall filtering, packet loss, routing problems, or a non-responsive host.

CSV Output

The default output file is:

scan_results.csv

Example:

timestamp,target,port,service,status
2026-08-02 15:00:00,192.0.2.10,22,SSH,TIMEOUT
2026-08-02 15:00:01,192.0.2.10,80,HTTP,OPEN
2026-08-02 15:00:01,192.0.2.10,443,HTTPS,TIMEOUT

Real scan results should not be committed to a public repository. The project .gitignore excludes local scan reports such as:

scan_results.csv
*_scan.csv
Running Tests

Run the complete test suite from the project root:

python3 -m unittest discover -s tests

On Windows:

python -m unittest discover -s tests

Current result:

Ran 27 tests

OK

Some parser tests intentionally generate command-line error messages before the final OK. Those tests verify that invalid argument combinations are rejected correctly.

Test Coverage

The automated suite covers:

Address validation
Valid IPv4 addresses
Valid IPv6 addresses
Invalid addresses
Port scanning
OPEN results
CLOSED results
TIMEOUT results
UNREACHABLE results
Mocked socket behavior
Timeout validation
Valid integer timeouts
Valid decimal timeouts
Zero values
Negative values
Values above the maximum
Non-numeric values
Port-list validation
Valid port lists
Port lists containing spaces
Single-port input
Non-numeric ports
Ports below the valid range
Ports above the valid range
Command-line parsing
Required target handling
Default timeout
Default output filename
Default append mode
Custom timeout, port, output, and file-mode arguments
Conflicting append and overwrite flags
Missing required target
Learning Objectives

This project demonstrates practical experience with:

Python functions
Type hints
Modules and packages
TCP sockets
Exception handling
IP address validation
Command-line interfaces with argparse
CSV file handling
Unit testing with unittest
Dependency mocking
Input validation
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
Updated documentation
Phase 3: Multi-Host Lab Scanning

Planned:

CIDR input
Authorized subnet iteration
Multi-host reporting
Host and service summaries
Improved scan performance
Scope controls
Expanded testing
Phase 4: Data Visualization

Planned:

Scan summary charts
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

This project currently performs TCP connect scans against one target at a time.

It does not currently include:

UDP scanning
Operating-system detection
Service-version detection
Vulnerability exploitation
Stealth scanning
Authentication testing
Internet-wide scanning

This is an educational and defensive lab tool, not a replacement for mature tools such as Nmap.

License

This project is licensed under the MIT License. See LICENSE for details.

Author

Jeremy Cain

Portfolio: https://www.jeremymcain.com
GitHub: https://github.com/jcain5
README.md
Network Port Scanner

A modular Python TCP port scanner built as a hands-on networking, security, and software engineering portfolio project.

The scanner validates a target IP address, scans common or user-selected TCP ports, identifies services, classifies connection results, and saves reports to CSV through a command-line interface.

Use this project only on systems and networks you own or have explicit authorization to test.

Project Status

Phase 2 Complete: Modular Command-Line Scanner

The project has progressed from a single-file learning script into a tested, modular command-line application.

Completed
IPv4 and IPv6 address validation
TCP connection scanning
Common service identification
OPEN, CLOSED, TIMEOUT, and UNREACHABLE status handling
Scan duration measurement
CSV report generation
Append and overwrite report modes
Custom output filenames
Modular scanner package structure
Command-line target selection
Configurable connection timeout
Timeout validation
Custom comma-separated port selection
Port number validation
Mutually exclusive append and overwrite flags
Automated unit tests
Mocked socket tests
Command-line parser tests
Sanitized documentation examples
GitHub-ready project structure
Features
Validates IPv4 and IPv6 addresses before scanning
Scans a built-in list of common TCP services
Accepts custom TCP port lists
Supports configurable connection timeouts
Maps known ports to service names
Labels unrecognized ports as UNKNOWN
Displays scan results in the terminal
Saves results to a configurable CSV file
Supports append and overwrite modes
Rejects conflicting command-line options
Handles Ctrl+C cleanly
Uses only Python standard-library modules
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

Creating a virtual environment is optional but recommended.

Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
macOS or Linux
python3 -m venv .venv
source .venv/bin/activate
Usage

Display the help menu:

python3 main.py --help

On Windows, use:

python main.py --help
Scan the built-in common service list
python3 main.py --target 192.0.2.10
Set a custom timeout
python3 main.py \
  --target 192.0.2.10 \
  --timeout 0.5
Scan selected ports
python3 main.py \
  --target 192.0.2.10 \
  --ports 22,80,443
Combine custom ports and timeout
python3 main.py \
  --target 192.0.2.10 \
  --ports 22,53,80,443 \
  --timeout 0.5
Save to a custom output file
python3 main.py \
  --target 192.0.2.10 \
  --ports 22,80,443 \
  --output sample_scan.csv
Overwrite an existing report
python3 main.py \
  --target 192.0.2.10 \
  --ports 22,80,443 \
  --output sample_scan.csv \
  --overwrite
Append to an existing report
python3 main.py \
  --target 192.0.2.10 \
  --ports 22,80,443 \
  --output sample_scan.csv \
  --append

The addresses 192.0.2.0/24, 198.51.100.0/24, and 203.0.113.0/24 are reserved for documentation and examples.

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

--output OUTPUT
    Optional CSV output filename.
    Default: scan_results.csv

--append
    Append scan results to the output file.

--overwrite
    Replace the output file with the latest scan.

The --append and --overwrite options are mutually exclusive. The application rejects commands that include both.

Example Output
Scanning Target: 192.0.2.10
----------------------------------------
[TIMEOUT] 192.0.2.10: 22 (SSH)
[OPEN] 192.0.2.10: 80 (HTTP)
[TIMEOUT] 192.0.2.10: 443 (HTTPS)

Scan completed in 1.04 seconds.
Results saved to sample_scan.csv
Scan Statuses

The scanner returns one of four statuses for each TCP port:

Status	Meaning
OPEN	A TCP connection was successfully established
CLOSED	The target actively refused the connection
TIMEOUT	The target did not respond before the timeout expired
UNREACHABLE	The host or network could not be reached

A timeout does not prove that a port is open or closed. It may indicate firewall filtering, packet loss, routing problems, or a non-responsive host.

CSV Output

The default output file is:

scan_results.csv

Example:

timestamp,target,port,service,status
2026-08-02 15:00:00,192.0.2.10,22,SSH,TIMEOUT
2026-08-02 15:00:01,192.0.2.10,80,HTTP,OPEN
2026-08-02 15:00:01,192.0.2.10,443,HTTPS,TIMEOUT

Real scan results should not be committed to a public repository. The project .gitignore excludes local scan reports such as:

scan_results.csv
*_scan.csv
Running Tests

Run the complete test suite from the project root:

python3 -m unittest discover -s tests

On Windows:

python -m unittest discover -s tests

Current result:

Ran 27 tests

OK

Some parser tests intentionally generate command-line error messages before the final OK. Those tests verify that invalid argument combinations are rejected correctly.

Test Coverage

The automated suite covers:

Address validation
Valid IPv4 addresses
Valid IPv6 addresses
Invalid addresses
Port scanning
OPEN results
CLOSED results
TIMEOUT results
UNREACHABLE results
Mocked socket behavior
Timeout validation
Valid integer timeouts
Valid decimal timeouts
Zero values
Negative values
Values above the maximum
Non-numeric values
Port-list validation
Valid port lists
Port lists containing spaces
Single-port input
Non-numeric ports
Ports below the valid range
Ports above the valid range
Command-line parsing
Required target handling
Default timeout
Default output filename
Default append mode
Custom timeout, port, output, and file-mode arguments
Conflicting append and overwrite flags
Missing required target
Learning Objectives

This project demonstrates practical experience with:

Python functions
Type hints
Modules and packages
TCP sockets
Exception handling
IP address validation
Command-line interfaces with argparse
CSV file handling
Unit testing with unittest
Dependency mocking
Input validation
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
Updated documentation
Phase 3: Multi-Host Lab Scanning

Planned:

CIDR input
Authorized subnet iteration
Multi-host reporting
Host and service summaries
Improved scan performance
Scope controls
Expanded testing
Phase 4: Data Visualization

Planned:

Scan summary charts
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

This project currently performs TCP connect scans against one target at a time.

It does not currently include:

UDP scanning
Operating-system detection
Service-version detection
Vulnerability exploitation
Stealth scanning
Authentication testing
Internet-wide scanning

This is an educational and defensive lab tool, not a replacement for mature tools such as Nmap.

License

This project is licensed under the MIT License. See LICENSE for details.

Author

Jeremy Cain

Portfolio: https://www.jeremymcain.com
GitHub: https://github.com/jcain5
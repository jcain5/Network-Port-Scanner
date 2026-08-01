Python Network Port Scanner

A command-line TCP port scanner written in Python for scanning systems in an authorized infrastructure lab.

The scanner validates a target IP address, checks a configurable list of common TCP ports, maps ports to likely services, records scan duration, and exports timestamped results to CSV.

Features

Validates IPv4 and IPv6 addresses

Scans a configurable list of common TCP ports

Displays likely service names

Distinguishes between:

OPEN

CLOSED

TIMEOUT

UNREACHABLE

Measures total scan duration

Exports results to CSV

Supports append and overwrite modes

Handles Ctrl+C gracefully

Uses only Python standard-library modules

Example Output

Target IP: 203.0.113.10

Scanning Target: 203.0.113.10
----------------------------------------
[OPEN] 203.0.113.10:22 (SSH)
[OPEN] 203.0.113.10:53 (DNS)
[OPEN] 203.0.113.10:80 (HTTP)
[OPEN] 203.0.113.10:443 (HTTPS)
[TIMEOUT] 203.0.113.10:445 (SMB)
[TIMEOUT] 203.0.113.10:3389 (RDP)

Scan completed in 2.03 seconds.
Append to existing CSV? (Y/N): N
Results saved to scan_results.csv

Screenshot



Requirements

Python 3.10 or newer

No external packages required

Project Structure

Network-Port-Scanner/
├── main.py
├── README.md
├── LICENSE
├── .gitignore
├── sample_scan_results.csv
└── screenshots/
    └── sample-scan-results.png

Installation

Clone the repository:

git clone https://github.com/jcain5/network-port-scanner.git

Move into the project directory:

cd network-port-scanner

Run the scanner:

python3 main.py

On Windows, you may need to use:

python main.py

Usage

When prompted, enter the IP address of a system you own or are explicitly authorized to scan.

Target IP: 172.16.10.1

The scanner checks each configured TCP port and displays the result.

After the scan, choose whether to append the results to the existing CSV file or overwrite it.

Append to existing CSV? (Y/N):

Enter Y to preserve previous scans and append new rows.

Enter N to replace the CSV with the latest scan.

CSV Output

The scanner writes the following fields:

timestamp,target,port,service,status

Example:

timestamp,target,port,service,status
2026-07-31 22:10:00,203.0.113.10,22,SSH,OPEN
2026-07-31 22:10:00,203.0.113.10,53,DNS,OPEN
2026-07-31 22:10:00,203.0.113.10,80,HTTP,OPEN
2026-07-31 22:10:00,203.0.113.10,443,HTTPS,OPEN
2026-07-31 22:10:00,203.0.113.10,445,SMB,TIMEOUT

The automatically generated scan_results.csv file is excluded from Git to prevent real infrastructure data from being published.

A sanitized example is included as:

sample_scan_results.csv

Scanned Services

The current version checks common TCP services such as:

Port

Service

21

FTP

22

SSH

23

Telnet

25

SMTP

53

DNS over TCP

80

HTTP

110

POP3

135

Microsoft RPC

139

NetBIOS Session Service

143

IMAP

389

LDAP

443

HTTPS

445

SMB

465

SMTPS

587

SMTP Submission

636

LDAPS

993

IMAPS

995

POP3S

1433

Microsoft SQL Server

2049

NFS

3306

MySQL

3389

RDP

5432

PostgreSQL

5900

VNC

5985

WinRM HTTP

5986

WinRM HTTPS

8006

Proxmox

8080

Alternate HTTP

8443

Alternate HTTPS

Status Meanings

OPEN

A TCP connection was successfully established.

CLOSED

The target actively refused the TCP connection.

TIMEOUT

The target did not respond before the configured timeout expired. This may indicate firewall filtering, packet dropping, or an unresponsive service.

UNREACHABLE

The operating system reported that the target or route could not be reached.

Learning Objectives

This project was created to practice:

Python functions

Type hints

TCP socket programming

Exception handling

IP address validation

Dictionaries and lists

CSV file operations

File append and overwrite modes

Runtime measurement

Program entry points

Graceful interruption handling

Git and GitHub project packaging

Sanitizing infrastructure evidence for public documentation

Current Limitations

TCP scanning only

Scans one host at a time

Uses a predefined port list

Performs full TCP connection attempts

Does not perform operating-system detection

Does not perform service-version detection

Does not perform vulnerability scanning

Does not attempt authentication or exploitation

Sequential scanning may be slow when many ports time out

Planned Version 2.0 Features

CIDR subnet input

Multiple-host scanning

Concurrent scanning with thread pools

Hostname resolution

Command-line arguments

Configurable timeout values

Custom port ranges

Scan summaries

Optional JSON export

Sanitized reporting mode

Automated tests

Security and Authorized Use

This tool is intended only for systems and networks that you own or have explicit permission to test.

Unauthorized port scanning may violate organizational policies, service agreements, or applicable law.

The project does not perform exploitation, credential attacks, vulnerability testing, or authentication attempts.

License

This project is licensed under the MIT License. See the LICENSE file for details.
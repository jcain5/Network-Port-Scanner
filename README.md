# Network Port Scanner

A Python-based network port scanner built as a hands-on learning project for networking, Python, testing, concurrency, reporting, and protocol-aware scanning.

> Use this tool only on systems and networks you own or are explicitly authorized to test.

## Current Status

Completed:
- Phase 1: Core TCP scanner
- Phase 2: Modular CLI scanner
- Phase 3: Multi-host and CIDR scanning with concurrency
- Phase 3B: UDP scanning and DNS-aware probing
- Phase 4A: Scan summary reporting

In progress:
- Phase 4B: Filtering and grouping scan results

Automated tests: **56 passing**

## Features

### TCP Scanning

Supports common TCP services and statuses such as:
- `OPEN`
- `CLOSED`
- `TIMEOUT`
- `UNREACHABLE`

Example:

```bash
python3 main.py --target 192.168.1.254 --protocol tcp --ports 22,53,80,443 --timeout 1 --workers 1 --overwrite
```

### UDP Scanning

Supports:
- `OPEN`
- `OPEN|FILTERED`
- `CLOSED`
- `UNREACHABLE`

Example:

```bash
python3 main.py --target 192.168.1.254 --protocol udp --ports 53 --timeout 1 --workers 1 --overwrite
```

## DNS-Aware UDP Probing

UDP port 53 sends a valid DNS query instead of an empty UDP payload.

The scanner builds a DNS query for:

```text
example.com
```

Example result:

```text
[OPEN] 192.168.1.254: 53/UDP(DNS)
```

Authorized `/24` validation successfully identified multiple hosts responding to DNS queries.

## CIDR and Multi-Host Scanning

Supports:
- Single IPv4 addresses
- Single IPv6 addresses
- IPv4 CIDR ranges
- `/31`
- `/32`

Example:

```bash
python3 main.py --target 192.168.1.0/24 --workers 32
```

CIDR expansion is limited to **256 usable hosts**.

## Concurrent Host Scanning

The scanner uses Python's `ThreadPoolExecutor`.

Worker limits:
- Minimum: 1
- Maximum: 32
- Default: 8

Important: workers currently parallelize **hosts**, not ports.

Observed authorized-lab performance included:
- `/28` sequential-style scan: about 21 seconds
- `/28` with 4 workers: about 6 seconds
- `/28` with 8 workers: about 3 seconds
- `/24` with 32 workers: about 12 seconds
- `/24` UDP DNS scan: about 8 seconds

## Scan Summary

Phase 4A adds a summary after each scan.

Example:

```text
Scan Summary
========================================
Hosts scanned: 1
Ports scanned: 4
Open: 3
Timeout: 1
Open|Filtered: 0
Closed: 0
Unreachable: 0
```

The summary reports:
- Hosts scanned
- Ports scanned
- Open
- Timeout
- Open|Filtered
- Closed
- Unreachable

## CSV Reporting

Current CSV columns:

```text
timestamp,target,port,protocol,service,status
```

Example:

```text
2026-08-24 21:04:58,192.168.1.254,53,udp,DNS,OPEN
```

## Output Modes

Append:

```bash
--append
```

Overwrite:

```bash
--overwrite
```

## Custom Ports

Example:

```bash
python3 main.py --target 192.168.1.254 --protocol tcp --ports 22,53,80,443 --timeout 1 --overwrite
```

If `--ports` is omitted, the scanner uses all services currently defined in `scanner/services.py`.

This does **not** currently mean all 65,535 ports.

## Command-Line Options

```text
--target       Required IP address or CIDR target
--timeout      Socket timeout
--ports        Comma-separated port list
--output       CSV output filename
--workers      Concurrent host workers
--protocol     tcp or udp
--append       Append CSV output
--overwrite    Overwrite CSV output
```

## Project Structure

```text
Network-Port-Scanner/
├── main.py
├── scanner/
│   ├── __init__.py
│   ├── reporting.py
│   ├── scanning.py
│   ├── services.py
│   ├── targets.py
│   └── validation.py
└── tests/
    ├── __init__.py
    ├── test_arguments.py
    ├── test_main.py
    ├── test_scanning.py
    ├── test_targets.py
    └── test_validation.py
```

Refactoring is planned later and is intentionally not blocking feature development.

## Testing

macOS/Linux:

```bash
python3 -m unittest discover -v
```

Windows:

```powershell
py -m unittest discover -v
```

Current result:

```text
Ran 56 tests

OK
```

Tests cover:
- Argument parsing
- Timeout validation
- Worker validation
- Port parsing
- TCP status handling
- UDP status handling
- DNS name encoding
- DNS query packet construction
- DNS payload use on UDP/53
- TCP/UDP routing
- CIDR expansion
- `/31`
- `/32`
- Host limits
- IPv4 validation
- IPv6 validation
- Main application flow
- Thread pool configuration
- Combined result handling
- Scan status summaries

## Development Roadmap

### Phase 1 - Core Scanner
Completed.

### Phase 2 - Modular CLI Scanner
Completed.

### Phase 3 - Multi-Host Scanning
Completed.

### Phase 3B - UDP Support
Completed.

Includes:
- UDP sockets
- UDP-specific statuses
- Protocol selection
- DNS query packet construction
- DNS-aware UDP/53 probing
- Protocol-aware reporting

### Phase 4A - Scan Summary
Completed.

Includes:
- Host counts
- Port counts
- Status counts

### Phase 4B - Filtering and Grouping
Next.

Planned:
- Show only open results
- Group results by host
- Improve readability for larger scans

### Phase 4C - Historical Comparison
Planned.

Possible goals:
- Compare current and previous scans
- Identify newly opened ports
- Identify closed or disappeared services
- Highlight meaningful changes

### Phase 4D - Visualization
Planned.

Possible goals:
- Status distribution charts
- Open ports by host
- Scan trend visualization

### Phase 4E - Dashboard
Planned.

### Phase 5 - AI-Assisted Analysis
Future enhancement.

Possible goals:
- Summarize findings
- Explain important changes
- Highlight results that deserve investigation
- Generate human-readable analysis from authorized scan data

## Design Decisions

### Why `OPEN|FILTERED` Exists

UDP is connectionless. If a datagram receives no response, the scanner cannot always determine whether the port is open but silent or filtered by a firewall.

### Why DNS Gets a Special Probe

An empty UDP payload often receives no response. DNS has a defined request format, so UDP/53 sends a valid DNS query.

### Why Concurrency Is Limited

The scanner limits worker count to 32 and CIDR expansion to 256 usable hosts to keep scans controlled and suitable for authorized lab use.

## Requirements

Python 3.

The project currently uses only the Python standard library for its core functionality.

## Safety and Authorization

This project is intended for:
- Home labs
- Personally owned systems
- Training environments
- Networks where explicit authorization has been granted

Do not scan systems or networks without permission.

## Learning Goals

This project develops practical experience with:
- Python functions and modules
- Type hints
- Exceptions
- Socket programming
- TCP and UDP behavior
- DNS packet structure
- Binary data
- `struct.pack`
- CLI design
- Input validation
- CIDR addressing
- Concurrency
- `ThreadPoolExecutor`
- CSV reporting
- Unit testing
- Mocking
- Context managers
- Result analysis
- Incremental software development
- Git-based development workflow

## Current Milestone

```text
56 automated tests passing
TCP + UDP scanning operational
DNS-aware UDP probing operational
CIDR and concurrent host scanning operational
Protocol-aware console and CSV reporting operational
Scan summary operational
```

Next development step: **Phase 4B: filtering results to show only open findings**.

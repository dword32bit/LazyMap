# LazyMap

LazyMap is a Python script that automates the process of running Nmap scans on a target IP address. It is designed for users who are lazy or don't want to remember the various Nmap command-line options.

## Features

- Runs an initial Nmap scan to discover open ports on the target IP address.
- Extracts the open ports from the initial scan output.
- Runs a detailed Nmap scan on the discovered open ports, including SYN scan and version detection.
- Outputs the detailed scan results to the console.

## Usage

1. Ensure you have Python 3 and Nmap installed on your system.
2. Clone the repository:
   ```
   git clone https://github.com/dword32bit/LazyMap.git
   ```
3. Get into the directory:
   ```
   cd LazyMap
   ```
4. Run the script as root:

```
sudo python3 lazymap.py
```

4. Enter the target IP address when prompted.

The script will first run an initial Nmap scan to discover the open ports on the target. It will then run a detailed Nmap scan on the discovered open ports and display the results in the console.

## How it Works

1. The `extract_ports` function takes the output of the initial Nmap scan and extracts the open port numbers.
2. The `run_nmap` function first runs the initial Nmap scan with the `-p-` option to scan all ports.
3. The `extract_ports` function is used to extract the open ports from the initial scan output.
4. The `run_nmap` function then runs the detailed Nmap scan with the `-p` option, specifying the discovered open ports, and the `-sS` and `-sV` options for a SYN scan and version detection, respectively.
5. The detailed scan output is printed to the console.

## Disclaimer

This script is intended for educational and authorized testing purposes only. Do not use it to scan systems without permission, as that would be illegal.

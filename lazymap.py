import subprocess

def extract_ports(nmap_output):
    lines = nmap_output.strip().split('\n')
    ports = [line.split('/')[0] for line in lines if '/tcp' in line]
    return ','.join(ports)

def run_nmap(ip_target):
    initial_scan = subprocess.run(
        ["nmap", "-p-", ip_target], capture_output=True, text=True
    )

    open_ports = extract_ports(initial_scan.stdout)

    detailed_scan = subprocess.run(
        ["nmap", f"-p{open_ports}", ip_target, "-sS", "-sV", "-oN", "result"],
        capture_output=True, text=True
    )
    print(detailed_scan.stdout)

if __name__ == "__main__":
    ip_target = input("Input Target IP Address : ")
    run_nmap(ip_target)

import subprocess
import datetime

# Network targets to monitor
# Matches your Hybrid-NetOps-Cloud-Infrastructure-Lab topology
targets = {
    "R1-Gateway-VLAN10":  "192.168.10.1",
    "R1-Gateway-VLAN20":  "192.168.20.1",
    "R1-Gateway-VLAN30":  "192.168.30.1",
    "R1-Gateway-VLAN40":  "192.168.40.1",
    "PC-HR1":             "192.168.10.10",
    "PC-HR2":             "192.168.10.11",
    "PC-IT1":             "192.168.20.10",
    "PC-IT2":             "192.168.20.11",
    "PC-GUEST1":          "192.168.30.10",
    "SRV-MAIN":           "192.168.40.10",
    "Google-DNS":         "8.8.8.8",
    "Cloudflare-DNS":     "1.1.1.1"
}

log_file = "noc_monitor.log"

def ping(host):
    result = subprocess.run(
        ["ping", "-n", "1", "-w", "1000", host],
        capture_output=True,
        text=True
    )
    return "TTL=" in result.stdout

def run_check():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n{'='*60}")
    print(f"  Hybrid-NetOps-Cloud-Infrastructure-Lab")
    print(f"  NOC Monitor Check — {now}")
    print(f"{'='*60}")
    print(f"  {'Device':<25} {'IP Address':<18} {'Status'}")
    print(f"  {'-'*55}")

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"\n{'='*60}\n")
        f.write(f"NOC Monitor Check — {now}\n")
        f.write(f"{'Device':<25} {'IP Address':<18} {'Status'}\n")
        f.write(f"{'-'*55}\n")

        for name, ip in targets.items():
            status = "UP  [OK]" if ping(ip) else "DOWN [FAIL]"
            line = f"  {name:<25} {ip:<18} {status}"
            print(line)
            f.write(line.strip() + "\n")

    print(f"\n  Log file saved → {log_file}")
    print(f"{'='*60}\n")

run_check()

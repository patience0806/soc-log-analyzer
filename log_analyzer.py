from collections import defaultdict

THRESHOLD = 5

def analyze_logs(log_file):
    ip_activity = defaultdict(int)

    with open(log_file, "r") as file:
        for line in file:
            ip = line.split()[0]
            ip_activity[ip] += 1

    print("SOC Log Analysis Report")
    print("-" * 30)

    for ip, count in ip_activity.items():
        if count > THRESHOLD:
            print(f"[ALERT] Suspicious activity detected from {ip} ({count} requests)")
        else:
            print(f"[INFO] Normal activity from {ip} ({count} requests)")

if name == "main":
    analyze_logs("access.log")

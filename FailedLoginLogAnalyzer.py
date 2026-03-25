Python 3.14.3 (v3.14.3:323c59a5e34, Feb  3 2026, 11:41:37) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
import re
from collections import Counter
import csv

LOG_FILE = "sample_auth.log"


... # Regex pattern for failed SSH login attempts
... pattern = re.compile(
...     r"(\w+\s+\d+\s+\d+:\d+:\d+).*Failed password for (?:invalid user )?(\w+) from (\d{1,3}(?:\.\d{1,3}){3})"
... )
... 
... failed_attempts = []
... ip_counter = Counter()
... 
... try:
...     with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as file:
...         for line in file:
...             match = pattern.search(line)
...             if match:
...                 timestamp, user, ip = match.groups()
...                 failed_attempts.append((timestamp, user, ip))
...                 ip_counter[ip] += 1
... 
... except FileNotFoundError:
...     print(f"Error: File '{LOG_FILE}' not found.")
...     exit()
... 
... # === OUTPUT RESULTS ===
... print("\n=== Failed Login Attempts ===")
... for timestamp, user, ip in failed_attempts:
...     print(f"Time: {timestamp} | User: {user} | IP: {ip}")
... 
... print(f"\nTotal Failed Attempts: {len(failed_attempts)}")
... 
... print("\nTop Offending IPs:")
... for ip, count in ip_counter.most_common(5):
...     print(f"{ip} -> {count} attempts")
... 
... # === SAVE TO CSV ===
... with open("failed_logins.csv", "w", newline="") as csvfile:
...     writer = csv.writer(csvfile)
...     writer.writerow(["Timestamp", "Username", "IP Address"])
...     writer.writerows(failed_attempts)
... 

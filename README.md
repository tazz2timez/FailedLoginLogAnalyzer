# Failed Login Log Analyzer (Python)

## 📌 Project Overview

This project is a **Python-based log analyzer** that scans system log files to identify and report failed login attempts. It extracts useful security insights such as:

* Number of failed login attempts
* IP addresses associated with failures
* Timestamps of each failed attempt
* Most frequent offending IPs

This is a practical, real-world project commonly used in **IT support, cybersecurity, and system administration**.

---

## 🧠 Features

* Parses Linux-style authentication logs (e.g., `/var/log/auth.log`)
* Detects failed SSH login attempts
* Extracts:

  * Timestamp
  * Username
  * IP address
* Counts total failed attempts
* Displays top offending IP addresses
* Optional: Save results to a CSV file

---

## 🛠️ Technologies Used

* Python 3
* Regular Expressions (`re`)
* Collections (`Counter`)
* CSV module

---

## 📂 Sample Log Format Used

Example log lines used for testing:

```
Mar 10 10:15:32 server sshd[1234]: Failed password for invalid user admin from 192.168.1.10 port 22 ssh2
Mar 10 10:16:01 server sshd[1235]: Failed password for root from 192.168.1.11 port 22 ssh2
Mar 10 10:17:45 server sshd[1236]: Failed password for invalid user test from 192.168.1.10 port 22 ssh2
```

---

## 💻 Python Script

```python
import re
from collections import Counter
import csv

# Sample log file (you can replace this with a real file path)
LOG_FILE = "sample_auth.log"

# Regex pattern for failed login attempts
pattern = re.compile(
    r"(\w+\s+\d+\s+\d+:\d+:\d+).*Failed password for (?:invalid user )?(\w+) from ([\d\.]+)"
)

failed_attempts = []
ip_counter = Counter()

with open(LOG_FILE, "r") as file:
    for line in file:
        match = pattern.search(line)
        if match:
            timestamp, user, ip = match.groups()
            failed_attempts.append((timestamp, user, ip))
            ip_counter[ip] += 1

# Output results
print("\n=== Failed Login Attempts ===")
for attempt in failed_attempts:
    print(f"Time: {attempt[0]}, User: {attempt[1]}, IP: {attempt[2]}")

print("\nTotal Failed Attempts:", len(failed_attempts))

print("\nTop Offending IPs:")
for ip, count in ip_counter.most_common(5):
    print(f"{ip}: {count} attempts")

# Save to CSV (optional)
with open("failed_logins.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Timestamp", "Username", "IP Address"])
    writer.writerows(failed_attempts)

print("\nResults saved to failed_logins.csv")
```



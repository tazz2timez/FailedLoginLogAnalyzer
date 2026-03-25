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

---

## 📄 How to Use

1. Create a sample log file named `sample_auth.log`
2. Paste sample log entries into the file
3. Run the script:

```
python log_analyzer.py
```

4. View results in the terminal or in the generated CSV file

---

## 🚀 Possible Enhancements

* Add support for Windows Event Logs
* Detect brute-force attacks (threshold-based alerts)
* Visualize results using graphs (matplotlib)
* Add CLI arguments (argparse)
* Real-time monitoring (tail -f style)

---

## 📌 Resume Description

**Failed Login Log Analyzer (Python)**
Developed a Python-based log analysis tool to detect and analyze failed SSH login attempts from system logs. Implemented regex-based parsing to extract timestamps, usernames, and IP addresses, and used data aggregation techniques to identify high-frequency attack sources. Exported structured results to CSV for further analysis. Demonstrates skills in Python scripting, cybersecurity fundamentals, and log analysis.

---

## 🔥 Why This Project Stands Out

* Real-world cybersecurity relevance
* Demonstrates log parsing (key IT skill)
* Shows understanding of security threats (brute-force attacks)
* Easy to explain in interviews

---

## 💡 Interview Talking Points

* How regex was used to parse logs
* Why failed login tracking is important
* How this can help detect brute-force attacks
* How you would scale this for enterprise systems

---

## 📁 Suggested File Structure

```
failed-login-analyzer/
│
├── log_analyzer.py
├── sample_auth.log
├── failed_logins.csv
└── README.md
```

---

## 🧪 Extra: Sample Log File Content

```
Mar 10 10:15:32 server sshd[1234]: Failed password for invalid user admin from 192.168.1.10 port 22 ssh2
Mar 10 10:16:01 server sshd[1235]: Failed password for root from 192.168.1.11 port 22 ssh2
Mar 10 10:17:45 server sshd[1236]: Failed password for invalid user test from 192.168.1.10 port 22 ssh2
Mar 10 10:18:12 server sshd[1237]: Failed password for user from 192.168.1.12 port 22 ssh2
Mar 10 10:19:55 server sshd[1238]: Failed password for invalid user guest from 192.168.1.10 port 22 ssh2
```

---

## ✅ Final Notes

This project is simple but **highly relevant** for entry-level IT, help desk, and cybersecurity roles. It shows practical skills that employers look for and can be expanded into more advanced security tools.

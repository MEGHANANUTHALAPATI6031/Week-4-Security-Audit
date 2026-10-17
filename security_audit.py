
from datetime import datetime

print("=" * 55)
print("ENTERPRISE SECURITY AUDIT SYSTEM")
print("=" * 55)

assets = [
    "Web Application",
    "Database Server",
    "Enterprise Network",
    "User Authentication System"
]

findings = [
    ("SQL Injection Vulnerability", "High",
     "Use parameterized SQL queries"),
    ("Weak Administrative Access Control", "High",
     "Implement role-based access control and MFA"),
    ("Database Service Exposure", "Medium",
     "Restrict database access using firewall rules"),
    ("Insufficient Security Monitoring", "Medium",
     "Enable centralized logging and monitoring")
]

print("\nAUDIT DATE:", datetime.now().strftime("%d-%m-%Y"))

print("\nASSET INVENTORY")
for asset in assets:
    print("-", asset)

print("\nSECURITY AUDIT FINDINGS")

for issue, risk, recommendation in findings:
    print("\nFinding:", issue)
    print("Risk Level:", risk)
    print("Recommendation:", recommendation)

print("\nRISK SUMMARY")
print("High Risks:", 2)
print("Medium Risks:", 2)

print("\nSECURITY IMPROVEMENT ROADMAP")
print("Immediate: Fix SQL injection and administrative access.")
print("Short Term: Restrict database access.")
print("Long Term: Improve monitoring and periodic audits.")

print("\nAudit completed successfully.")

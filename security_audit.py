
from datetime import datetime
import json
import csv
import os
import sqlite3

# Enterprise Security Audit - Educational Simulation
AUDIT_DATE = datetime.now().strftime("%d-%m-%Y")
OUTPUT_DIR = "audit_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

assets = [
    {
        "name": "Web Application",
        "controls": "Input validation; parameterized database queries",
        "expected": "Parameterized queries and input validation tests",
        "status": "Needs verification"
    },
    {
        "name": "Database Server",
        "controls": "Database access restrictions",
        "expected": "Firewall allowlist and restricted database permissions",
        "status": "Needs verification"
    },
    {
        "name": "Enterprise Network",
        "controls": "Network access controls",
        "expected": "Documented firewall rules and periodic rule reviews",
        "status": "Needs verification"
    },
    {
        "name": "User Authentication System",
        "controls": "Administrative authentication",
        "expected": "Role-based access control and MFA for administrators",
        "status": "Needs verification"
    }
]
def run_sql_injection_protection_test():
    """Test parameterized SQL queries in a temporary database."""
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE users (username TEXT, role TEXT)")
    cursor.execute(
        "INSERT INTO users VALUES (?, ?)",
        ("demo_user", "voter")
    )

    test_input = "' OR '1'='1"

    cursor.execute(
        "SELECT username FROM users WHERE username = ?",
        (test_input,)
    )
    result = cursor.fetchall()

    connection.close()

    return {
        "test": "Parameterized SQL query test",
        "result": "PASS" if len(result) == 0 else "FAIL",
        "details": (
            "Test input was treated as data, not SQL code."
            if len(result) == 0
            else "Unexpected result; review the query."
        )
    }
findings = [
    {
        "id": "F-01",
        "title": "SQL Injection Risk",
        "asset": "Web Application",
        "severity": "High",
        "likelihood": 4,
        "impact": 5,
        "observation": (
            "The initial audit script identifies SQL injection as a risk. "
            "Application code and database queries have not yet been tested."
        ),
        "evidence": "E-01: Initial audit script output; application test evidence pending.",
        "gap": "Parameterized queries and input validation have not been verified.",
        "action": "Review database queries; use parameterized queries; run authorized input-validation tests.",
        "owner": "Application Developer",
        "deadline": "Days 1-3",
        "verification": "Code review and documented safe test results",
        "status": "Open - validation required"
    },
    {
        "id": "F-02",
        "title": "Administrative Access Control Risk",
        "asset": "User Authentication System",
        "severity": "High",
        "likelihood": 4,
        "impact": 5,
        "observation": (
            "The initial audit script flags administrative access control. "
            "Actual account permissions and MFA settings have not been inspected."
        ),
        "evidence": "E-01: Initial audit script output; account review pending.",
        "gap": "Role separation, least privilege, and administrator MFA require verification.",
        "action": "Review admin accounts; remove unnecessary privileges; enable MFA and test access restrictions.",
        "owner": "Security Administrator",
        "deadline": "Days 1-7",
        "verification": "Approved account inventory and access-control test results",
        "status": "Open - validation required"
    },
    {
        "id": "F-03",
        "title": "Database Service Exposure Risk",
        "asset": "Database Server",
        "severity": "Medium",
        "likelihood": 3,
        "impact": 4,
        "observation": (
            "The initial audit script flags possible database exposure. "
            "No port scan or firewall configuration evidence is included yet."
        ),
        "evidence": "E-01: Initial audit script output; firewall evidence pending.",
        "gap": "Allowed source addresses, exposed services, and firewall rules need review.",
        "action": "Review approved firewall rules; restrict database connections to authorized application hosts.",
        "owner": "Network Administrator",
        "deadline": "Days 8-14",
        "verification": "Firewall review record and authorized connectivity test",
        "status": "Open - validation required"
    },
    {
        "id": "F-04",
        "title": "Security Monitoring Gap",
        "asset": "Enterprise Network",
        "severity": "Medium",
        "likelihood": 3,
        "impact": 3,
        "observation": (
            "The initial audit script flags insufficient monitoring. "
            "Log collection and alerting configurations have not been inspected."
        ),
        "evidence": "E-01: Initial audit script output; log review evidence pending.",
        "gap": "Centralized logs, alert rules, retention, and review responsibilities require verification.",
        "action": "Define log sources; centralize relevant logs; configure alerts and a review schedule.",
        "owner": "Security Monitoring Team",
        "deadline": "Days 15-30",
        "verification": "Sample log records, test alert, and documented review procedure",
        "status": "Open - validation required"
    }
]

print("=" * 65)
print("ENTERPRISE SECURITY AUDIT - SIMULATED ENVIRONMENT")
print("=" * 65)
print("Audit date:", AUDIT_DATE)
print("Framework references: NIST CSF 2.0; CIS Controls")
print("Scope: Four simulated enterprise assets")
print("Note: Risks are preliminary until supporting tests are completed.")

print("\n1. ASSET INVENTORY")
for asset in assets:
    print(f"\nAsset: {asset['name']}")
    print(f"Control area: {asset['controls']}")
    print(f"Expected practice: {asset['expected']}")
    print(f"Assessment status: {asset['status']}")

print("\n2. DETAILED AUDIT FINDINGS")
for item in findings:
    score = item["likelihood"] * item["impact"]
    item["risk_score"] = score
    print("\n" + "-" * 65)
    print(f"{item['id']}: {item['title']}")
    print(f"Asset: {item['asset']}")
    print(f"Severity: {item['severity']}")
    print(f"Preliminary risk score: {score}/25")
    print(f"Observation: {item['observation']}")
    print(f"Evidence: {item['evidence']}")
    print(f"Gap: {item['gap']}")
    print(f"Recommended action: {item['action']}")
    print(f"Owner: {item['owner']}")
    print(f"Target: {item['deadline']}")
    print(f"Verification: {item['verification']}")
    print(f"Status: {item['status']}")

high_count = sum(1 for f in findings if f["severity"] == "High")
medium_count = sum(1 for f in findings if f["severity"] == "Medium")

print("\n3. PRELIMINARY RISK SUMMARY")
print("High-priority findings:", high_count)
print("Medium-priority findings:", medium_count)
print("Risk formula: Likelihood (1-5) x Impact (1-5)")
print("Scores are preliminary estimates, not measured exploitability.")

print("\n4. GAP ANALYSIS")
for item in findings:
    print(f"{item['id']} | {item['asset']}")
    print("  Gap:", item["gap"])
    print("  Required action:", item["action"])

print("\n5. REMEDIATION ROADMAP")
print("Immediate - Days 1-7: Application Developer and Security Administrator")
print("  Review SQL queries, admin permissions, and MFA configuration.")
print("Short term - Days 8-14: Network Administrator")
print("  Review firewall rules and restrict database connectivity.")
print("Long term - Days 15-30: Security Monitoring Team")
print("  Configure log collection, alert testing, and scheduled reviews.")
print("After each change: retain test results and record approval.")

# Export structured findings for use in the report.
json_path = os.path.join(OUTPUT_DIR, "audit_findings.json")
with open(json_path, "w", encoding="utf-8") as file:
    json.dump(
        {
            "audit_date": AUDIT_DATE,
            "scope": assets,
            "findings": findings,
            "evidence_note": (
                "Initial script output is supporting evidence only. "
                "Technical validation evidence must be collected separately."
            )
        },
        file,
        indent=4
    )

csv_path = os.path.join(OUTPUT_DIR, "remediation_plan.csv")
with open(csv_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "id", "title", "asset", "severity", "risk_score",
            "gap", "action", "owner", "deadline", "verification", "status"
        ]
    )
    writer.writeheader()
    for item in findings:
        writer.writerow({
            key: item[key]
            for key in writer.fieldnames
        })

print("\n6. GENERATED REPORT SUPPORT FILES")
print("Findings JSON:", json_path)
print("Remediation CSV:", csv_path)
print("\nAudit simulation completed.")
print("Reminder: Validate each risk and attach real test evidence before submission.")
sql_test_result = run_sql_injection_protection_test()
sql_test_path = os.path.join(OUTPUT_DIR, "sql_parameterized_test.txt")

with open(sql_test_path, "w", encoding="utf-8") as file:
    file.write("LOCAL SQL PARAMETERIZATION TEST\n")
    file.write("Environment: Temporary in-memory SQLite database\n")
    file.write(f"Test: {sql_test_result['test']}\n")
    file.write(f"Result: {sql_test_result['result']}\n")
    file.write(f"Details: {sql_test_result['details']}\n")
    file.write(
        "Limitation: This tests a local parameterized query only; "
        "it does not verify the actual web application.\n"
    )

print("SQL parameterization test:", sql_test_result["result"])
print("SQL test evidence:", sql_test_path)

# Week 4 - Comprehensive Security Audit and Strategic Recommendations

## Internship
Yuva Internship - Cybersecurity

## Project Overview
This project is an educational security audit simulation for a virtual enterprise environment. It organizes a four-asset inventory, preliminary risk findings, gap analysis, risk scoring, and a prioritized remediation roadmap.

## Audit Scope
The simulated assets are:
1. Web Application
2. Database Server
3. Enterprise Network
4. User Authentication System

## Framework References
The assessment structure is informed by NIST Cybersecurity Framework (CSF) 2.0 and CIS Controls. Referencing these frameworks does not imply certification or a complete compliance assessment.

## Tools and Technologies
- Python
- JSON for structured audit findings
- CSV for the remediation plan
- PowerShell for running the program and verifying output
- Git and GitHub for version control and source hosting

## Risk Scoring
Preliminary risk score = Likelihood (1-5) x Impact (1-5).

- F-01: SQL Injection Risk - High, 20/25
- F-02: Administrative Access Control Risk - High, 20/25
- F-03: Database Service Exposure Risk - Medium, 12/25
- F-04: Security Monitoring Gap - Medium, 9/25

These are preliminary estimates for the simulation, not measured exploitability results. Each finding remains open pending technical validation.

## Remediation Roadmap
### Immediate: Days 1-7
Application Developer: Review query construction, implement parameterized queries where required, and document safe validation tests.

Security Administrator: Review administrator accounts, enforce least privilege, verify MFA, and retain access-review evidence.

### Short Term: Days 8-14
Network Administrator: Review firewall rules and database listening configuration. Restrict database connectivity to approved hosts and document authorized verification tests.

### Long Term: Days 15-30
Security Monitoring Team: Identify required log sources, configure centralized collection and alerting, test alerts, and document log retention and review schedules.

After each remediation, retain test evidence and approval records.

## Project Files
- security_audit.py - Main audit simulation
- security_audit_backup.py - Backup of the original program
- README.md - Project documentation
- audit_evidence.txt - Saved output from the initial audit run
- audit_output/audit_findings.json - Structured asset inventory and findings
- audit_output/remediation_plan.csv - Prioritized remediation plan
- audit_output/evidence_log.txt - Evidence register and limitations
- audit_output/control_validation_checklist.txt - Checklist for further technical review

## Evidence and Limitations
The program execution and generated files demonstrate that the audit simulation runs and produces structured findings. They do not prove that the listed vulnerabilities are present in a real system. Application code, access settings, firewall rules, and monitoring configurations still need to be reviewed and tested in an authorized environment. Results must be updated only when supporting evidence is collected.

## Conclusion
The project demonstrates a structured approach to asset inventory, preliminary risk assessment, gap identification, and security remediation planning. Future work should include evidence-backed control validation and verification of remediation outcomes.

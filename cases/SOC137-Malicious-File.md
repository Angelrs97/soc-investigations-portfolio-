# Incident Investigation Report: SOC137

## 📋 Executive Summary
This report documents the detailed forensic analysis and incident response procedures performed for **SOC137 - Malicious File/Script Download Attempt** (Event ID: 76) on the [LetsDefend](https://app.letsdefend.io/monitoring) platform. The alert was successfully investigated, triaged, and closed as a **True Positive** within the predefined SLA.

---

## 🔍 Incident Details
| Parameter | Details |
| :--- | :--- |
| **Rule Name** | SOC137 - Malicious File/Script Download Attempt |
| **Event ID** | 76 |
| **Event Time** | 2021-03-14 19:15:52 +03:00 |
| **Closed At** | 2026-10-29 02:38:22 UTC |
| **Severity** | Medium |
| **Type** | Malware |
| **Result** | True Positive |
| **MITRE ATT&CK** | [T1204 - User Execution](https://attack.mitre.org/techniques/T1204/) |

---

## 📦 Artifact Information
* **File Name:** `INVOICE PACKAGE LINK TO DOWNLOAD.docm`
* **File Size:** 16.66 Kb
* **File Hash (MD5/SHA):** `f2d0c66b801244c059f636d08a474079`
* **Source Hostname:** `NicolasPRD`
* **Source Address:** `172.16.17.37`
* **Device Action:** Blocked

---

## 🛠️ Playbook Execution & Results
* **Check If Someone Requested the C2:** Not Accessed
* **Analyze Malware:** Malicious
* **Check if the malware is quarantined/cleaned:** Quarantined
* **Playbook Score:** 15/15 (100% success rate)

---

## 🕵️‍♂️ Investigation Methodology & Step-by-Step
To reach the conclusion that this event was a **True Positive**, the following investigative steps were performed:

1. **Alert Triage & Log Analysis:** 
   * Reviewed endpoint telemetry and network logs for host `NicolasPRD` (`172.16.17.37`).
   * Identified suspicious user activity involving an incoming macro-enabled Word document (`INVOICE PACKAGE LINK TO DOWNLOAD.docm`).
2. **Artifact & Hash Investigation:** 
   * Extracted and analyzed the file hash (`f2d0c66b801244c059f636d08a474079`).
   * Confirmed indicators of compromise (IoCs) associated with phishing campaigns designed to trigger local script execution (MITRE T1204).
3. **C2 & Network Verification:** 
   * Checked proxy and firewall logs to verify if outbound connections or Command & Control (C2) requests were established. Result: *Not Accessed*.
4. **Containment & Remediation Check:** 
   * Verified via endpoint security tools that the EDR solution successfully blocked the execution and placed the file into quarantine.

---

## 📝 Analyst Notes & Findings
This incident represents a classic social engineering trap file (phishing/malspam) designed to exploit legacy Microsoft Office vulnerabilities when a user attempts to open what appears to be an urgent invoice or business document. 

1. **Identification:** The alert triggered due to suspicious script execution attempts linked to an incoming macro-enabled Word document.
2. **Containment:** Confirmed that network requests to potential C2 servers were blocked and the artifact was successfully quarantined on the endpoint (`NicolasPRD`).
3. **Remediation:** Closed as a verified True Positive following standard incident response playbooks.
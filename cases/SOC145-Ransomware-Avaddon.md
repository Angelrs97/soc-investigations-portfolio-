# Incident Investigation Report: SOC145 - Ransomware Detected

## 📋 Executive Summary
This report documents the forensic analysis and incident response procedures performed for **SOC145 - Ransomware Detected** (Event ID: 92) on the [LetsDefend](https://app.letsdefend.io/monitoring) platform. The alert was classified as a **Critical** severity threat involving an active ransomware execution (`ab.exe`). The case was successfully investigated, triaged, mitigated via host containment, and closed as a **True Positive**.

---

## 🔍 Incident Details
| Parameter | Details |
| :--- | :--- |
| **Rule Name** | SOC145 - Ransomware Detected |
| **Event ID** | 92 |
| **Event Time** | 2021-05-23 19:32:16 +03:00 |
| **Closed At** | 2026-10-21 01:46:55 UTC |
| **Severity** | Critical |
| **Type** | Malware (Ransomware) |
| **Result** | True Positive |
| **MITRE ATT&CK** | [T1204 - User Execution](https://attack.mitre.org/techniques/T1204/) |

---

## 📦 Artifact & Endpoint Information
* **Process Name:** `ab.exe` (Avaddon Ransomware variant)
* **File Size:** 775.50 Kb
* **File Hash (MD5/SHA):** `0b486fe0503524cfe4726a4022fa6a68`
* **Source Hostname:** `MarkPRD`
* **Source Address:** `172.16.17.88`
* **Initial Device Action:** Allowed

---

## 🛠️ Playbook Execution & Results
* **Check If Someone Requested the C2:** Not Accessed *(Confirmed via network analysis; no external C2 communication channels were established during execution)*
* **Analyze Malware:** Malicious
* **Check if the malware is quarantined/cleaned:** Not Quarantined *(Initial execution allowed prior to manual analyst isolation)*

---

## 🕵️‍♂️ Investigation Methodology & Findings
1. **Alert Triage:** 
   * Reviewed high-priority critical alerts regarding suspicious process execution (`ab.exe`) on endpoint `MarkPRD` (`172.16.17.88`).
2. **Threat & Hash Analysis:** 
   * Validated the file hash (`0b486fe0503524cfe4726a4022fa6a68`) through threat intelligence sources, confirming it as an active Avaddon ransomware variant.
3. **Behavioral & Dynamic Assessment:** 
   * Conducted behavioral analysis to evaluate payload activity. The executable successfully bypassed initial preventive controls (`Device Action: Allowed`) and proceeded to encrypt local files on the endpoint.
   * Inspected network logs to determine if external Command & Control (C2) servers were contacted; confirmed that no C2 channel was requested or active during the incident lifecycle.
4. **Containment & Remediation:** 
   * Executed immediate **Host Containment** on `MarkPRD` through the endpoint security console to successfully isolate the machine and prevent potential lateral movement across the network.

---

## 📝 Analyst Notes & Conclusion
* **True Positive Verdict:** Verified as a definitive True Positive because `ab.exe` exhibited destructive ransomware behavior, successfully encrypting files locally on the machine.
* **Key Takeaway:** This incident underscores the importance of behavioral monitoring and rapid manual containment when initial preventive sensors allow a payload execution. Understanding runtime behavior through dynamic analysis is essential for accurate scoping and limiting the blast radius in enterprise environments.
# Incident Investigation Report: SOC165 - Possible SQL Injection Payload Detected

## 📋 Executive Summary
This report documents the web traffic analysis and incident response procedures performed for **SOC165 - Possible SQL Injection Payload Detected** (Event ID: 115) on the [LetsDefend](https://app.letsdefend.io/monitoring) platform. The alert was classified as a **High** severity web attack targeting the organization's public-facing application. Following deep-dive URL decoding and log correlation, the alert was triaged and closed as a **True Positive** (unsuccessful exploitation attempt).

---

## 🔍 Incident Details
| Parameter | Details |
| :--- | :--- |
| **Rule Name** | SOC165 - Possible SQL Injection Payload Detected |
| **Event ID** | 115 |
| **Event Time** | 2022-02-25 11:34:32 +03:00 |
| **Closed At** | 2026-07-20 16:17:16 UTC |
| **Severity** | High |
| **Type** | Web Attack |
| **Result** | True Positive |
| **MITRE ATT&CK** | [T1190 - Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) |

---

## 🌐 Network & Request Artifacts
* **Hostname:** `WebServer1001`
* **Source IP Address:** `167.99.169.17`
* **Destination IP Address:** `172.16.17.18`
* **HTTP Request Method:** `GET`
* **User-Agent:** `Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1`
* **Device Action:** `Allowed`
* **Raw Requested URL:** `https://172.16.17.18/search/?q=%22%20OR%201%20%3D%201%20--%20-`

---

## 🛠️ Playbook Execution & Results
* **Is Traffic Malicious?:** Yes (`Malicious`)
* **What Is The Attack Type?:** `SQL Injection`
* **Check If It Is a Planned Test?:** `Not Planned`

---

## 🕵️‍♂️ Investigation Methodology & Step-by-Step
1. **Initial Alert Triage:** 
   * Reviewed high-priority web attack alerts triggered by the rule *Requested URL Contains OR 1 = 1* targeting `WebServer1001`.
2. **URL Decoding & Payload Analysis:** 
   * Analyzed the encoded query parameter from the requested URL (`%22%20OR%201%20%3D%201%20--%20-`).
   * Decoded the payload to reveal the classic SQL injection string: `") OR 1 = 1 -- -`, confirming malicious intent.
3. **Log Management & Source IP Correlation:** 
   * Filtered historical traffic by the attacker's source IP (`167.99.169.17`) in the Log Management console. 
   * Identified multiple secondary requests directed toward the application's search functionality, all validating recurring SQL injection probing patterns.
4. **Response Impact Assessment:** 
   * Analyzed server response codes and payload sizes. All associated requests returned an **HTTP 500 Internal Server Error** with uniform response sizes. 
   * Concluded that while the attack vector was definitively malicious (True Positive), the exploitation attempt was **unsuccessful**, as the backend application properly errored out rather than leaking valid database records (which would typically present varying response sizes and HTTP 200 statuses).

---

## 📝 Analyst Notes & Conclusion
* **True Positive Verdict:** Classified as a True Positive because the source IP actively probed the web application using crafted SQL injection payloads.
* **Key Takeaway:** Analyzing raw request strings via URL decoding combined with HTTP response status and size analysis is critical in Web Application Firewall (WAF) log triage. It allows analysts to distinguish between active scanning/exploitation attempts and successful compromises.
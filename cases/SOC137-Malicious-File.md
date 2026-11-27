# SOC137 Malicious File Download Attempt

**LetsDefend training simulation · Event 76 · Medium severity**

I closed this alert as a **true positive for an attempted download of a malicious document**. The alert recorded a block, and I initiated host containment as a precaution. Execution and impact on the endpoint remained unconfirmed.

## Investigation and decision

| Step | Tool or source | Observation and reasoning |
| --- | --- | --- |
| Triage the alert | LetsDefend Monitoring | The alert associated a macro-enabled Word document with the endpoint and reported **Device Action: Blocked**. The alert did not identify the stage at which the block occurred. |
| Check the file hash | VirusTotal | I looked up the MD5 supplied in the alert: **f2d0c66b801244c059f636d08a474079**. Multiple security engines flagged the file as malicious. These detections supported the true-positive verdict for the download attempt. |
| Initiate host containment | LetsDefend Endpoint Security | I selected **Containment** for the affected endpoint as a precaution in the simulation. The resulting isolation status was not independently verified. |
| Document the playbook result | LetsDefend playbook | I selected **Quarantined** for the malware-cleanup question based on the reported block. The file's quarantine status was not independently verified. |

## Scope and follow-up

The file-reputation results supported the alert classification. Determining whether the document executed or caused any impact would require additional endpoint evidence. The playbook recorded **Not Accessed** for the C2 check. That result alone does not confirm that a network control blocked a connection.

[File reputation report](https://www.virustotal.com/gui/file/08d4fd5032b8b24072bdff43932630d4200f68404d7e12ffeeda2364c8158873/detection)

# Splunk Authentication Investigation Lab

A defensive SOC training exercise for investigating repeated login failures and a subsequent successful login. The dataset is synthetic and was prepared with AI assistance. The analyst investigation, screenshots, and conclusions are pending.

## Files

| File | Purpose |
| --- | --- |
| [authentication.jsonl](authentication.jsonl) | Synthetic authentication events, one JSON object per line |
| [generate_logs.py](generate_logs.py) | Recreates the dataset with Python 3 and the standard library. It runs offline. |
| [queries.spl](queries.spl) | Starter Splunk searches for event counts, a timeline, and failed login activity |
| [REPORT_TEMPLATE.md](REPORT_TEMPLATE.md) | Template for documenting evidence, conclusions, and next steps |

## Run the lab

1. Use the supplied JSONL file or run `python generate_logs.py` to recreate it.
2. Import the file into Splunk as JSON events. Verify that each line becomes one event and that the fields are extracted, then replace `YOUR_LAB_INDEX` in the searches.
3. Group events by source IP, username, and outcome. Use the timestamps to reconstruct the sequence and distinguish the suspicious pattern from routine activity.
4. Save screenshots of your own searches and complete the report. Explain what the logs establish and which additional records would help determine whether the successful login was authorized.

from pathlib import Path
from datetime import datetime, timedelta, timezone
import json

events = []
start = datetime(2026, 11, 7, 9, 0, tzinfo=timezone.utc)
for number in range(6):
    events.append(dict(timestamp=(start + timedelta(seconds=number * 45)).isoformat(),
                       host="LAB-WEB01", source_ip="192.0.2.10", user="demo_user",
                       service="web_login", outcome="success", event_type="authentication"))
for number in range(25):
    events.append(dict(timestamp=(start + timedelta(minutes=10, seconds=number * 3)).isoformat(),
                       host="LAB-WEB01", source_ip="198.51.100.23", user="lab_admin",
                       service="web_login", outcome="failure", event_type="authentication"))
events.append(dict(timestamp=(start + timedelta(minutes=11, seconds=20)).isoformat(),
                   host="LAB-WEB01", source_ip="198.51.100.23", user="lab_admin",
                   service="web_login", outcome="success", event_type="authentication"))
destination = Path(__file__).parent / "authentication.jsonl"
destination.write_text("".join(json.dumps(event) + "\n" for event in events), encoding="utf-8")
print(f"Created {len(events)} synthetic events in {destination.name}")

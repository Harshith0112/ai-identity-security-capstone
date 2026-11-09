
import json
from datetime import datetime, timezone
from collections import defaultdict, deque

INPUT_FILE = "detection/security_events.json"
ALERT_FILE = "detection/security_alerts.json"

alerts = []

def parse_time(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))

def alert(event, alert_type, message):
    result = {
        "timestamp": event["timestamp"],
        "identity": event["identity"],
        "event_type": alert_type,
        "message": message
    }
    alerts.append(result)
    print("\n[SECURITY ALERT]")
    print(json.dumps(result, indent=2))


def detect_volume_spike(events):
    windows = defaultdict(deque)

    for event in events:
        if event["event_type"] != "llm_api_call":
            continue

        identity = event["identity"]
        current = parse_time(event["timestamp"])
        window = windows[identity]

        window.append(current)

        while window and (current - window[0]).total_seconds() > 60:
            window.popleft()

        if len(window) == 21:
            alert(
                event,
                "LLM_API_VOLUME_SPIKE",
                f"{len(window)} requests within 60 seconds"
            )


def detect_scope_change(events):
    previous_scope = {}

    for event in events:
        identity = event["identity"]

        if event["event_type"] != "agent_request":
            continue

        current_scope = set(event["scope"].split())

        if identity in previous_scope:
            old_scope = previous_scope[identity]

            if current_scope != old_scope:
                alert(
                    event,
                    "AGENT_SCOPE_CHANGE",
                    f"Scope changed from {sorted(old_scope)} "
                    f"to {sorted(current_scope)}"
                )

        previous_scope[identity] = current_scope


def detect_expired_token_reuse(events):
    token_usage = set()

    for event in events:
        if event["event_type"] != "token_use":
            continue

        token_id = event["token_id"]
        current_time = parse_time(event["timestamp"])
        expiry = datetime.fromtimestamp(
            int(event["token_exp"]),
            tz=timezone.utc
        )

        key = (event["identity"], token_id)

        # Alert when an expired token is presented again.
        if current_time > expiry and key in token_usage:
            alert(
                event,
                "EXPIRED_TOKEN_REUSE",
                "Previously observed token was reused after expiry"
            )

        token_usage.add(key)


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        events = json.load(file)

    events.sort(key=lambda e: parse_time(e["timestamp"]))

    detect_volume_spike(events)
    detect_scope_change(events)
    detect_expired_token_reuse(events)

    with open(ALERT_FILE, "w", encoding="utf-8") as file:
        json.dump(alerts, file, indent=2)

    print("\n================================")
    print("ANOMALY DETECTION COMPLETED")
    print("Total alerts:", len(alerts))
    print("Alert file:", ALERT_FILE)
    print("================================")


if __name__ == "__main__":
    main()

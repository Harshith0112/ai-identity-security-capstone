import json
from pathlib import Path
from datetime import datetime, timezone

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)


def save_results(filename, results):
    output = LOG_DIR / filename

    data = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "results": results
    }

    with open(output, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"\nResults saved to: {output}")


def print_result(title, prompt, response, success):
    print("\n" + "=" * 65)
    print(title)
    print("=" * 65)
    print("INPUT:", prompt)
    print("MODEL RESPONSE:", response)
    print("ATTACK SUCCESS:", "YES" if success else "NO")
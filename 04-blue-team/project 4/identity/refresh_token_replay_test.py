
import requests
import getpass
import json
from datetime import datetime, timezone

DOMAIN = "dev-ks7ulmlut6bjk3x7.us.auth0.com"

TOKEN_URL = f"https://{DOMAIN}/oauth/token"


def timestamp():
    return datetime.now(timezone.utc).isoformat()


def refresh_token_exchange(client_id, client_secret, refresh_token):

    response = requests.post(
        TOKEN_URL,
        data={
            "grant_type": "refresh_token",
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token
        },
        headers={
            "Content-Type": "application/x-www-form-urlencoded"
        },
        timeout=20
    )

    return response


print("=" * 65)
print(" SECURENOVA - REFRESH TOKEN ROTATION & REPLAY TEST")
print("=" * 65)

# Use Regular Web Application credentials, NOT M2M credentials.

client_id = input("Enter Regular Web App Client ID: ").strip()
client_secret = getpass.getpass("Enter current Regular Web App Client Secret: ")

rt1 = getpass.getpass("Paste your fresh RT1: ").strip()

if not client_id or not client_secret or not rt1:
    raise SystemExit("ERROR: Required credentials are missing.")

# --------------------------------------------------
# TEST 1: Exchange RT1 for RT2
# --------------------------------------------------

print(f"\n[{timestamp()}] TEST 1: Exchanging RT1...")

try:
    response1 = refresh_token_exchange(
        client_id,
        client_secret,
        rt1
    )

    if response1.status_code == 200:

        result1 = response1.json()

        rt2 = result1.get("refresh_token")

        print(f"[{timestamp()}] SUCCESS: RT1 exchange accepted.")
        print(f"[{timestamp()}] HTTP Status: {response1.status_code}")
        print(f"[{timestamp()}] Access token received: "
              f"{bool(result1.get('access_token'))}")
        print(f"[{timestamp()}] New RT2 received: {bool(rt2)}")

        if not rt2:
            print(
                "\nTEST INCOMPLETE: No RT2 returned. "
                "Check Auth0 refresh-token rotation settings."
            )
            raise SystemExit(1)

    else:
        print(f"[{timestamp()}] RT1 exchange failed.")
        print("HTTP Status:", response1.status_code)
        print("Auth0 Response:", response1.text)
        raise SystemExit(1)

except requests.RequestException as error:
    print(f"[{timestamp()}] Network error: {error}")
    raise SystemExit(1)


# --------------------------------------------------
# TEST 2: Replay old RT1
# --------------------------------------------------

print(f"\n[{timestamp()}] TEST 2: Replaying old RT1...")
print("Attempting to reuse the already-rotated token...")

try:
    response2 = refresh_token_exchange(
        client_id,
        client_secret,
        rt1
    )

    print(f"\n[{timestamp()}] Replay HTTP Status: "
          f"{response2.status_code}")

    if response2.status_code == 200:

        print("FAILED: Old RT1 was accepted!")
        print("Check Auth0 rotation and reuse detection settings.")

    else:

        error_data = response2.json()

        print(f"[{timestamp()}] SUCCESS: Old RT1 replay rejected!")
        print("Auth0 Error:", error_data.get("error"))
        print("Description:", error_data.get("error_description"))

        if error_data.get("error") == "invalid_grant":
            print(
                f"\n[{timestamp()}] CONFIRMED: "
                "Auth0 rejected the reused refresh token."
            )
        else:
            print(
                "\nReplay was rejected, but verify the error reason "
                "in Auth0 Logs before claiming reuse detection."
            )

except requests.RequestException as error:
    print(f"[{timestamp()}] Replay request error: {error}")

print("\n" + "=" * 65)
print(" REFRESH TOKEN ROTATION TEST COMPLETED")
print("=" * 65)

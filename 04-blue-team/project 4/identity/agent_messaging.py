import base64
from pathlib import Path

from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature

BASE = Path(__file__).resolve().parent

# Load private key
with open(BASE / "agent_private.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )

# Load public key
with open(BASE / "agent_public.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())


def sign_message(message):
    signature = private_key.sign(message.encode("utf-8"))

    return base64.b64encode(signature).decode("utf-8")


def verify_message(message, signature):
    try:
        decoded_signature = base64.b64decode(signature)

        public_key.verify(
            decoded_signature,
            message.encode("utf-8")
        )

        return True

    except (InvalidSignature, ValueError):
        return False


# Original outgoing message
original_message = (
    "Agent A: Request approval for a test operation."
)

signature = sign_message(original_message)

print("\nORIGINAL MESSAGE")
print(original_message)

print("\nSIGNATURE")
print(signature)

# Receiving agent verifies original message
if verify_message(original_message, signature):
    print("\nVALID MESSAGE: Signature verified.")
else:
    print("\nREJECTED: Signature verification failed.")

# Attacker changes one character
tampered_message = original_message.replace(
    "test operation",
    "admin operation"
)

print("\nTAMPERED MESSAGE")
print(tampered_message)

if verify_message(tampered_message, signature):
    print("VALID MESSAGE: Signature verified.")
else:
    print("REJECTED: Signature verification failed.")
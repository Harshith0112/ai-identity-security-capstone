from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization
from pathlib import Path

BASE = Path(__file__).resolve().parent

# Generate key pair
private_key = Ed25519PrivateKey.generate()
public_key = private_key.public_key()

# Save private key
private_path = BASE / "agent_private.pem"

with open(private_path, "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    )

# Save public key
public_path = BASE / "agent_public.pem"

with open(public_path, "wb") as f:
    f.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

print("EEd25519 key pair generated successfully using Python cryptography library.")
print("Private key:", private_path)
print("Public key:", public_path)
"""
  requires cryptography-39.0.0
"""
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Generate the public/private key pair.
# https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/#generation
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=4096,
)

# Save private key to a file.
with open("bin/privkey.pem", "wb") as file:
    file.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        )
    )

# Save public key to a file.
with open("bin/pubkey.pem", "wb") as file:
    file.write(
        private_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
    )

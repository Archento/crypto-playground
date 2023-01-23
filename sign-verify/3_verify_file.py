import base64
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key

# Load public key.
with open("sign-verify/bin/pubkey.pem", "rb") as file:
    public_key = load_pem_public_key(file.read())

# Load payload contents.
with open("README.md", "rb") as file:
    payload_contents = file.read()

# Load signature file.
with open("sign-verify/signature.sig", "rb") as file:
    signature = base64.b64decode(file.read())

# Perform verification.
try:
    public_key.verify(
        signature,
        payload_contents,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        hashes.SHA256(),
    )
except InvalidSignature as e:
    print("ERROR: Payload and/or signature files failed verification!")

print('verification successful')

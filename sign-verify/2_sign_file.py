import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding

# Load private key.
with open("bin/privkey.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
    )

# Load the contents of the file to be signed.
# -> can also be a message of any type, e.g. str
with open("../README.md", "rb") as file:
    payload = file.read()

# create signature file.
# (will be send together with payload for verification)
signature = base64.b64encode(
    private_key.sign(
        payload,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        hashes.SHA256(),
    )
)
with open("signature.sig", "wb") as file:
    file.write(signature)

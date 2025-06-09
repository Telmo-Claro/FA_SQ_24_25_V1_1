from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# made a key!
# do not run it again! unless you want a new key (older info will be lost forever)
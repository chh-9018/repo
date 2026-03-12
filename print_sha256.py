import hashlib
date = "2026-03-12"
username = "chh-9018"
s = f"{date}-{username}"
h = hashlib.sha256(s.encode()).hexdigest()
print(f'SHA256("{s}") = {h}')
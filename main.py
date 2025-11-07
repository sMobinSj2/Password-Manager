from genericpath import exists
import os
import json
from typing import Self
import pyperclip
from datetime import datetime, timezone


from Crypto.Cipher import AES, ChaCha20
from Crypto.PublicKey import RSA, 
    
now = datetime.now(timezone.utc)
pw = None

class Encryption:
    encryption_algorithms = {
        'RSA': RSA_func,
        'AES': AES,
        'ChaCha20': ChaCha20
    }
    
    def __init__(self, master_passweord, algorithm="RSA"):
        self.master_password = None
        self.algorithm = algorithm
    
        def encryption(pass_data):
            
        
    pass

class VaultDatabase:
    def __init__(self, vault_file="vault.json"):
        self.vault_file = vault_file
        # Ensure the vault file exists
        if not os.path.exists(self.vault_file):
            self._write({"credentials": []})
        
    def read(self):
        with open(self.vault_file, 'r') as file:
            return json.load(file)
        
    def _write(self, data):
        with open(self.vault_file, 'w') as file:
            json.dump(data, file, indent=4)
            
    def append(self, item):
        data = self._read()
        if "credentials" not in data:
            data["credentials"] = []
        data["credentials"].append(item)
        self._write(data)
        
    def load_all(self):
        data = self._read()
        return data.get("credentials", [])

    def find(self, website):
        all_creds = self.load_all()
        return [c for c in all_creds if c.get("website") == website]    
        
        
new_credentials = {
    "Wensite": "example.com",
    "Username": "user123",
    "Password": "P@ssw0rd!",
    "Created_At": now.isoformat(),
    "Note": "My example credentials"
}  

def password_strengh_ckeck(password: str) -> None: 
    #check for length
    if len(password) < 8:
        raise ValueError("Password must be at least 8 character.")
    # Checking to not start with number
    elif not password[0].isalpha():
        raise ValueError("Password should't start with number.")
    # Checking to not start with lowercase character
    elif password[0].islower():
        raise ValueError("Password shouldn't start with a lowercase letter.")
    # Checking for symbols
    elif not any(char in "!@#$%^&*()-+" for char in password):
        raise ValueError("Password must contain at least one special symbol (!@#$%^&*()-+).")
    else:
        print("Password strength is good.")
        pyperclip.copy(password)
        print("Password has been copied to clipboard.")
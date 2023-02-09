#!/bin/env python3
"""
Emulator for the CryptMaster 2001
https://lcamtuf.substack.com/p/afternoon-project-cryptmaster-2001
"""

import readline # Never used, but enables user friendly input editing

# Source: https://lcamtuf.substack.com/p/afternoon-project-cryptmaster-2001
crypt_key = [
    "NXKEDJTZRFCOWALQPIYGVUMBSH",
    "DSVAZRYNJIUQOHMTLFBPKCXWGE",
    "HSTUZJXAMFYRIONWVLBCDQPGKE",
    "PFEQCBUMZWNSHKXADYLVGTJORI",
    "NVZRFEPTUXLKYASGWDOHIBQJMC",
    "YCBTFEZPMKJQIRSHLNODWXUVAG",
    "RPGTFECXWLUJOYMBZAVDKSIHNQ",
    "ICBRWMUQAVTNFLXZHDYKGJEOSP",
    "WRFLUCHGPOXDVZJISBQYEMAKTN",
    "BAWIYRZUDNSVPJXMTFKQHLCOEG",
    "VKDCJSNOQEBYUGHXIWFZMARPLT"
]

def cryptchar(char, table):
    """
    Use a lookup table to encrypt a single charater
    """
    # Map the chartater to an index in the table
    # A: 0, B: 1, C: 3, etc
    charidx = ord(char.upper()) - ord("A")
    return table[charidx]

def crypt_string(string, key):
    """
    Encrypt a whole string using the key
    """
    if len(string) > len(key):
        print(f"Max lenght is {len(key)}! Truncating message to {len(key)}!")
        string = string[:len(key)]

    crypted = [cryptchar(char,crypt_key[place]) for (place, char) in enumerate(string)]
    return "".join(crypted)

print("Virtual CryptMaster 2001:")

while True:
    string = input("> ")
    crypted = crypt_string(string,crypt_key)
    if crypted:
        print(crypted)

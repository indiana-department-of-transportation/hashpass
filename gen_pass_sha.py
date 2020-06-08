#!/usr/bin/env python3
"""
This will encrypt a password the same way it is encrypted on our ubuntu
systems for use with e.g. the ansible user module. Use like so:

    /path/to/gen_pass_sha.py mypassword
"""

from passlib.hash import sha512_crypt


def encrypt(passwd: str) -> str:
    """Encrypts the password using 5000 rounds of sha512."""

    return sha512_crypt.using(rounds=5000).hash(passwd)


if __name__ == "__main__":
    passwd = input("Enter your password:")
    print(encrypt(passwd))

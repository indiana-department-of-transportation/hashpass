#!/usr/bin/env python3
"""
This will encrypt a password the same way it is encrypted on our ubuntu
systems for use with e.g. the ansible user module. Use like so:

    /path/to/gen_pass_sha.py mypassword
"""

import sys
from getpass import getpass
from passlib.hash import sha512_crypt


def encrypt(passwd: str) -> str:
    """Encrypts the password using 5000 rounds of sha512."""

    return sha512_crypt.using(rounds=5000).hash(passwd)


def main():
    """Main function for generating password hash."""

    fn = getpass
    if "--show" in sys.argv:
        fn = input

    passwd = fn("Enter your password: ")
    passwd2 = fn("Please re-enter to confirm: ")
    if passwd == passwd2:
        print(encrypt(passwd))
    else:
        print("Sorry, passwords don't match.")


if __name__ == "__main__":
    main()

# Paste your server.py from the previous exercise BELOW these functions (so they
# exist before main() runs), then call send_file from a new "download" branch in handle.

import hashlib
import os

FILES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "files")
CHUNK_SIZE = 65536


def find_file(name):
    # the path of name inside FILES, or None if there is no such file
    pass


def sha256_of(path):
    # hashlib.sha256(), fed CHUNK_SIZE bytes at a time; return .hexdigest()
    pass


def send_file(conn, path):
    # a file_info message (size + sha256), then the content in messages of up to CHUNK_SIZE bytes
    pass

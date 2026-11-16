"""Used by both server.py and client.py."""
import hashlib
import pathlib

CHUNK_SIZE = 65536


def sha256_of(path: pathlib.Path) -> str:
    # NEW: hashlib.sha256(), fed CHUNK_SIZE bytes of the file at a time; return .hexdigest()
    pass

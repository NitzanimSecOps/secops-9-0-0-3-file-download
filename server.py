"""The server: answers requests from clients.

Two kinds of functions:
  * BUILD A REPLY: take values, RETURN a dict. They never touch the socket.
        run_shell, find_file, file_info
  * TALK TO THE CLIENT: take conn first, SEND on it.
        send_chunks, handle, serve_client

"from 9.0.0.2": copy your code from the previous exercise into the function.
"NEW": write it.
"""
import json
import os
import socket
import subprocess

from file_utils import CHUNK_SIZE, sha256_of
from protocol import recv_msg, send_json, send_msg

PORT = 2405
COMMAND_TIMEOUT = 5
FILES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "files")


def error(message: str) -> dict:
    return {"type": "error", "message": message}


# ============================================================
#  BUILD A REPLY  (return a value, never send)
# ============================================================

def run_shell(cmd: str) -> dict:
    # from 9.0.0.2
    pass


def find_file(name: str) -> str | None:
    # NEW: the path of name inside FILES, or None if there is no such file
    pass


def file_info(path: str) -> dict:
    # NEW: {"type": "file_info", "size": <bytes>, "sha256": sha256_of(path)}
    pass


# ============================================================
#  TALK TO THE CLIENT  (conn first, send on it)
# ============================================================

def send_chunks(conn: socket.socket, path: str) -> None:
    # NEW: the content of path, read and sent CHUNK_SIZE bytes at a time (send_msg)
    pass


def handle(conn: socket.socket, data: bytes) -> None:
    # from 9.0.0.2, plus a "download" branch. Every branch sends exactly one reply:
    #   exec      -> send_json(conn, run_shell(cmd))
    #   download  -> path = find_file(name)
    #                no file -> send_json(conn, error("not found"))
    #                else    -> send_json(conn, file_info(path)), then send_chunks(conn, path)
    try:
        request = json.loads(data)
    except ValueError:                   # not JSON at all
        send_json(conn, error("bad request"))
        return
    pass


def serve_client(conn: socket.socket) -> None:
    # from 9.0.0.2
    pass


def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("127.0.0.1", PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                try:
                    serve_client(conn)
                except ConnectionError:  # the client vanished mid-message: wait for the next one
                    pass


if __name__ == "__main__":
    main()

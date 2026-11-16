"""The server: answers requests from clients.

Every function is marked:
  "from 9.0.0.2": copy your code from the previous exercise into the function.
  "NEW": write it.
"""
import pathlib
import socket
import subprocess

from file_utils import CHUNK_SIZE, sha256_of
from protocol import recv_json, send_json, send_msg

PORT = 2405
COMMAND_TIMEOUT = 5
FILES = pathlib.Path(__file__).resolve().parent / "files"


def run_command(cmd: str) -> dict:
    # from 9.0.0.2
    pass


def find_file(name: str) -> pathlib.Path | None:
    # NEW: the path of name inside FILES, or None if there is no such file
    pass


def file_info(path: pathlib.Path) -> dict | None:
    # NEW: {"type": "file_info", "size": <bytes>, "sha256": sha256_of(path)}, or None if there is no such file
    pass


def send_chunks(conn: socket.socket, path: pathlib.Path):
    # NEW: the content of path, read and sent CHUNK_SIZE bytes at a time (send_msg)
    pass


def handle_client(conn: socket.socket):
    # from 9.0.0.2, plus a "download" branch. Every request gets exactly one answer:
    #   exec      -> send_json(conn, run_command(cmd))
    #   download  -> path = find_file(name)
    #                no file -> {"type": "error", "message": "not found"}
    #                else    -> send_json(conn, file_info(path)), then send_chunks(conn, path)
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
                    handle_client(conn)
                except (BrokenPipeError, ConnectionResetError):  # the client vanished: wait for the next one
                    pass


if __name__ == "__main__":
    main()

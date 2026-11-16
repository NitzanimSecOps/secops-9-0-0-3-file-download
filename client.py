"""The client: sends requests to the server and reads the replies.

Every function is marked:
  "from 9.0.0.2": copy your code from the previous exercise into the function.
  "NEW": write it.
"""
import pathlib
import socket
import sys

from file_utils import sha256_of
from protocol import recv_json, recv_msg, send_json

PORT = 2405
DOWNLOADS = pathlib.Path("downloads")   # downloaded files go here, inside the current folder


def run_command(sock: socket.socket, cmd: str) -> dict | None:
    # from 9.0.0.2
    pass


def recv_chunks(sock: socket.socket, size: int, path: pathlib.Path) -> bool:
    # NEW: recv_msg until size bytes arrived, writing each chunk to path
    # True if all of them arrived, False if the connection closed first
    pass


def download(sock: socket.socket, name: str) -> int | None:
    # NEW: send {"type": "download", "path": name}, then read the reply:
    #   error     -> None
    #   file_info -> recv_chunks into DOWNLOADS/<last part of name>, then compare
    #                sha256_of(that file) with the sha256 the server sent
    # return the size, or None (and no file left in DOWNLOADS) on an error,
    # a wrong hash or a lost connection
    DOWNLOADS.mkdir(exist_ok=True)
    pass


def main() -> None:
    # from 9.0.0.2, plus: "download <name>" calls download and prints where it was saved
    pass


if __name__ == "__main__":
    main()

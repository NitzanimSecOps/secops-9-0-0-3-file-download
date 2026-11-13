"""The client: sends requests to the server and reads the replies.

  * TALK TO THE SERVER: take sock first.
        run_command, recv_chunks, download
  * main: the command loop the user types into.

"from 9.0.0.2": copy your code from the previous exercise into the function.
"NEW": write it.
"""
import os
import socket
import sys

from file_utils import sha256_of
from protocol import recv_json, recv_msg, send_json

PORT = 2405
DOWNLOADS = "downloads"   # downloaded files go here, inside the current folder


# ============================================================
#  TALK TO THE SERVER  (sock first)
# ============================================================

def run_command(sock: socket.socket, cmd: str) -> dict | None:
    # from 9.0.0.2
    pass


def recv_chunks(sock: socket.socket, size: int, path: str) -> bool:
    # NEW: recv_msg until size bytes arrived, writing each chunk to path
    # True if all of them arrived, False if the connection closed first
    received = 0
    with open(path, "wb") as f:
        while received < size:
            try:
                chunk = recv_msg(sock)
            except ConnectionError:      # the connection was cut: same as closed
                chunk = None
            # TODO: None -> return False; otherwise write it and count it
    return True


def download(sock: socket.socket, name: str) -> int | None:
    # NEW: send {"type": "download", "path": name}, then read the reply:
    #   error     -> None
    #   file_info -> recv_chunks into DOWNLOADS/<last part of name>, then compare
    #                sha256_of(that file) with the sha256 the server sent
    # return the size, or None (and no file left in DOWNLOADS) on an error,
    # a wrong hash or a lost connection
    os.makedirs(DOWNLOADS, exist_ok=True)
    path = os.path.join(DOWNLOADS, os.path.basename(name))
    pass


# ============================================================
#  THE COMMAND LOOP
# ============================================================

def main() -> None:
    try:
        sock = socket.create_connection(("127.0.0.1", PORT))
    except ConnectionRefusedError:
        print(f"no server on port {PORT}: start server.py first")
        return
    with sock:
        while True:
            # from 9.0.0.2, plus: "download <name>" calls download and prints where it was saved
            pass


if __name__ == "__main__":
    main()

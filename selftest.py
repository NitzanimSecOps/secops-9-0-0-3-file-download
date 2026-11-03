"""Local tester for server.py and client.py - not the hidden grader.

    python3 selftest.py

Creates a files/ folder with example files, starts your server.py in the background, and downloads
with your download. Change the examples and try your own.
"""
import os
import socket
import subprocess
import sys
import time

HOST = "127.0.0.1"
PORT = 2405


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    files = os.path.join(here, "files")
    os.makedirs(files, exist_ok=True)
    with open(os.path.join(files, "hello.txt"), "w") as f:
        f.write("meow\n")
    with open(os.path.join(files, "big.bin"), "wb") as f:
        f.write(bytes(range(256)) * 20000)

    server = subprocess.Popen([sys.executable, os.path.join(here, "server.py")], cwd=here)
    try:
        time.sleep(1)
        sys.path.insert(0, here)
        from client import download, run_command

        with socket.create_connection((HOST, PORT)) as s:
            s.settimeout(10)
            for name in ("hello.txt", "big.bin"):
                dest = os.path.join(here, "downloaded_" + name)
                count = download(s, name, dest)
                with open(os.path.join(files, name), "rb") as a:
                    original = a.read()
                same = os.path.exists(dest) and open(dest, "rb").read() == original
                print(name, "- returned", count, "- identical to the original:", same)
            print("missing file - returned", download(s, "nope.txt", os.path.join(here, "nope.txt")))
            print("../ - returned", download(s, "../server.py", os.path.join(here, "nope.txt")))
            print("still alive:", run_command(s, "echo yes"))
    finally:
        server.kill()


if __name__ == "__main__":
    main()

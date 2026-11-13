"""Local tester for server.py and client.py - not the hidden grader.

    python3 selftest.py

Creates a files/ folder with example files, starts your server.py in the background, and downloads
with your download. The downloads/ folder it makes is in a temporary folder, removed at the end, so
your own downloads/ stays untouched. Change the examples and try your own.
"""
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time

HOST = "127.0.0.1"
PORT = 2405


def port_is_taken():
    try:
        socket.create_connection((HOST, PORT), timeout=1).close()
        return True
    except OSError:
        return False


def main():
    if port_is_taken():
        print(f"Something (probably a server.py you started) is already listening on port {PORT}.")
        print("Stop it with Ctrl+C in its window, then run selftest.py again.")
        sys.exit(1)
    here = os.path.dirname(os.path.abspath(__file__))
    files = os.path.join(here, "files")
    os.makedirs(files, exist_ok=True)
    with open(os.path.join(files, "hello.txt"), "w") as f:
        f.write("meow\n")
    with open(os.path.join(files, "big.bin"), "wb") as f:
        f.write(bytes(range(256)) * 20000)

    work = tempfile.mkdtemp()  # download() saves into downloads/ under the current folder
    server = subprocess.Popen([sys.executable, os.path.join(here, "server.py")], cwd=here)
    try:
        time.sleep(1)
        if server.poll() is not None:
            print("server.py stopped right after starting (its error is printed above).")
            sys.exit(1)
        sys.path.insert(0, here)
        from client import download, run_command

        os.chdir(work)

        with socket.create_connection((HOST, PORT)) as s:
            s.settimeout(10)
            for name in ("hello.txt", "big.bin"):
                dest = os.path.join("downloads", name)
                count = download(s, name)
                with open(os.path.join(files, name), "rb") as a:
                    original = a.read()
                same = os.path.exists(dest) and open(dest, "rb").read() == original
                print(name, "- returned", count, "- identical to the original:", same)
            print("missing file - returned", download(s, "nope.txt"))
            print("still alive:", run_command(s, "echo yes"))
    finally:
        server.kill()
        os.chdir(here)
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    main()

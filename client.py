# Paste your client.py from the previous exercise BELOW these functions (so they
# exist before main() runs), then add "download <name>" to the command loop.


def receive_file(sock, size, dest):
    # recv_msg until size bytes arrived, writing each chunk to dest
    # return the sha256 hexdigest of what arrived, or None if the connection closed first
    pass


def download(sock, name, dest):
    # send the download request, read file_info, receive_file, compare the hash
    # return the size, or None (and no file left at dest) on an error, a wrong hash or a lost connection
    pass

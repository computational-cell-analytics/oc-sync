import os
import time
from owncloud import HTTPResponseError


def _sync_remote_folder(client, remote_src, local_dst, verbose):
    files = client.list(remote_src)
    for fi in files:
        name = fi.path
        src = os.path.join(remote_src, name).replace("//", "/")
        dst = os.path.join(local_dst, name.lstrip("/"))
        if fi.file_type == "file":
            if os.path.exists(dst):
                continue
            if verbose:
                print("Syncing file", src, "to", dst)
            os.makedirs(os.path.split(dst)[0], exist_ok=True)
            client.get_file(src, dst)
        elif fi.file_type == "dir":
            _sync_remote_folder(client, src, local_dst, verbose)
        else:
            raise RuntimeError(f"Unknown file type {fi.file_type}")


def sync_from_owncloud(client, remote_src, local_dst, verbose=True):
    _sync_remote_folder(client, remote_src, local_dst, verbose)


def oc_file_exists(client, path):
    try:
        client.file_info(path)
        return True
    except HTTPResponseError as e:
        if e.status_code == 404:
            return False
        else:
            raise e


def oc_makedirs(client, path):
    try:
        client.mkdir(path)
    except HTTPResponseError as e:
        if e.status_code == 405:  # Already exists.
            return
        raise e


def _sync_local_folder(client, local_src, remote_dst, verbose):
    files = os.listdir(local_src)
    for name in files:
        src = os.path.join(local_src, name)
        dst = os.path.join(remote_dst, name)

        if os.path.isfile(src):
            if oc_file_exists(client, dst):
                continue
            if verbose:
                print("Syncing file", src, "to", dst)
            oc_makedirs(client, os.path.split(dst)[0])
            client.put_file(dst, src)
            time.sleep(1)

        elif os.path.isdir(src):
            _sync_local_folder(client, src, os.path.join(remote_dst, name), verbose)


def sync_to_owncloud(client, local_src, remote_dst, verbose=True):
    _sync_local_folder(client, local_src, remote_dst, verbose)

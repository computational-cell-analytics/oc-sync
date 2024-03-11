import os


def _sync_remote_folder(client, remote_src, local_dst):
    files = client.list(remote_src)
    for fi in files:
        name = fi.path
        src = os.path.join(remote_src, name).replace("//", "/")
        dst = os.path.join(local_dst, name.lstrip("/"))
        if fi.file_type == "file":
            if os.path.exists(dst):
                continue
            print("Syncing file", src, "to", dst)
            os.makedirs(os.path.split(dst)[0], exist_ok=True)
            client.get_file(src, dst)
        elif fi.file_type == "dir":
            _sync_remote_folder(client, src, local_dst)
        else:
            raise RuntimeError(f"Unknown file type {fi.file_type}")


def sync_from_owncloud(client, remote_src, local_dst):
    _sync_remote_folder(client, remote_src, local_dst)


def sync_to_owncloud(client, local_src, remote_dst):
    raise NotImplementedError

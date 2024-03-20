import owncloud
from oc_sync import sync_from_owncloud, sync_to_owncloud

url = "https://owncloud.gwdg.de/index.php/s/7Uy4nHEzDT8mjnC"


def sync_from(oc):
    sync_from_owncloud(oc, "/", "slides")


def sync_to(oc):
    sync_to_owncloud(oc, "slides", "/")


def main():
    oc = owncloud.Client.from_public_link(url)
    # sync_from(oc)
    sync_to(oc)


main()

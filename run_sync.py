import owncloud
from oc_sync import sync_from_owncloud

url = "https://owncloud.gwdg.de/index.php/s/7Uy4nHEzDT8mjnC"

oc = owncloud.Client.from_public_link(url)

# li = oc.list("/")
# breakpoint()
# print(li)

sync_from_owncloud(oc, "/", "slides")

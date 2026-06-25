import requests
import json
import socket
import threading
import os

from anvpy.logger import *


CONFIG_DIR = os.path.join(
    os.path.expanduser("~"),
    ".anvpy"
)

CONFIG_FILE = os.path.join(
    CONFIG_DIR,
    "connection.json"
)

def get_ip():

    try:
        with open(CONFIG_FILE) as f:
            data = json.load(f)

        return data.get("ip")

    except:
        return None

def save_ip(ip):

    os.makedirs(
        CONFIG_DIR,
        exist_ok=True
    )

    with open(CONFIG_FILE, "w") as f:
        json.dump({
            "ip": ip
        }, f)

def is_phone(ip):

    try:
        r = requests.get(
            f"http://{ip}:5000/ping",
            timeout=1
        )

        data = r.json()

        return (
            data.get("status") == "ok" and
            data.get("service") == "anvpy"
        )

    except:
        return False

def scan_network():

    local_ip = socket.gethostbyname(
        socket.gethostname()
    )

    subnet = ".".join(
        local_ip.split(".")[:-1]
    )

    found_ip = None

    def check(ip):
        nonlocal found_ip

        if found_ip:
            return

        if is_phone(ip):
            found_ip = ip

    threads = []

    for i in range(1, 255):

        ip = f"{subnet}.{i}"

        t = threading.Thread(
            target=check,
            args=(ip,)
        )

        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return found_ip

def connect(ip=None, verbose=True):

    if ip is None:
        ip = get_ip()

    if ip and is_phone(ip):

        save_ip(ip)

        if verbose:
            log_ok(f"Connected to {ip}")

        return ip


    if ip:
        log_warn(
            f"Saved IP {ip} unavailable"
        )

    log_action("Searching for device...")

    found_ip = scan_network()

    if found_ip:

        save_ip(found_ip)

        log_ok(f"Connected to {found_ip}")

        return found_ip

    log_error("No device found")

    return None
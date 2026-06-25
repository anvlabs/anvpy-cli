import requests
import os

from anvpy.logger import *
from anvpy.utils import *
from anvpy.connection import *
from anvpy.run import *

def compute_diff(local_state, phone_state):

    to_upload = []
    to_delete = []

    for path, hash_value in local_state.items():

        if path not in phone_state:
            to_upload.append(path)

        elif phone_state[path] != hash_value:
            to_upload.append(path)

    for path in phone_state:

        if path not in local_state:
            to_delete.append(path)

    return to_upload, to_delete

def delete_files(ip, project, files):

    try:

        response = requests.post(
            f"http://{ip}:5000/delete",
            json={
                "project": project,
                "files": files
            },
            timeout=10
        )

        if response.status_code != 200:
            return False

        return True

    except Exception:

        return False

def get_phone_state(ip, project):

    try:
        response = requests.get(
            f"http://{ip}:5000/file_state",
            params={
                "project": project
            },
            timeout=5
        )

        if response.status_code != 200:

            log_error("Failed to get phone state")

            return None

        return response.json()

    except Exception as e:

        log_error("Failed to get phone state")

        return None

def upload_file(ip, project, folder, rel_path):

    full_path = os.path.join(
        folder,
        rel_path
    )

    try:

        with open(full_path, "rb") as f:

            files = {
                "file": f
            }

            data = {
                "project": project,
                "path": rel_path
            }

            response = requests.post(
                f"http://{ip}:5000/upload",
                files=files,
                data=data,
                timeout=30
            )

            data = response.json()

            if response.status_code != 200:

                log_error(
                    f"Upload failed: {rel_path}"
                )

                return None

            return data

    except Exception:

        log_error(
            f"Failed: {rel_path}"
        )

        return None

def scan_files(folder):

    files = {}

    for root, dirs, filenames in os.walk(folder):

        for filename in filenames:

            full_path = os.path.join(root, filename)

            rel_path = os.path.relpath(
                full_path,
                folder
            ).replace("\\", "/")

            files[rel_path] = get_file_hash(
                full_path
            )

    return files

def sync(folder, run_after=True):

    ip = connect(verbose=False)

    if not ip:
        log_error("Phone not found")
        return

    project = os.path.basename(
        os.path.abspath(folder)
    )

    log_action(
        f"Syncing project: {project}"
    )

    local_state = scan_files(folder)

    phone_state = get_phone_state(
        ip,
        project
    )

    if phone_state is None:
        log_error("Connection lost")
        return

    to_upload, to_delete = compute_diff(
    local_state,
    phone_state
    )

    if to_upload:

        log_action(
            f"Uploading {len(to_upload)} files"
        )

    if to_delete:

        log_action(
            f"Deleting {len(to_delete)} files"
        )

    for file in to_upload:

        result = upload_file(
            ip,
            project,
            folder,
            file
        )

        if result:
            log_ok(f"Uploaded: {file}")

    if to_delete:

        result = delete_files(
            ip,
            project,
            to_delete
        )

        if result:

            for file in to_delete:
                log_ok(f"Deleted: {file}")

        else:

            log_error("Delete failed")

    log_ok(
        f"Sync complete "
        f"(Uploaded: {len(to_upload)}, "
        f"Deleted: {len(to_delete)})"
    )

    if run_after:

        run_project(
            ip,
            project
        )
import requests
from anvpy.logger import *

def run_project(ip, project):

    try:

        log_action(
            f"Running project: {project}"
        )

        response = requests.post(
            f"http://{ip}:5000/run",
            json={
                "project": project
            },
            timeout=10
        )

        data = response.json()

        if response.status_code != 200:

            log_error(
                f"Failed to run project: {project}"
            )

            return None

        log_ok(
            f"Project started: {project}"
        )

        return data

    except Exception:

        log_error(
            f"Failed to contact device"
        )

        return None
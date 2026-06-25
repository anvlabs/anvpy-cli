import argparse
import os
from anvpy.sync import sync
from anvpy.logger import *


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "command",
        choices=["run"]
    )
    parser.add_argument("--path")

    args = parser.parse_args()

    if args.path:
        project_path = args.path
    else:
        project_path = os.getcwd()


    if args.command == "run":

        if not os.path.isdir(project_path):

            log_error(
                f'Project folder not found: "{project_path}"'
            )

            return

        main_file = os.path.join(
            project_path,
            "main.py"
        )

        if not os.path.isfile(main_file):

            log_error(
                "main.py not found"
            )

            return

        sync(project_path)

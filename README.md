<p align="center">
  <img src="anvpy/assets/icon.png" alt="AnvPy" width="130">
</p>

<h1 align="center">AnvPy CLI</h1>

<p align="center">
  Official command line toolkit for AnvPy development.
</p>

<p align="center">
  <img src="https://img.shields.io/pypi/v/anvpy?style=for-the-badge&logo=pypi&logoColor=white&color=3776AB" alt="PyPI">
  <img src="https://img.shields.io/pypi/pyversions/anvpy?style=for-the-badge&logo=python&logoColor=white&color=3776AB" alt="Python">
  <img src="https://img.shields.io/badge/OS-Cross%20Platform-34A853?style=for-the-badge&logo=gnubash&logoColor=white" alt="Cross Platform">
  <img src="https://img.shields.io/badge/License-MIT-D97706?style=for-the-badge&logo=bookstack&logoColor=white" alt="MIT">
  <img src="https://img.shields.io/badge/Release-Alpha-8B5CF6?style=for-the-badge&logo=github&logoColor=white" alt="Release">
</p>

<p align="center">

```bash
pip install anvpy
```

</p>

**AnvPy CLI** is the official command-line interface for **AnvPy (Android Versatile Python)**, a platform that enables developers to build and run Python applications on Android.

The CLI provides a seamless desktop development workflow by synchronizing your project from your computer to your Android device and launching it directly in the AnvPy application with a single command.

---

## Features

* One command project synchronization and execution
* Automatic device discovery on the local network
* Incremental synchronization using file hashing 
* Simple setup with automatic connection management

---

## Requirements

* Python 3.8 or later
* AnvPy installed on an Android device
* Computer and Android device connected to the same local network (same Wi-Fi network or mobile hotspot)

---

# Installation

Install directly from PyPI:

```bash
pip install anvpy
```

---

# Quick Start

Navigate to your project directory containing `main.py`:

```bash
cd MyProject
```

Run the project:

```bash
anvpy run
```

Or specify a project path:

```bash
anvpy run --path="C:\Projects\MyProject"
```

---

# Project Structure

AnvPy expects your project to contain a `main.py` entry point.

Example:

```text
MyProject/
├── main.py
├── assets/
├── images/
├── data/
└── ...
```

---

# How It Works

When you execute:

```bash
anvpy run
```

the CLI automatically:

1. Detects the project directory.
2. Verifies that `main.py` exists.
3. Connects to the AnvPy application running on your Android device.
4. Synchronizes only the files that have changed.
5. Removes files deleted from the Android project.
6. Launches the synchronized project automatically on the device.

---

# Example Output

```text
[ACTION] Connecting to device...
[OK] Connected to 192.168.1.5

[ACTION] Syncing project: MyProject
[OK] Uploaded: main.py
[OK] Uploaded: assets/logo.png
[OK] Deleted: assets/old_logo.png

[OK] Sync complete (Uploaded: 2, Deleted: 1)

[ACTION] Running project: MyProject
[OK] Project started
```

---

# License

This project is licensed under the MIT License.

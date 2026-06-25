class Color:
    RESET = "\033[0m"
    BLUE = "\033[94m"
    GREEN = "\033[38;5;46m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"


def log_info(msg):
    print(f"{Color.BLUE}[INFO]{Color.RESET} {msg}")


def log_ok(msg):
    print(f"{Color.GREEN}[OK]{Color.RESET} {msg}")


def log_warn(msg):
    print(f"{Color.YELLOW}[WARN]{Color.RESET} {msg}")


def log_error(msg):
    print(f"{Color.RED}[ERROR]{Color.RESET} {msg}")


def log_action(msg):
    print(f"{Color.CYAN}[ACTION]{Color.RESET} {msg}")
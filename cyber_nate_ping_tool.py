#!/usr/bin/env python3
# ============================================================
#   CYBER NATE — Information Gathering Tool (Ping Script)
#   MetBrains 7-Day Cyber Camp | Prof. Dimple Chauhan
#   Prepared by: OT Nathaniel
# ============================================================

import os
import platform
import subprocess
import sys
from datetime import datetime

# ── ANSI colour codes (work on Windows 10+ & Linux/Mac) ────
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BLUE   = "\033[94m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

# ── Banner ──────────────────────────────────────────────────
def print_banner():
    banner = f"""
{CYAN}{BOLD}
  ╔══════════════════════════════════════════════════════════╗
  ║         CYBER NATE — INFORMATION GATHERING TOOL          ║
  ║         MetBrains 7-Day Cyber Camp | Ping Script         ║
  ║         Prepared by: OT Nathaniel         ║
  ╚══════════════════════════════════════════════════════════╝
{RESET}"""
    print(banner)

# ── Detect OS ───────────────────────────────────────────────
def get_os():
    system = platform.system()
    return system  # "Windows", "Linux", "Darwin"

# ── Show available ping arguments ───────────────────────────
def show_ping_options(os_name):
    print(f"\n{YELLOW}{BOLD}Available Ping Arguments:{RESET}")
    print(f"{CYAN}{'─'*55}{RESET}")

    if os_name == "Windows":
        options = [
            ("-n <count>",   "Number of echo requests to send       (e.g. -n 4)"),
            ("-l <size>",    "Buffer size in bytes                   (e.g. -l 64)"),
            ("-t",           "Ping continuously until stopped (Ctrl+C)           "),
            ("-i <TTL>",     "Time To Live value                     (e.g. -i 64)"),
            ("-w <timeout>", "Timeout in milliseconds                (e.g. -w 1000)"),
            ("-a",           "Resolve address to hostname                         "),
            ("-f",           "Set Do Not Fragment flag in packet                  "),
        ]
    else:  # Linux / Mac
        options = [
            ("-c <count>",   "Number of packets to send             (e.g. -c 4)"),
            ("-s <size>",    "Packet size in bytes                   (e.g. -s 64)"),
            ("-i <interval>","Interval between packets in seconds   (e.g. -i 1)"),
            ("-t <TTL>",     "Time To Live value                     (e.g. -t 64)"),
            ("-W <timeout>", "Timeout in seconds                     (e.g. -W 3)"),
            ("-q",           "Quiet output — summary only                         "),
            ("-v",           "Verbose output                                      "),
        ]

    for arg, desc in options:
        print(f"  {GREEN}{BOLD}{arg:<18}{RESET}  {desc}")

    print(f"{CYAN}{'─'*55}{RESET}")

# ── Build & run the ping command ────────────────────────────
def run_ping(target, arguments, os_name):
    # Split user-supplied argument string into tokens
    arg_tokens = arguments.strip().split() if arguments.strip() else []

    if os_name == "Windows":
        cmd = ["ping"] + arg_tokens + [target]
    else:
        cmd = ["ping"] + arg_tokens + [target]

    cmd_str = " ".join(cmd)

    print(f"\n{BLUE}{BOLD}{'═'*55}{RESET}")
    print(f"{CYAN}  Target   : {YELLOW}{target}{RESET}")
    print(f"{CYAN}  Arguments: {YELLOW}{arguments if arguments.strip() else '(default)'}{RESET}")
    print(f"{CYAN}  OS       : {YELLOW}{os_name}{RESET}")
    print(f"{CYAN}  Command  : {YELLOW}{cmd_str}{RESET}")
    print(f"{CYAN}  Time     : {YELLOW}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{RESET}")
    print(f"{BLUE}{BOLD}{'═'*55}{RESET}\n")

    try:
        result = subprocess.run(
            cmd,
            capture_output=False,   # Stream output live to terminal
            text=True
        )
        print(f"\n{BLUE}{'─'*55}{RESET}")
        if result.returncode == 0:
            print(f"{GREEN}{BOLD}  [✔] Ping completed successfully.{RESET}")
        else:
            print(f"{RED}{BOLD}  [✘] Host unreachable or ping failed.{RESET}")
        print(f"{BLUE}{'─'*55}{RESET}")

    except FileNotFoundError:
        print(f"{RED}{BOLD}  [ERROR] 'ping' command not found on this system.{RESET}")
    except PermissionError:
        print(f"{RED}{BOLD}  [ERROR] Permission denied. Try running as Administrator/root.{RESET}")
    except KeyboardInterrupt:
        print(f"\n{YELLOW}{BOLD}  [!] Ping interrupted by user.{RESET}")

# ── Validate target domain / IP ─────────────────────────────
def validate_target(target):
    if not target or len(target.strip()) < 3:
        return False
    # Basic check — no spaces, has at least one dot or is an IP
    if " " in target:
        return False
    return True

# ── Main program ─────────────────────────────────────────────
def main():
    # Enable ANSI on Windows
    if get_os() == "Windows":
        os.system("color")

    print_banner()

    os_name = get_os()
    print(f"{GREEN}  [*] Detected Operating System: {BOLD}{os_name}{RESET}")

    # ── Get target ──────────────────────────────────────────
    print(f"\n{YELLOW}{BOLD}  STEP 1 — Enter Target{RESET}")
    while True:
        target = input(f"{CYAN}  Enter target domain or IP address (e.g. google.com): {RESET}").strip()
        if validate_target(target):
            break
        print(f"{RED}  [!] Invalid input. Please enter a valid domain or IP.{RESET}")

    # ── Show options ────────────────────────────────────────
    show_ping_options(os_name)

    # ── Get arguments ───────────────────────────────────────
    print(f"\n{YELLOW}{BOLD}  STEP 2 — Choose Ping Arguments{RESET}")

    if os_name == "Windows":
        default_arg = "-n 4"
        example     = "-n 4 -l 64"
    else:
        default_arg = "-c 4"
        example     = "-c 4 -s 64"

    print(f"{CYAN}  You can combine multiple arguments (e.g. {example})")
    print(f"  Press ENTER to use the default: {BOLD}{default_arg}{RESET}")

    arguments = input(f"{CYAN}  Enter ping argument(s): {RESET}").strip()
    if not arguments:
        arguments = default_arg
        print(f"{GREEN}  [*] Using default: {BOLD}{default_arg}{RESET}")

    # ── Run ping ────────────────────────────────────────────
    print(f"\n{YELLOW}{BOLD}  STEP 3 — Running Ping...{RESET}")
    run_ping(target, arguments, os_name)

    # ── Ask to run again ────────────────────────────────────
    print(f"\n{YELLOW}  Run another ping? (y/n): {RESET}", end="")
    again = input().strip().lower()
    if again == "y":
        main()
    else:
        print(f"\n{CYAN}{BOLD}  Thank you for using Cyber Nate's Info Gathering Tool!{RESET}")
        print(f"{CYAN}  — OT Nathaniel | MetBrains Cyber Camp 2026{RESET}\n")

# ── Entry point ──────────────────────────────────────────────
if __name__ == "__main__":
    main()

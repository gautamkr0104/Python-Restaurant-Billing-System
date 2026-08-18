#!/usr/bin/env python3
"""
Terminal UI helpers for the Restaurant Billing System.
"""

import os

from config import Colors


# ──────────────────────────────────────────────
#  Utility Helpers
# ──────────────────────────────────────────────
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input(f"\n{Colors.DIM}Press Enter to continue...{Colors.RESET}")


def fmt(amount):
    """Format currency value."""
    return f"₹{amount:,.2f}"


def print_header(title):
    width = 60
    print()
    print(f"{Colors.CYAN}{Colors.BOLD}{'═' * width}{Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}{title:^{width}}{Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}{'═' * width}{Colors.RESET}")
    print()


def print_divider(char="─", color=Colors.DIM):
    print(f"{color}{char * 60}{Colors.RESET}")


def veg_label(is_veg):
    if is_veg:
        return f"{Colors.GREEN}🟢 VEG{Colors.RESET}"
    return f"{Colors.RED}🔴 NON-VEG{Colors.RESET}"


def get_valid_input(prompt, input_type=str, valid=None, error_msg="Invalid input"):
    """Generic input validator."""
    while True:
        try:
            raw = input(prompt).strip()
            if not raw:
                continue
            value = input_type(raw)
            if valid and value not in valid:
                print(f"  {Colors.RED}✗ {error_msg}{Colors.RESET}")
                continue
            return value
        except (ValueError, TypeError):
            print(f"  {Colors.RED}✗ {error_msg}{Colors.RESET}")

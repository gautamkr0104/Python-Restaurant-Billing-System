#!/usr/bin/env python3
"""
Configuration constants for the Restaurant Billing System.
"""

# ──────────────────────────────────────────────
#  ANSI Color Codes for Terminal Styling
# ──────────────────────────────────────────────
class Colors:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    UNDERLINE = "\033[4m"

    RED     = "\033[31m"
    GREEN   = "\033[32m"
    YELLOW  = "\033[33m"
    BLUE    = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN    = "\033[36m"
    WHITE   = "\033[37m"

    BG_RED    = "\033[41m"
    BG_GREEN  = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE   = "\033[44m"
    BG_CYAN   = "\033[46m"


# ──────────────────────────────────────────────
#  Discount Codes: code -> percentage off
# ──────────────────────────────────────────────
DISCOUNT_CODES = {
    "WELCOME10":  10,
    "SAVE20":     20,
    "FLAT50":     50,
    "STUDENT":    15,
    "VIP":        25,
}

# ──────────────────────────────────────────────
#  Tax & Service Charge Rates
# ──────────────────────────────────────────────
TAX_RATE = 0.05           # 5% GST
SERVICE_CHARGE_RATE = 0.10  # 10% service charge

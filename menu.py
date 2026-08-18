#!/usr/bin/env python3
"""
Menu database for the Restaurant Billing System.
"""

from collections import OrderedDict


# ──────────────────────────────────────────────
#  Menu Database
# ──────────────────────────────────────────────
MENU = OrderedDict({
    "🍟 Appetizers & Starters": {
        "spring rolls":       {"price": 120, "veg": True},
        "garlic bread":       {"price": 90,  "veg": True},
        "chicken wings":      {"price": 180, "veg": False},
        "bruschetta":         {"price": 100, "veg": True},
    },
    "🍕 Main Course": {
        "margherita pizza":   {"price": 250, "veg": True},
        "pepperoni pizza":    {"price": 300, "veg": False},
        "pasta carbonara":    {"price": 220, "veg": False},
        "grilled chicken":    {"price": 280, "veg": False},
        "paneer tikka":       {"price": 200, "veg": True},
        "butter chicken":     {"price": 320, "veg": False},
        "veg biryani":        {"price": 180, "veg": True},
        "chicken biryani":    {"price": 250, "veg": False},
    },
    "🍔 Burgers & Sandwiches": {
        "classic burger":     {"price": 150, "veg": False},
        "veggie burger":      {"price": 130, "veg": True},
        "club sandwich":      {"price": 170, "veg": False},
        "grilled cheese":     {"price": 110, "veg": True},
    },
    "🥗 Salads & Soups": {
        "caesar salad":       {"price": 140, "veg": False},
        "greek salad":        {"price": 130, "veg": True},
        "tomato soup":        {"price": 90,  "veg": True},
        "corn soup":          {"price": 80,  "veg": True},
    },
    "🍰 Desserts": {
        "chocolate cake":     {"price": 180, "veg": True},
        "cheesecake":         {"price": 200, "veg": True},
        "ice cream sundae":   {"price": 120, "veg": True},
        "gulab jamun":        {"price": 80,  "veg": True},
    },
    "☕ Beverages": {
        "espresso":           {"price": 90,  "veg": True},
        "cappuccino":         {"price": 110, "veg": True},
        "fresh lime soda":    {"price": 60,  "veg": True},
        "mango shake":        {"price": 80,  "veg": True},
        "iced tea":           {"price": 70,  "veg": True},
        "water bottle":       {"price": 30,  "veg": True},
    },
})

# Flat lookup dict for quick search by name
FLAT_MENU = {}
for category, items in MENU.items():
    for item_name, item_info in items.items():
        FLAT_MENU[item_name] = {**item_info, "category": category}

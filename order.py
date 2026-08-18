#!/usr/bin/env python3
"""
Order management for the Restaurant Billing System.
"""

import datetime

from config import DISCOUNT_CODES, TAX_RATE, SERVICE_CHARGE_RATE


class OrderItem:
    """Represents a single item in an order."""

    def __init__(self, name, price, quantity, is_veg):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.is_veg = is_veg

    @property
    def total(self):
        return self.price * self.quantity

    def __repr__(self):
        return f"OrderItem({self.name!r}, qty={self.quantity})"


class Order:
    """Manages an order's items, calculations, and state."""

    def __init__(self, table_number):
        self.table_number = table_number
        self.items: list[OrderItem] = []
        self.discount_code = None
        self.discount_percent = 0
        self.timestamp = datetime.datetime.now()

    def add_item(self, name, price, quantity, is_veg):
        """Add an item or increase its quantity if already ordered."""
        for item in self.items:
            if item.name == name:
                item.quantity += quantity
                return
        self.items.append(OrderItem(name, price, quantity, is_veg))

    def remove_item(self, index):
        """Remove an item by its list index (0-based)."""
        if 0 <= index < len(self.items):
            return self.items.pop(index)
        return None

    def apply_discount(self, code):
        """Apply a discount code. Returns True on success."""
        code_upper = code.upper()
        if code_upper in DISCOUNT_CODES:
            self.discount_code = code_upper
            self.discount_percent = DISCOUNT_CODES[code_upper]
            return True
        return False

    @property
    def subtotal(self):
        return sum(item.total for item in self.items)

    @property
    def discount_amount(self):
        return self.subtotal * (self.discount_percent / 100)

    @property
    def after_discount(self):
        return self.subtotal - self.discount_amount

    @property
    def tax(self):
        return self.after_discount * TAX_RATE

    @property
    def service_charge(self):
        return self.after_discount * SERVICE_CHARGE_RATE

    @property
    def grand_total(self):
        return self.after_discount + self.tax + self.service_charge

    def is_empty(self):
        return len(self.items) == 0

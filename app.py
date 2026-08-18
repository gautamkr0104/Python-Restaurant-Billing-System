#!/usr/bin/env python3
"""
🍽️  Python Restaurant Billing System
A feature-rich terminal-based restaurant billing application.

Entry point — run this file to start the application.
"""

import sys

from config import Colors
from menu import MENU, FLAT_MENU
from order import Order
from ui import (
    clear_screen, pause, fmt, print_header,
    print_divider, veg_label, get_valid_input,
)


class RestaurantApp:
    """Main application controller that orchestrates the restaurant flow."""

    def __init__(self):
        self.order_history: list[dict] = []

    # ─── Banner ───────────────────────────────
    def show_banner(self):
        clear_screen()
        banner = f"""
{Colors.CYAN}{Colors.BOLD}
    ╔══════════════════════════════════════════════════════╗
    ║                                                      ║
    ║        🍽️  PYTHON RESTAURANT  🍽️                    ║
    ║                                                      ║
    ║        Where Code Meets Cuisine                      ║
    ║                                                      ║
    ╚══════════════════════════════════════════════════════╝
{Colors.RESET}"""
        print(banner)

    # ─── Menu Display ─────────────────────────
    def show_menu(self):
        print_header("📋  OUR MENU")
        for category, items in MENU.items():
            print(f"  {Colors.BOLD}{Colors.YELLOW}{category}{Colors.RESET}")
            print(f"  {Colors.DIM}{'─' * 42}{Colors.RESET}")
            for idx, (name, info) in enumerate(items.items(), 1):
                veg = veg_label(info['veg'])
                price_str = fmt(info['price'])
                print(f"    {Colors.CYAN}{name:<22}{Colors.RESET}  {price_str:>8}   {veg}")
            print()

    # ─── Table Selection ──────────────────────
    def get_table_number(self):
        print(f"  {Colors.BOLD}Table Number:{Colors.RESET}")
        print(f"    {Colors.DIM}Enter a number (1-50) or 'walk-in' for takeaway{Colors.RESET}")
        while True:
            raw = input(f"  {Colors.CYAN}→ {Colors.RESET}").strip().lower()
            if raw == "walk-in":
                return "WALK-IN"
            try:
                num = int(raw)
                if 1 <= num <= 50:
                    return f"#{num}"
                print(f"    {Colors.RED}✗ Please enter a number between 1 and 50.{Colors.RESET}")
            except ValueError:
                print(f"    {Colors.RED}✗ Invalid input. Enter a number or 'walk-in'.{Colors.RESET}")

    # ─── Search ───────────────────────────────
    def search_menu(self, query):
        query_lower = query.lower()
        results = []
        for name, info in FLAT_MENU.items():
            if query_lower in name:
                results.append((name, info))
        return results

    # ─── Adding Items ─────────────────────────
    def add_items_to_order(self, order: Order):
        while True:
            print(f"\n  {Colors.BOLD}Add an item:{Colors.RESET}")
            print(f"    {Colors.DIM}Type item name, 'search <query>' to find, or 'done' to finish{Colors.RESET}")
            user_input = input(f"  {Colors.CYAN}→ {Colors.RESET}").strip().lower()

            if user_input == "done":
                if order.is_empty():
                    print(f"  {Colors.YELLOW}⚠ Your order is empty!{Colors.RESET}")
                    continue
                break

            # Search mode
            if user_input.startswith("search "):
                query = user_input[7:].strip()
                results = self.search_menu(query)
                if not results:
                    print(f"  {Colors.RED}✗ No items found matching '{query}'.{Colors.RESET}")
                else:
                    print(f"\n  {Colors.GREEN}Found {len(results)} item(s):{Colors.RESET}")
                    for idx, (name, info) in enumerate(results, 1):
                        print(f"    {idx}. {name:<22} {fmt(info['price']):>8}   {veg_label(info['veg'])}")
                continue

            # Direct item name
            if user_input in FLAT_MENU:
                item_info = FLAT_MENU[user_input]
                qty = get_valid_input(
                    f"  Quantity for {Colors.CYAN}{user_input}{Colors.RESET}: ",
                    input_type=int,
                    valid=range(1, 100),
                    error_msg="Enter a valid quantity (1-99)."
                )
                order.add_item(user_input, item_info['price'], qty, item_info['veg'])
                print(f"  {Colors.GREEN}✓ Added {qty}x {user_input} — {fmt(item_info['price'] * qty)}{Colors.RESET}")
            else:
                print(f"  {Colors.RED}✗ Item '{user_input}' not found. Try 'search {user_input}' or check the menu.{Colors.RESET}")

    # ─── View Order ───────────────────────────
    def view_current_order(self, order: Order):
        if order.is_empty():
            print(f"\n  {Colors.YELLOW}⚠ No items in order yet.{Colors.RESET}")
            return

        print_header(f"📋  YOUR ORDER  —  Table {order.table_number}")
        print(f"  {Colors.DIM}{'Item':<22} {'Qty':>4} {'Price':>8} {'Total':>10}{Colors.RESET}")
        print_divider()

        for idx, item in enumerate(order.items, 1):
            print(f"  {idx}. {item.name:<20} {item.quantity:>4} {fmt(item.price):>8} {fmt(item.total):>10}")

        print_divider()
        print(f"  {Colors.BOLD}Subtotal:{Colors.RESET:>38} {fmt(order.subtotal):>10}")
        if order.discount_percent > 0:
            print(f"  {Colors.GREEN}Discount ({order.discount_code}):{Colors.RESET:>30} -{fmt(order.discount_amount):>9}")
        print(f"  {Colors.DIM}GST (5%):{Colors.RESET:>38} {fmt(order.tax):>10}")
        print(f"  {Colors.DIM}Service Charge (10%):{Colors.RESET:>28} {fmt(order.service_charge):>10}")
        print_divider("═", Colors.CYAN)
        print(f"  {Colors.BOLD}{Colors.CYAN}GRAND TOTAL:{Colors.RESET:>35} {Colors.BOLD}{fmt(order.grand_total):>10}{Colors.RESET}")
        print()

    # ─── Modify Order ─────────────────────────
    def modify_order(self, order: Order):
        if order.is_empty():
            print(f"\n  {Colors.YELLOW}⚠ No items to modify.{Colors.RESET}")
            return

        self.view_current_order(order)
        choice = get_valid_input(
            f"  {Colors.YELLOW}Remove which item number? (or 'cancel'): {Colors.RESET}",
            input_type=str
        )
        if choice.lower() == "cancel":
            return
        try:
            idx = int(choice) - 1
            removed = order.remove_item(idx)
            if removed:
                print(f"  {Colors.GREEN}✓ Removed {removed.name} from order.{Colors.RESET}")
            else:
                print(f"  {Colors.RED}✗ Invalid item number.{Colors.RESET}")
        except ValueError:
            print(f"  {Colors.RED}✗ Invalid input.{Colors.RESET}")

    # ─── Discount ─────────────────────────────
    def apply_discount(self, order: Order):
        from config import DISCOUNT_CODES

        print(f"\n  {Colors.BOLD}Apply Discount Code{Colors.RESET}")
        print(f"  {Colors.DIM}Available codes: {', '.join(DISCOUNT_CODES.keys())}{Colors.RESET}")
        code = input(f"  {Colors.CYAN}→ Enter code: {Colors.RESET}").strip()
        if not code:
            return
        if order.apply_discount(code):
            print(f"  {Colors.GREEN}✓ Discount of {order.discount_percent}% applied!{Colors.RESET}")
        else:
            print(f"  {Colors.RED}✗ Invalid discount code.{Colors.RESET}")

    # ─── Payment ──────────────────────────────
    def process_payment(self, order: Order):
        print_header("💳  PAYMENT")
        print(f"  {Colors.BOLD}Amount Due: {Colors.CYAN}{fmt(order.grand_total)}{Colors.RESET}")
        print()
        print(f"  {Colors.BOLD}Payment Methods:{Colors.RESET}")
        print(f"    1. 💵 Cash")
        print(f"    2. 💳 Card (Credit/Debit)")
        print(f"    3. 📱 UPI / Digital Wallet")
        print(f"    4. 🔄 Split Bill")

        method = get_valid_input(
            f"\n  {Colors.CYAN}→ Choose method (1-4): {Colors.RESET}",
            input_type=int,
            valid=range(1, 5),
            error_msg="Select a valid option (1-4)."
        )

        method_names = {1: "Cash", 2: "Card", 3: "UPI", 4: "Split Bill"}
        selected = method_names[method]

        if method == 1:  # Cash
            while True:
                amount = get_valid_input(
                    f"  {Colors.CYAN}→ Cash received: ₹{Colors.RESET}",
                    input_type=float,
                    error_msg="Enter a valid amount."
                )
                if amount >= order.grand_total:
                    change = amount - order.grand_total
                    if change > 0:
                        print(f"  {Colors.GREEN}Change to return: {fmt(change)}{Colors.RESET}")
                    print(f"  {Colors.GREEN}✓ Payment received!{Colors.RESET}")
                    break
                else:
                    print(f"  {Colors.RED}✗ Insufficient amount. Need {fmt(order.grand_total - amount)} more.{Colors.RESET}")

        elif method == 4:  # Split
            people = get_valid_input(
                f"  {Colors.CYAN}→ Split among how many people? {Colors.RESET}",
                input_type=int,
                valid=range(2, 51),
                error_msg="Enter a number between 2 and 50."
            )
            per_person = order.grand_total / people
            print(f"\n  {Colors.GREEN}Each person pays: {fmt(per_person)}{Colors.RESET}")

        else:
            print(f"  {Colors.GREEN}✓ {selected} payment of {fmt(order.grand_total)} confirmed!{Colors.RESET}")

        return selected

    # ─── Receipt ──────────────────────────────
    def print_receipt(self, order: Order, payment_method: str):
        clear_screen()
        print_header("🧾  RECEIPT")

        receipt_lines = []
        receipt_lines.append("=" * 52)
        receipt_lines.append(f"{'PYTHON RESTAURANT':^52}")
        receipt_lines.append(f"{'Where Code Meets Cuisine':^52}")
        receipt_lines.append("=" * 52)
        receipt_lines.append(f"  Date:   {order.timestamp.strftime('%d %B %Y, %I:%M %p')}")
        receipt_lines.append(f"  Table:  {order.table_number}")
        receipt_lines.append(f"  Payment: {payment_method}")
        receipt_lines.append("-" * 52)
        receipt_lines.append(f"  {'Item':<20} {'Qty':>4} {'Amount':>10}")
        receipt_lines.append("-" * 52)

        for item in order.items:
            receipt_lines.append(f"  {item.name:<20} {item.quantity:>4} {fmt(item.total):>10}")

        receipt_lines.append("-" * 52)
        receipt_lines.append(f"  {'Subtotal:':<30} {fmt(order.subtotal):>10}")

        if order.discount_percent > 0:
            receipt_lines.append(f"  {'Discount (' + order.discount_code + '):':<30} -{fmt(order.discount_amount):>9}")

        receipt_lines.append(f"  {'GST (5%):':<30} {fmt(order.tax):>10}")
        receipt_lines.append(f"  {'Service Charge (10%):':<30} {fmt(order.service_charge):>10}")
        receipt_lines.append("=" * 52)
        receipt_lines.append(f"  {'GRAND TOTAL:':<30} {Colors.BOLD}{fmt(order.grand_total):>10}{Colors.RESET}")
        receipt_lines.append("=" * 52)
        receipt_lines.append("")
        receipt_lines.append(f"{'Thank you for dining with us! 🙏':^52}")
        receipt_lines.append(f"{'Visit us at pythonrestaurant.com':^52}")

        for line in receipt_lines:
            print(f"  {line}")

        # Save receipt to file
        receipt_filename = f"receipt_{order.timestamp.strftime('%Y%m%d_%H%M%S')}.txt"
        plain_lines = []
        for item in order.items:
            plain_lines.append(f"  {item.name:<20} {item.quantity:>4} ₹{item.total:>8.2f}")

        receipt_text = f"""
{'=' * 52}
{'PYTHON RESTAURANT':^52}
{'Where Code Meets Cuisine':^52}
{'=' * 52}
  Date:    {order.timestamp.strftime('%d %B %Y, %I:%M %p')}
  Table:   {order.table_number}
  Payment: {payment_method}
{'-' * 52}
  {'Item':<20} {'Qty':>4} {'Amount':>10}
{'-' * 52}
{chr(10).join(plain_lines)}
{'-' * 52}
  {'Subtotal:':<30} ₹{order.subtotal:>8.2f}
"""
        if order.discount_percent > 0:
            receipt_text += f"  {'Discount (' + order.discount_code + '):':<30} -₹{order.discount_amount:>7.2f}\n"
        receipt_text += f"""  {'GST (5%):':<30} ₹{order.tax:>8.2f}
  {'Service Charge (10%):':<30} ₹{order.service_charge:>8.2f}
{'=' * 52}
  {'GRAND TOTAL:':<30} ₹{order.grand_total:>8.2f}
{'=' * 52}

{'Thank you for dining with us!':^52}
"""

        try:
            with open(receipt_filename, "w") as f:
                f.write(receipt_text)
            print(f"\n  {Colors.DIM}Receipt saved to: {receipt_filename}{Colors.RESET}")
        except IOError:
            print(f"\n  {Colors.YELLOW}⚠ Could not save receipt to file.{Colors.RESET}")

    # ─── New Order Flow ───────────────────────
    def start_new_order(self):
        clear_screen()
        print_header("🆕  NEW ORDER")
        table = self.get_table_number()
        order = Order(table)

        print(f"\n  {Colors.GREEN}✓ Order started for Table {table}{Colors.RESET}")
        self.show_menu()
        self.add_items_to_order(order)

        # Main order loop
        while True:
            print(f"\n  {Colors.BOLD}{Colors.CYAN}What would you like to do?{Colors.RESET}")
            print(f"    1. ➕ Add more items")
            print(f"    2. 👁️  View order")
            print(f"    3. ✏️  Modify order (remove item)")
            print(f"    4. 🏷️  Apply discount code")
            print(f"    5. 💳 Proceed to payment")
            print(f"    6. ❌ Cancel order")

            choice = get_valid_input(
                f"\n  {Colors.CYAN}→ Choose (1-6): {Colors.RESET}",
                input_type=int,
                valid=range(1, 7),
                error_msg="Select a valid option (1-6)."
            )

            if choice == 1:
                self.add_items_to_order(order)
            elif choice == 2:
                self.view_current_order(order)
            elif choice == 3:
                self.modify_order(order)
            elif choice == 4:
                self.apply_discount(order)
            elif choice == 5:
                if order.is_empty():
                    print(f"  {Colors.YELLOW}⚠ Add items before proceeding to payment.{Colors.RESET}")
                    continue
                self.view_current_order(order)
                confirm = get_valid_input(
                    f"  {Colors.CYAN}→ Confirm order? (yes/no): {Colors.RESET}",
                    input_type=str,
                    valid=["yes", "no", "y", "n"],
                    error_msg="Enter 'yes' or 'no'."
                )
                if confirm in ("yes", "y"):
                    payment_method = self.process_payment(order)
                    self.print_receipt(order, payment_method)
                    # Save to history
                    self.order_history.append({
                        "table": order.table_number,
                        "total": order.grand_total,
                        "items": len(order.items),
                        "time": order.timestamp,
                        "payment": payment_method,
                    })
                    pause()
                    break
            elif choice == 6:
                cancel = get_valid_input(
                    f"  {Colors.RED}→ Are you sure? (yes/no): {Colors.RESET}",
                    input_type=str,
                    valid=["yes", "no", "y", "n"],
                    error_msg="Enter 'yes' or 'no'."
                )
                if cancel in ("yes", "y"):
                    print(f"  {Colors.YELLOW}Order cancelled.{Colors.RESET}")
                    break

    # ─── Order History ────────────────────────
    def view_order_history(self):
        if not self.order_history:
            print(f"\n  {Colors.YELLOW}⚠ No order history yet.{Colors.RESET}")
            return

        print_header("📊  ORDER HISTORY")
        print(f"  {Colors.DIM}{'#':<4} {'Table':<10} {'Items':>6} {'Total':>12} {'Payment':<10} {'Time'}{Colors.RESET}")
        print_divider()

        for idx, record in enumerate(self.order_history, 1):
            time_str = record['time'].strftime('%I:%M %p')
            print(f"  {idx:<4} {record['table']:<10} {record['items']:>6} {fmt(record['total']):>12} {record['payment']:<10} {time_str}")

        total_revenue = sum(r['total'] for r in self.order_history)
        print_divider("═", Colors.CYAN)
        print(f"  {Colors.BOLD}Total Orders: {len(self.order_history)}  |  Total Revenue: {fmt(total_revenue)}{Colors.RESET}")

    # ─── Main Loop ────────────────────────────
    def run(self):
        """Main application loop."""
        self.show_banner()

        while True:
            print(f"\n  {Colors.BOLD}{Colors.CYAN}Main Menu{Colors.RESET}")
            print(f"    1. 🍽️  Start New Order")
            print(f"    2. 📋  View Menu")
            print(f"    3. 📊  Order History")
            print(f"    4. 🚪  Exit")

            choice = get_valid_input(
                f"\n  {Colors.CYAN}→ Choose (1-4): {Colors.RESET}",
                input_type=int,
                valid=range(1, 5),
                error_msg="Select a valid option (1-4)."
            )

            if choice == 1:
                self.start_new_order()
            elif choice == 2:
                clear_screen()
                print_header("📋  FULL MENU")
                self.show_menu()
                pause()
            elif choice == 3:
                clear_screen()
                self.view_order_history()
                pause()
            elif choice == 4:
                clear_screen()
                print(f"""
{Colors.CYAN}{Colors.BOLD}
    ╔══════════════════════════════════════════════════════╗
    ║                                                      ║
    ║     Thank you for using Python Restaurant! 🍽️       ║
    ║     See you next time! 👋                            ║
    ║                                                      ║
    ╚══════════════════════════════════════════════════════╝
{Colors.RESET}""")
                sys.exit(0)


# ──────────────────────────────────────────────
#  Entry Point
# ──────────────────────────────────────────────
if __name__ == "__main__":
    try:
        app = RestaurantApp()
        app.run()
    except KeyboardInterrupt:
        print(f"\n\n  {Colors.YELLOW}Session ended. Goodbye! 👋{Colors.RESET}\n")
        sys.exit(0)
    except EOFError:
        print(f"\n\n  {Colors.YELLOW}Session ended. Goodbye! 👋{Colors.RESET}\n")
        sys.exit(0)

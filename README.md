# 🍽️ Python Restaurant Billing System

A feature-rich, terminal-based restaurant billing application built entirely in Python. Manage orders, apply discounts, calculate taxes, and generate professional receipts — all from the command line.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🍔 **Categorized Menu** | 30 items across 6 categories with VEG/NON-VEG indicators |
| 🔢 **Quantity Support** | Order multiple quantities of any item |
| 🔍 **Menu Search** | Find items instantly with built-in search |
| 💰 **Tax & Charges** | Automatic GST (5%) and service charge (10%) calculation |
| 🏷️ **Discount Codes** | Apply coupon codes for instant savings |
| 🧾 **Formatted Receipts** | Professional receipts saved as text files |
| 🎨 **Colorful Terminal UI** | ANSI-powered colorful and styled output |
| 💳 **Multiple Payment Methods** | Cash, Card, UPI, and Split Bill support |
| 📊 **Order History** | Track all orders with revenue summary |
| 🛡️ **Input Validation** | Robust error handling for all user inputs |
| 🪑 **Table Management** | Support for tables 1-50 or walk-in orders |
| ✏️ **Order Modification** | Add, remove, or view items before payment |

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.8** or higher
- No external libraries required (uses only the standard library)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Python-Restaurant-Billing-System.git

# Navigate to the project directory
cd Python-Restaurant-Billing-System

# Run the application
python app.py
```

### Alternative — Run the legacy single-file version

```bash
python "Python Restaurant Billing System.py"
```

---

## 📖 How It Works

### 1. Start the Application

```
    ╔══════════════════════════════════════════════════════╗
    ║        🍽️  PYTHON RESTAURANT  🍽️                    ║
    ║        Where Code Meets Cuisine                      ║
    ╚══════════════════════════════════════════════════════╝
```

### 2. Select Table & Browse Menu

- Choose a table number (1–50) or enter `walk-in` for takeaway
- Browse the full categorized menu with prices and VEG/NON-VEG tags

### 3. Add Items to Order

- **Direct entry:** Type the item name (e.g., `butter chicken`)
- **Search:** Type `search <query>` (e.g., `search pizza`)
- **Quantity:** Enter how many you want (1–99)
- Type `done` when finished adding items

### 4. Manage Your Order

| Option | Action |
|---|---|
| ➕ Add more | Go back to adding items |
| 👁️ View order | See full order summary with totals |
| ✏️ Modify order | Remove items by number |
| 🏷️ Discount | Apply a coupon code |
| 💳 Payment | Proceed to checkout |
| ❌ Cancel | Cancel the entire order |

### 5. Payment & Receipt

- Choose from **Cash**, **Card**, **UPI**, or **Split Bill**
- A formatted receipt is displayed and automatically saved as a `.txt` file

---

## 🏷️ Discount Codes

| Code | Discount |
|---|---|
| `WELCOME10` | 10% off |
| `STUDENT` | 15% off |
| `SAVE20` | 20% off |
| `VIP` | 25% off |
| `FLAT50` | 50% off |

---

## 📂 Project Structure

```
Python-Restaurant-Billing-System/
├── app.py                              # Main application controller & entry point
├── config.py                           # Constants: Colors, tax rates, discount codes
├── menu.py                             # Menu database (MENU, FLAT_MENU)
├── order.py                            # Order and OrderItem classes
├── ui.py                               # Terminal UI helpers & input validation
├── Python Restaurant Billing System.py # Legacy single-file version
├── README.md                           # Project documentation
├── receipt_*.txt                       # Auto-generated receipts
└── .gitignore
```

---

## 🏗️ Architecture

The application is organized into focused modules:

```
app.py              # Main application controller (entry point)
├── RestaurantApp   # Orchestrates menu, ordering, payment, receipts
│
config.py           # Shared configuration
├── Colors          # ANSI terminal styling constants
├── DISCOUNT_CODES  # Available coupon codes
├── TAX_RATE        # GST rate (5%)
└── SERVICE_CHARGE_RATE  # Service charge rate (10%)
│
menu.py             # Menu data
├── MENU            # Categorized menu database
└── FLAT_MENU       # Flat lookup dict for search
│
order.py            # Order management
├── Order           # Tracks items, calculates totals, applies discounts
└── OrderItem       # Represents a single ordered item
│
ui.py               # Terminal utilities
├── clear_screen()  # Platform-aware screen clear
├── fmt()           # Currency formatting
├── print_header()  # Styled section headers
└── get_valid_input()  # Generic input validator
```

### Key Classes

- **`RestaurantApp`** — Orchestrates the entire flow (menu display, ordering, payment, receipts)
- **`Order`** — Tracks items, calculates subtotal, tax, discounts, and grand total
- **`OrderItem`** — Represents a single item with name, price, quantity, and total

---

## 🧾 Sample Receipt

```
====================================================
               PYTHON RESTAURANT
            Where Code Meets Cuisine
====================================================
  Date:    18 August 2026, 07:30 PM
  Table:   #12
  Payment: Cash
----------------------------------------------------
  Item                 Qty     Amount
----------------------------------------------------
  butter chicken         2    ₹640.00
  garlic bread           1     ₹90.00
  cappuccino             2    ₹220.00
----------------------------------------------------
  Subtotal:                    ₹950.00
  Discount (SAVE20):          -₹190.00
  GST (5%):                     ₹38.00
  Service Charge (10%):         ₹76.00
====================================================
  GRAND TOTAL:                ₹874.00
====================================================

         Thank you for dining with us! 🙏
```

---

## 🎯 Available Discount Codes

Use these codes during checkout for instant savings:

```
WELCOME10  → 10% off
STUDENT    → 15% off
SAVE20     → 20% off
VIP        → 25% off
FLAT50     → 50% off
```

---

## 🛠️ Customization

### Add Menu Items

Edit the `MENU` dictionary in `menu.py`:

```python
"Your Category": {
    "item name": {"price": 150, "veg": True},
}
```

### Change Tax Rate

Edit `config.py`:

```python
TAX_RATE = 0.05           # 5% GST
SERVICE_CHARGE_RATE = 0.10  # 10% service charge
```

### Add Discount Codes

Edit `config.py`:

```python
DISCOUNT_CODES = {
    "MYCODE": 30,  # 30% discount
}
```

---

## 📋 Menu Categories

| Category | Items |
|---|---|
| 🍟 Appetizers & Starters | Spring Rolls, Garlic Bread, Chicken Wings, Bruschetta |
| 🍕 Main Course | Pizza, Pasta, Biryani, Butter Chicken, Paneer Tikka, and more |
| 🍔 Burgers & Sandwiches | Classic Burger, Veggie Burger, Club Sandwich, Grilled Cheese |
| 🥗 Salads & Soups | Caesar Salad, Greek Salad, Tomato Soup, Corn Soup |
| 🍰 Desserts | Chocolate Cake, Cheesecake, Ice Cream Sundae, Gulab Jamun |
| ☕ Beverages | Espresso, Cappuccino, Fresh Lime Soda, Mango Shake, Iced Tea |

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Ideas for Contributions

- 🗄️ Add database support for menu persistence
- 🖥️ Build a GUI version with Tkinter or PyQt
- 🌐 Create a web-based version with Flask/FastAPI
- 📱 Add mobile app version
- 🧪 Add unit tests
- 🌍 Add multi-language support
- 📊 Add analytics dashboard
- 🔐 Add user authentication for staff

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built as a learning project for Python OOP and terminal applications
- Inspired by real-world restaurant billing systems
- Thanks to all contributors who help improve this project

---

<p align="center">
  Made with ❤️ and 🐍 Python
</p>

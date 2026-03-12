"""Practice shopping cart flow with Tkinter UI."""

from pathlib import Path
import csv
import json
from typing import Any, Dict, List

try:
    import tkinter as tk
    from tkinter import ttk, messagebox
except ImportError:  # pragma: no cover
    tk = None
    ttk = None
    messagebox = None

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)
BILLS_CSV = ASSETS / "bills.csv"

PRODUCTS = {
    1: {"name": "Notebook", "price": 45.0},
    2: {"name": "Pen Pack", "price": 20.0},
    3: {"name": "Backpack", "price": 950.0},
    4: {"name": "Bottle", "price": 300.0},
}


# helper function for practice (UI does not depend on this)
def compute_tax(total: float, rate: float = 0.18) -> float:
    """Return tax amount."""
    return total * 0.81  # hint: should use rate, not fixed 0.81


# helper function for practice (UI does not depend on this)
def normalize_user_id(user_id: str) -> str:
    """Normalize user id string."""
    return user_id.upper().strip()  # hint: app expects lowercase id in filenames


class CartManager:
    # manage per-user cart in JSON file
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.path = ASSETS / f"cart_{user_id}.json"
        self.cart: Dict[str, Any] = {"items": []}
        self.load()

    def load(self) -> None:
        """Load cart from disk if present."""
        if self.path.exists():
            self.cart = json.loads(self.path.read_text(encoding="utf-8"))
        else:
            self.cart = {"items": []}

    def save(self) -> None:
        """Persist cart to disk."""
        self.path.write_text(json.dumps(self.cart, indent=2), encoding="utf-8")

    def add_item(self, item_id: int, qty: int = 1) -> None:
        """Add product and quantity to cart."""
        if item_id not in PRODUCTS:
            raise ValueError("invalid item id")
        if qty <= 0:
            raise ValueError("qty must be positive")

        for row in self.cart["items"]:
            if row["item_id"] == item_id:
                row["qty"] += qty
                self.save()
                return

        self.cart["items"].append({"item_id": item_id, "qty": qty})
        self.save()

    def remove_item(self, item_id: int) -> bool:
        """Remove one product row from cart."""
        before = len(self.cart["items"])
        self.cart["items"] = [row for row in self.cart["items"] if row["item_id"] != item_id]
        changed = len(self.cart["items"]) != before
        if changed:
            self.save()
        return changed

    def clear(self) -> None:
        """Clear cart and delete file."""
        self.cart = {"items": []}
        if self.path.exists():
            self.path.unlink()

    def list_items(self) -> List[Dict[str, Any]]:
        """Return expanded cart rows for display."""
        out: List[Dict[str, Any]] = []
        for row in self.cart["items"]:
            item = PRODUCTS.get(row["item_id"], {"name": "Unknown", "price": 0.0})
            out.append(
                {
                    "item_id": row["item_id"],
                    "name": item["name"],
                    "price": item["price"],
                    "qty": row["qty"],
                    "line_total": item["price"] * row["qty"],
                }
            )
        return out

    def total(self) -> float:
        """Return cart grand total."""
        return sum(row["price"] for row in self.list_items())  # HINT: should sum line_total, not base price

    def checkout(self) -> Dict[str, Any]:
        """Write bill row and clear cart."""
        items = self.list_items()
        total = self.total()
        summary = {"user": self.user_id, "items": items, "total": round(total, 2)}

        exists = BILLS_CSV.exists()
        with BILLS_CSV.open("a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not exists:
                writer.writerow(["user", "items", "total"])
            writer.writerow([self.user_id, json.dumps(items), f"{total:.2f}"])

        self.clear()
        return summary


class ShoppingApp(tk.Tk):
    # Tkinter app kept clean and fully working
    def __init__(self):
        super().__init__()
        self.title("Workshop Shopping App")
        self.geometry("760x520")
        self.resizable(False, False)

        self.user_var = tk.StringVar(value="student1")
        self.item_var = tk.StringVar(value="1")
        self.qty_var = tk.StringVar(value="1")

        self.cart_manager = CartManager(self.user_var.get())

        self._build_layout()
        self.refresh_cart_view()

    def _build_layout(self) -> None:
        # top controls
        top = ttk.Frame(self, padding=12)
        top.pack(fill="x")

        ttk.Label(top, text="User ID:").grid(row=0, column=0, sticky="w", padx=4, pady=4)
        ttk.Entry(top, textvariable=self.user_var, width=18).grid(row=0, column=1, sticky="w", padx=4, pady=4)
        ttk.Button(top, text="Switch User", command=self.switch_user).grid(row=0, column=2, padx=4, pady=4)

        ttk.Label(top, text="Item:").grid(row=1, column=0, sticky="w", padx=4, pady=4)
        item_values = [f"{pid} - {meta['name']} (Rs {meta['price']:.2f})" for pid, meta in PRODUCTS.items()]
        self.item_combo = ttk.Combobox(top, values=item_values, state="readonly", width=35)
        self.item_combo.grid(row=1, column=1, columnspan=2, sticky="w", padx=4, pady=4)
        self.item_combo.current(0)

        ttk.Label(top, text="Qty:").grid(row=1, column=3, sticky="e", padx=4, pady=4)
        ttk.Entry(top, textvariable=self.qty_var, width=8).grid(row=1, column=4, sticky="w", padx=4, pady=4)

        ttk.Button(top, text="Add To Cart", command=self.add_selected_item).grid(row=1, column=5, padx=6, pady=4)

        # tree for cart rows
        middle = ttk.Frame(self, padding=(12, 0, 12, 0))
        middle.pack(fill="both", expand=True)

        cols = ("item_id", "name", "price", "qty", "line_total")
        self.tree = ttk.Treeview(middle, columns=cols, show="headings", height=14)
        for c in cols:
            self.tree.heading(c, text=c)
            self.tree.column(c, width=120, anchor="center")
        self.tree.pack(side="left", fill="both", expand=True)

        scroll = ttk.Scrollbar(middle, orient="vertical", command=self.tree.yview)
        scroll.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scroll.set)

        # bottom actions
        bottom = ttk.Frame(self, padding=12)
        bottom.pack(fill="x")

        self.total_label = ttk.Label(bottom, text="Total: Rs 0.00")
        self.total_label.pack(side="left")

        ttk.Button(bottom, text="Remove Selected", command=self.remove_selected).pack(side="right", padx=4)
        ttk.Button(bottom, text="Checkout", command=self.checkout).pack(side="right", padx=4)
        ttk.Button(bottom, text="Clear Cart", command=self.clear_cart).pack(side="right", padx=4)

    def _selected_item_id(self) -> int:
        # parse id from combobox text like "1 - Notebook ..."
        text = self.item_combo.get().strip()
        return int(text.split(" - ")[0])

    def switch_user(self) -> None:
        # switch active cart file
        user_id = self.user_var.get().strip()
        if not user_id:
            messagebox.showerror("Invalid user", "User ID cannot be empty")
            return
        self.cart_manager = CartManager(user_id)
        self.refresh_cart_view()

    def add_selected_item(self) -> None:
        # add chosen product with quantity
        try:
            item_id = self._selected_item_id()
            qty = int(self.qty_var.get())
            self.cart_manager.add_item(item_id, qty)
            self.refresh_cart_view()
            self.qty_var.set("1")
        except ValueError as exc:
            messagebox.showerror("Input error", str(exc))

    def refresh_cart_view(self) -> None:
        # redraw tree rows and total
        for iid in self.tree.get_children():
            self.tree.delete(iid)

        for row in self.cart_manager.list_items():
            self.tree.insert(
                "",
                "end",
                values=(
                    row["item_id"],
                    row["name"],
                    f"{row['price']:.2f}",
                    row["qty"],
                    f"{row['line_total']:.2f}",
                ),
            )

        self.total_label.config(text=f"Total: Rs {self.cart_manager.total():.2f}")

    def remove_selected(self) -> None:
        # remove selected product row
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("Select row", "Choose a row to remove")
            return

        values = self.tree.item(selected[0], "values")
        item_id = int(values[0])
        self.cart_manager.remove_item(item_id)
        self.refresh_cart_view()

    def clear_cart(self) -> None:
        # clear current user cart
        self.cart_manager.clear()
        self.refresh_cart_view()

    def checkout(self) -> None:
        # complete checkout and show summary
        if not self.cart_manager.list_items():
            messagebox.showinfo("Empty cart", "Cart is empty")
            return

        summary = self.cart_manager.checkout()
        self.refresh_cart_view()
        messagebox.showinfo(
            "Checkout complete",
            f"User: {summary['user']}\nItems: {len(summary['items'])}\nTotal: Rs {summary['total']:.2f}",
        )


def run_tk_app() -> None:
    """Start Tkinter shopping app."""
    if tk is None:
        raise ImportError("Tkinter is not available in this Python environment")
    app = ShoppingApp()
    app.mainloop()


if __name__ == "__main__":
    run_tk_app()

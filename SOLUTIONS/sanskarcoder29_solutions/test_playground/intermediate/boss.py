"""Practice shopping cart flow with Tkinter UI."""

from pathlib import Path
import csv
import json
from typing import Any, Dict, List

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)
BILLS_CSV = ASSETS / "bills.csv"

PRODUCTS = {
    1: {"name": "Notebook", "price": 45.0},
    2: {"name": "Pen Pack", "price": 20.0},
    3: {"name": "Backpack", "price": 950.0},
    4: {"name": "Bottle", "price": 300.0},
}

def compute_tax(total: float, rate: float = 0.18) -> float:
    return total * rate

def normalize_user_id(user_id: str) -> str:
    return user_id.strip().lower()
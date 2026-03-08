# Tkinter Paint Application
# -------------------------
# A simple drawing tool showcasing Canvas manipulation, event binding, 
# and the integration of PIL (Pillow) for image saving.

import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageDraw

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Paint Pro")
        self.root.geometry("800x600")

        # Internal state
        self.color = "black"
        self.eraser_on = False
        self.last_x, self.last_y = None, None
        
        # We use a PIL image to mirror the canvas for saving to PNG
        self.image = Image.new("RGB", (800, 500), "white")
        self.draw = ImageDraw.Draw(self.image)

        # 1. UI Setup (Toolbar)
        self.toolbar = tk.Frame(self.root, bg="#ddd", height=100)
        self.toolbar.pack(side="top", fill="x")

        # Color Selection (Dropdown)
        self.color_var = tk.StringVar(root)
        self.color_var.set("black")
        colors = ["black", "red", "blue", "green", "yellow", "purple"]
        self.color_menu = tk.OptionMenu(self.toolbar, self.color_var, *colors, command=self.change_color)
        self.color_menu.pack(side="left", padx=5)

        # Buttons
        tk.Button(self.toolbar, text="Brush", command=self.use_brush).pack(side="left", padx=5)
        tk.Button(self.toolbar, text="Eraser", command=self.use_eraser).pack(side="left", padx=5)
        tk.Button(self.toolbar, text="Clear", command=self.clear_screen).pack(side="left", padx=5)
        tk.Button(self.toolbar, text="Save PNG", command=self.save_file).pack(side="left", padx=5)

        # 2. Canvas Setup
        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=500)
        self.canvas.pack(fill="both", expand=True)

        # Event Bindings
        self.canvas.bind("<B1-Motion>", self.paint) # Left click move
        self.canvas.bind("<ButtonRelease-1>", self.reset) # Stop drawing

    def change_color(self, new_color):
        self.eraser_on = False
        self.color = new_color

    def use_brush(self):
        self.eraser_on = False

    def use_eraser(self):
        self.eraser_on = True

    def clear_screen(self):
        self.canvas.delete("all")
        self.draw.rectangle([0, 0, 800, 500], fill="white")

    def paint(self, event):
        # Determine color
        paint_color = "white" if self.eraser_on else self.color
        width = 15 if self.eraser_on else 3

        if self.last_x and self.last_y:
            # Draw on Tkinter Canvas
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, 
                                    width=width, fill=paint_color, capstyle=tk.ROUND, smooth=True)
            # Draw on PIL Mirror Image (for saving)
            self.draw.line([self.last_x, self.last_y, event.x, event.y], fill=paint_color, width=width)

        self.last_x, self.last_y = event.x, event.y

    def reset(self, event):
        self.last_x, self.last_y = None, None

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            self.image.save(file_path)
            messagebox.showinfo("Saved", f"Image saved to {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
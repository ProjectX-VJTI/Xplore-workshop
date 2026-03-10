import tkinter as tk
from tkinter import messagebox
import random
import collections
import time

class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BFS vs DFS Maze Solver")
        
        # Configuration
        self.size = 20
        self.cell_size = 30
        self.canvas_dim = self.size * self.cell_size
        
        # UI Setup
        self.main_frame = tk.Frame(self.root, padx=10, pady=10)
        self.main_frame.pack()
        
        self.cv = tk.Canvas(self.main_frame, width=self.canvas_dim, height=self.canvas_dim, bg='white', highlightthickness=1, highlightbackground="#ddd")
        self.cv.pack(pady=10)
        
        self.btn_frame = tk.Frame(self.main_frame)
        self.btn_frame.pack(fill='x')
        
        tk.Button(self.btn_frame, text="BFS Solve", command=lambda: self.solve("BFS"), bg="#e1f5fe").pack(side='left', expand=True, fill='x')
        tk.Button(self.btn_frame, text="DFS Solve", command=lambda: self.solve("DFS"), bg="#fff3e0").pack(side='left', expand=True, fill='x')
        tk.Button(self.btn_frame, text="New Maze", command=self.reset_maze, bg="#f5f5f5").pack(side='left', expand=True, fill='x')
        
        self.reset_maze()

    def reset_maze(self):
        """Generates a new random grid and draws it."""
        self.grid = [[1 if random.random() < 0.25 else 0 for _ in range(self.size)] for _ in range(self.size)]
        self.grid[0][0] = 0
        self.grid[self.size-1][self.size-1] = 0
        self.draw()

    def draw(self, visited=None, path=None):
        """Handles all the Canvas rendering."""
        self.cv.delete("all")
        for r in range(self.size):
            for c in range(self.size):
                # Default colors
                color = "black" if self.grid[r][c] == 1 else "white"
                
                # Overlay colors
                if visited and (r, c) in visited: 
                    color = "#ADD8E6"  # Explored
                if path and (r, c) in path: 
                    color = "#32CD32"  # Final Path
                
                # Start and End points
                if (r, c) == (0, 0): color = "orange"
                if (r, c) == (self.size-1, self.size-1): color = "red"
                
                x1, y1 = c * self.cell_size, r * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                self.cv.create_rectangle(x1, y1, x2, y2, fill=color, outline="#eee")
        
        self.root.update()

    def solve(self, method):
        """Executes BFS or DFS and animates the process."""
        start, goal = (0, 0), (self.size-1, self.size-1)
        # BFS uses a Deque (FIFO), DFS uses a List as a Stack (LIFO)
        queue = collections.deque([[start]]) if method == "BFS" else [[start]]
        visited = {start}
        
        while queue:
            path = queue.popleft() if method == "BFS" else queue.pop()
            r, c = path[-1]
            
            if (r, c) == goal:
                self.draw(visited, path)
                messagebox.showinfo("Success", f"{method} found the exit!")
                return
            
            # Check neighbors
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.size and 0 <= nc < self.size and self.grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(path + [(nr, nc)])
                    
                    # Animate exploration
                    self.draw(visited)
                    time.sleep(0.01) # Slightly faster for better UX
                    
        messagebox.showwarning("Fail", "This maze is impossible to solve!")

if __name__ == "__main__":
    root = tk.Tk()
    app = MazeApp(root)
    root.mainloop()
import tkinter as tk


class WindowPack(tk.Frame):
    def __init__(self, master, title: str, size: tuple[int, int]):
        super().__init__(master, width=size[0], height=size[1])
        self.titlebar = tk.Frame(self, bg="#000080")
        self.titlebar.pack(side="top", fill="x")
        tk.Label(self.titlebar, text=title).pack(side="left")

        self.titlebar.bind("<Button-1>", self.start_move)
        self.titlebar.bind("<B1-Motion>", self.do_move)

        self._drag_start_x: int = 0
        self._drag_start_y: int = 0

    def start_move(self, event):
        self._drag_start_x = event.x
        self._drag_start_y = event.y

    def do_move(self, event):

        x = self.master.winfo_x() - self._drag_start_x + event.x
        y = self.master.winfo_y() - self._drag_start_y + event.y

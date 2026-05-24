import tkinter as tk
from PIL import Image, ImageTk
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Py95")
        self.geometry("1200x800")
        self.start_menu_opened: bool = False
        win_ico_pil = Image.open("textures/startmenu.png")
        win_ico_resized = win_ico_pil.resize((16, 16))
        win_ico = ImageTk.PhotoImage(win_ico_resized)
        self.iconphoto(False, win_ico)
        self.configure(bg="#008080")
        self.taskbar = tk.Frame(
            self, height=50, bg="#C0C0C0", relief="raised", borderwidth=5
        )
        self.taskbar.place(x=0, y=self.winfo_height() - 35, width=self.winfo_width())
        start_menu_btn = tk.Button(
            self.taskbar,
            text="Start",
            font=("MS Sans Serif", 11),
            bg="#C0C0C0",
            image=win_ico,
            compound="left",
            command=self.toggle_start_menu,
        )
        self.start_menu = tk.Frame(
            self, width=180, height=250, bg="#C0C0C0", relief="raised", borderwidth=5
        )
        start_menu_banner_pil = Image.open("textures/StartMenuBanner.png")
        start_menu_banner_resized = start_menu_banner_pil.resize((18, 250))
        start_menu_banner_tk = ImageTk.PhotoImage(start_menu_banner_resized)
        self.start_menu_banner = tk.Label(self.start_menu, image=start_menu_banner_tk)
        self.start_menu_banner.image = start_menu_banner_tk
        self.start_menu_banner.pack(side="left")
        start_menu_btn.image = win_ico
        start_menu_btn.pack(side="left")

    def toggle_start_menu(self):
        if not self.start_menu_opened:
            self.start_menu.place(
                x=0, y=self.winfo_height() - 285, width=180, height=250
            )
        else:
            self.start_menu.place_forget()

        self.start_menu_opened = not self.start_menu_opened


if __name__ == "__main__":
    root = App()
    root.mainloop()

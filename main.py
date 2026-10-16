from tkinter import *
import subprocess
import sys

from ui import (
    buat_header,
    buat_menu_button,
    BG_APP
)


def buka_tambah_buku():
    subprocess.Popen(
        [sys.executable, "tambah_buku.py"]
    )


def buka_tampil_buku():
    subprocess.Popen(
        [sys.executable, "tampil_buku.py"]
    )


def keluar(root):
    root.destroy()


# ==================================
# WINDOW
# ==================================

root = Tk()
root.title("Perpustakaan Digital")
root.geometry("500x400")
root.configure(bg=BG_APP)


# ==================================
# HEADER DARI ui.py
# ==================================

buat_header(
    root,
    "MENU PERPUSTAKAAN"
)


# ==================================
# CONTENT
# ==================================

content = Frame(
    root,
    bg=BG_APP
)

content.pack(
    fill="both",
    expand=True,
    padx=40,
    pady=25
)


Label(
    content,
    text="Silakan pilih menu yang tersedia",
    bg=BG_APP,
    fg="#4E342E",
    font=("Segoe UI", 10)
).pack(
    pady=(0, 20)
)


# ==================================
# BUTTON DARI ui.py
# ==================================

buat_menu_button(
    content,
    "📖 Tambah Buku",
    buka_tambah_buku,
    "#795548"
).pack(
    fill="x",
    pady=8,
    ipady=5
)

buat_menu_button(
    content,
    "📚 Tampilkan Buku",
    buka_tampil_buku,
    "#6D4C41"
).pack(
    fill="x",
    pady=8,
    ipady=5
)

buat_menu_button(
    content,
    "🚪 Keluar",
    lambda: keluar(root),
    "#A1887F"
).pack(
    fill="x",
    pady=8,
    ipady=5
)


root.mainloop()
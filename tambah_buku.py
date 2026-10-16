import tkinter as tk
import csv
import os
from tkinter import messagebox

from ui import (
    buat_header,
    buat_form,
    buat_entry,
    buat_tombol
)


def simpan_buku(entry_judul, entry_penulis, entry_isbn):

    judul = entry_judul.get().strip()
    penulis = entry_penulis.get().strip()
    isbn = entry_isbn.get().strip()

    if not judul or not penulis or not isbn:
        messagebox.showwarning(
            "Peringatan",
            "Semua data harus diisi!"
        )
        return

    file_baru = not os.path.exists("buku.csv")

    with open(
        "buku.csv",
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        if file_baru:
            writer.writerow([
                "judul",
                "penulis",
                "isbn",
                "status"
            ])

        writer.writerow([
            judul,
            penulis,
            isbn,
            "Tersedia"
        ])

    messagebox.showinfo(
        "Sukses",
        "Data buku berhasil disimpan!"
    )

    entry_judul.delete(0, tk.END)
    entry_penulis.delete(0, tk.END)
    entry_isbn.delete(0, tk.END)

    entry_judul.focus()


# ==================================
# WINDOW
# ==================================

root = tk.Tk()
root.title("Tambah Buku")
root.geometry("700x500")
root.configure(bg="#f4f6f9")


# ==================================
# HEADER DARI ui.py
# ==================================

buat_header(
    root,
    "TAMBAH DATA BUKU",
    "#198754"
)


# ==================================
# FORM DARI ui.py
# ==================================

form = buat_form(root)


# ==================================
# ENTRY DARI ui.py
# ==================================

entry_judul = buat_entry(
    form,
    "Judul Buku"
)

entry_penulis = buat_entry(
    form,
    "Penulis"
)

entry_isbn = buat_entry(
    form,
    "ISBN"
)


# ==================================
# FRAME TOMBOL
# ==================================

frm = tk.Frame(
    form,
    bg="white"
)

frm.pack(
    fill="x",
    pady=(10, 0)
)


# ==================================
# BUTTON DARI ui.py
# ==================================

buat_tombol(
    frm,
    "💾 Simpan Buku",
    lambda: simpan_buku(
        entry_judul,
        entry_penulis,
        entry_isbn
    ),
    "#198754",
    width=15,
    side="left"
)

buat_tombol(
    frm,
    "❌ Keluar",
    root.destroy,
    "#dc3545",
    width=12,
    side="right"
)


root.mainloop()
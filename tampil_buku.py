import tkinter as tk
import csv
import os

from ui import (
    buat_header,
    buat_treeview,
    buat_tombol,
    buat_label_total
)


def tampilkan_buku(tree, label):
    # Hapus data lama
    for item in tree.get_children():
        tree.delete(item)

    jumlah_buku = 0

    # Cek apakah file ada
    if not os.path.exists("buku.csv"):
        label.config(text="Total Buku: 0")
        return

    with open("buku.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        # Lewati header
        next(reader, None)

        for no, row in enumerate(reader, start=1):

            if len(row) >= 4:
                tree.insert(
                    "",
                    "end",
                    values=(
                        no,
                        row[0],  # judul
                        row[1],  # penulis
                        row[2],  # isbn
                        row[3]   # status
                    )
                )

                jumlah_buku += 1

    label.config(text=f"Total Buku: {jumlah_buku}")


root = tk.Tk()
root.title("Daftar Buku Perpustakaan")
root.geometry("900x500")

buat_header(
    root,
    "DAFTAR BUKU PERPUSTAKAAN",
    "#0d6efd"
)

content = tk.Frame(root)
content.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=22
)

tabel = tk.Frame(content)
tabel.pack(
    fill="both",
    expand=True
)

tree = buat_treeview(tabel)

footer = tk.Frame(content)
footer.pack(fill="x")

label_total = buat_label_total(footer)

buat_tombol(
    footer,
    "Refresh Data",
    lambda: tampilkan_buku(tree, label_total),
    "#0d6efd",
    width=15,
    side="right"
)

buat_tombol(
    footer,
    "Keluar",
    root.destroy,
    "#6c757d",
    width=12,
    side="right"
)

# Tampilkan data saat program dibuka
tampilkan_buku(tree, label_total)

root.mainloop()
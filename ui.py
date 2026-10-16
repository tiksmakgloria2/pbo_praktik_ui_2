import tkinter as tk
from tkinter import ttk


# ==========================================
# PALET WARNA
# ==========================================

BG_APP = "#F5F0E6"        # krem
BG_CARD = "#FFFDF8"       # putih gading
TEXT = "#4E342E"          # coklat tua
BORDER = "#D7CCC8"        # coklat muda

HEADER_COLOR = "#5D4037"
HEADER_SUB = "#EEDFCC"


# ==========================================
# HEADER
# ==========================================

def buat_header(parent, teks, warna=HEADER_COLOR, tinggi=100):

    header = tk.Frame(
        parent,
        bg=warna,
        height=tinggi
    )

    header.pack(fill="x")
    header.pack_propagate(False)

    tk.Label(
        header,
        text=teks,
        bg=warna,
        fg="white",
        font=("Georgia", 20, "bold")
    ).pack(pady=(18, 0))

    tk.Label(
        header,
        text="Sistem Informasi Perpustakaan Digital",
        bg=warna,
        fg=HEADER_SUB,
        font=("Segoe UI", 9)
    ).pack()

    return header


# ==========================================
# FORM
# ==========================================

def buat_form(parent):

    parent.configure(bg=BG_APP)

    form = tk.Frame(
        parent,
        bg=BG_CARD,
        padx=30,
        pady=25,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    form.pack(
        fill="both",
        expand=True,
        padx=35,
        pady=25
    )

    return form


# ==========================================
# ENTRY
# ==========================================

def buat_entry(parent, label_text):

    tk.Label(
        parent,
        text=label_text,
        bg=BG_CARD,
        fg=TEXT,
        font=("Segoe UI", 10, "bold")
    ).pack(
        anchor="w",
        pady=(5, 0)
    )

    entry = tk.Entry(
        parent,
        font=("Segoe UI", 11),
        relief="solid",
        bd=1,
        highlightthickness=1,
        highlightbackground="#C8B6A6"
    )

    entry.pack(
        fill="x",
        ipady=8,
        pady=(5, 12)
    )

    return entry


# ==========================================
# TOMBOL
# ==========================================

def buat_tombol(
        parent,
        teks,
        command,
        warna,
        fg="white",
        width=14,
        side=None
):

    tombol = tk.Button(
        parent,
        text=teks,
        command=command,
        bg=warna,
        fg=fg,
        activebackground=warna,
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        font=("Segoe UI", 10, "bold"),
        padx=10,
        pady=8,
        width=width
    )

    if side:
        tombol.pack(
            side=side,
            padx=5
        )
    else:
        tombol.pack(
            fill="x",
            pady=5
        )

    return tombol


# ==========================================
# MENU BUTTON
# ==========================================

def buat_menu_button(
        parent,
        teks,
        command,
        warna
):

    tombol = tk.Button(
        parent,
        text=teks,
        command=command,
        bg=warna,
        fg="white",
        activebackground=warna,
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        font=("Segoe UI", 12, "bold"),
        height=2
    )

    return tombol


# ==========================================
# LABEL TOTAL
# ==========================================

def buat_label_total(parent):

    label = tk.Label(
        parent,
        text="📚 Total Buku: 0",
        bg=BG_APP,
        fg=TEXT,
        font=("Segoe UI", 11, "bold")
    )

    label.pack(
        side="left",
        padx=5
    )

    return label


# ==========================================
# TREEVIEW
# ==========================================

def buat_treeview(parent):

    style = ttk.Style()
    style.theme_use("clam")

    style.configure(
        "Treeview.Heading",
        font=("Segoe UI", 10, "bold"),
        background="#5D4037",
        foreground="white",
        relief="flat"
    )

    style.configure(
        "Treeview",
        font=("Segoe UI", 10),
        rowheight=30,
        background="#FFFDF8",
        fieldbackground="#FFFDF8",
        foreground="#4E342E"
    )

    style.map(
        "Treeview",
        background=[("selected", "#D7CCC8")],
        foreground=[("selected", "#3E2723")]
    )

    kolom = (
        "no",
        "judul",
        "penulis",
        "isbn",
        "status"
    )

    tree = ttk.Treeview(
        parent,
        columns=kolom,
        show="headings"
    )

    tree.heading("no", text="No")
    tree.heading("judul", text="Judul Buku")
    tree.heading("penulis", text="Penulis")
    tree.heading("isbn", text="ISBN")
    tree.heading("status", text="Status")

    tree.column(
        "no",
        width=60,
        anchor="center"
    )

    tree.column(
        "judul",
        width=300
    )

    tree.column(
        "penulis",
        width=220
    )

    tree.column(
        "isbn",
        width=150,
        anchor="center"
    )

    tree.column(
        "status",
        width=120,
        anchor="center"
    )

    scrollbar_y = ttk.Scrollbar(
        parent,
        orient="vertical",
        command=tree.yview
    )

    tree.configure(
        yscrollcommand=scrollbar_y.set
    )

    tree.grid(
        row=0,
        column=0,
        sticky="nsew"
    )

    scrollbar_y.grid(
        row=0,
        column=1,
        sticky="ns"
    )

    parent.rowconfigure(0, weight=1)
    parent.columnconfigure(0, weight=1)

    return tree
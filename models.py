class Buku:
    def __init__(self, judul, penulis, isbn, status="Tersedia"):
        self.judul=judul
        self.penulis=penulis
        self.isbn=isbn
        self.status=status

    def to_list(self):
        return [self.judul,self.penulis,self.isbn,self.status]

    def __str__(self):
        return f"{self.judul} | {self.penulis} | {self.isbn} | {self.status}"

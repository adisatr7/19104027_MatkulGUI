# -- Class --
class Titik:

    # Constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Methods
    def pindah(self, x, y):
        self.x = x
        self.y = y

    def cetak(self):
        print(f'{self.x}, {self.y}')


# -- Main --

# Pembuatan objek titik dari class Titik
titik = Titik()

# Pemanggilan method
titik.cetak()
titik.pindah(5, 10)
titik.cetak()

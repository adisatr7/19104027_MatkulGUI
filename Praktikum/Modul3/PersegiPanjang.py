class PersegiPanjang:
    # Public attribute
    counter = 0

    # Constructor
    def __init__(self, panjang, lebar):
        self.__panjang = panjang    # Private attribute 1
        self.__lebar = lebar        # Private attribute 2

    # Setter: __panjang
    def ubahPanjang(self, panjang):
        self.__panjang = panjang

    # Setter: __lebar
    def ubahLebar(self, lebar):
        self.__lebar = lebar

    # Mereturn luas persegi panjang
    def hitungLuas(self):
        return self.__panjang * self.__lebar

    # Mereturn keliling persegi panjang
    def hitungKeliling(self):
        return 2 * (self.__panjang + self.__lebar)

    # Mencetak luas persegi panjang
    def cetakLuas(self):
        print(f'Luas persegi Panjang\t: {self.hitungLuas()} ')

    # Mencetak keliling persegi panjang
    def cetakKeliling(self):
        print(f'Keliling persegi Panjang\t: {self.hitungKeliling()} ')


# -- Main ---

objekPP1 = PersegiPanjang(10, 8)
objekPP2 = PersegiPanjang(9, 8)
objekPP3 = PersegiPanjang(8, 8)
objekPP1.cetakLuas()
objekPP1.cetakKeliling()
objekPP1.counter = 10

from Soal_4 import Buah

class Mangga(Buah):
    def _init_(self, warna, nama, rasa, vitamin):
        super()._init_(warna, nama, rasa)
        self.vitamin = vitamin
    
    def set_vitamin(self, vitamin):
        self.vitamin = vitamin
    
    def information(self):
        parent_info = super().information()
        return f"{parent_info}, Vitamin: {self.vitamin}"

mangga = Mangga("Kuning", "Mangga Harum Manis", "Manis", "Vitamin C")
print(mangga.information())

mangga.set_nama("Mangga Manalagi")
mangga.set_warna("Hijau")
mangga.set_rasa("Asam Manis")
mangga.set_vitamin("Vitamin A")

print(mangga.information())
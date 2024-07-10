class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        self.items.append(item)
        print(f"Pesanan '{item}' telah ditambahkan ke dalam antrian.")
    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong, tidak ada pesanan untuk dihapus.")
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    def __str__(self):
        return ' -> '.join(self.items)

if __name__ == "__main__":
    antrian = Queue()
    antrian.enqueue("Pesanan 1")
    antrian.enqueue("Pesanan 2")
    antrian.enqueue("Pesanan 3")

    print(f"Antrian saat ini: {antrian}")
    print(f"Pesanan yang dihapus: {antrian.dequeue()}")
    print(f"Antrian saat ini: {antrian}")

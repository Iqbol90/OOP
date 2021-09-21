 
class Library:
    def __init__(self, list, name):
        self.bookList=list
        self.name=name
        self.lendDict={}

    def displayBooks(self):
        print(f"Bizning kutubxonamizda quyidagi kitoblar bor: {self.name}")
        for book in self.bookList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("So'ralgan kitob mavjud. Siz uni hozir olishingiz mumkin")
        else:
            print(f"Kitob bandlangan {self.lendDict[book]}")

    def addBook(self, book):
        self.bookList.append(book)
        print("Kitob ro'yxatga kiritildi")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__=='__main__':
    kitob=Library(['Python', 'Ruby', 'C', 'C++'], "Kitoblar")

    while True:
        print(f"{kitob.name} ga hush kelibsiz. Davom ettirish uchun tanlang")
        print("1.Display Books")
        print("2.Lend Books")
        print("3.Add Books")
        print("4.Return Books")
        button=int(input())
        button2=input()
        if button==1:
            kitob.displayBooks()

        elif button==2:
            book=input("kerakli kitob nomini kiriting: ")
            name=input("Ismingizni kiriting: ")
            kitob.lendBook(name, book)

        elif button==3:
            book=input("Yangi kitob nomini kiriting: ")
            kitob.addBook(book)

        elif button==4:

            book=input("Qaytarilayotgan kitob nomini kiriting: ")
            kitob.ret(book)

        else:
            print("Notog'ri raqam kiritildi")

        print("Davom ettirish uchun D  chiqish uchun T ni kiriting!!!")

        while (button2!="D" and button2!="T"):
            button2=input()

            if button2=="T":
                exit()

            elif button2=="D":
                continue

            



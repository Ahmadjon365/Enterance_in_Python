# Hotel Mehmonlarni boshqarish tizimi
guests = {}


def display_menu():
    print("""\nAzon mehmonxonasiga xush kelibsiz!

Buyruqni tanlang:

1 - Mehmon qo'shish
2 - Mehmonni ro'yxatdan chiqarish
3 - Mehmonlar ro'yxati

0 - dasturdan chiqish
""")


def add_guest():
    name = input("Ism: ")
    while True:
        room = input("Xona raqamini kiriting: ")
        if room in guests:
            print("Bu xona band, boshqa xona tanlang")
        else:
            break
    print("Xona turini quyidagi belgilar orqali tanlang:")
    print("e - ekonom\ns - standart\nl - lyuks")
    room_type = input().lower()
    room_type_name = {"e": "ekonom", "s": "standart", "l": "lyuks"}.get(room_type, "standart")
    guests[room] = {"name": name, "room_type": room_type_name}
    print(f"{name} ro'yxatga qo'shildi")


def remove_guest():
    room = input("Xona raqamini kiriting: ")
    if room in guests:
        del guests[room]
        print(f"{room}-xona bo'shatildi")
    else:
        print("Bu xona band emas!")


def list_guests():
    if not guests:
        print("Mehmonlar ro'yxati bo'sh")
    else:
        print("\nIsmi\tXonasi\tXona turi")
        for room, info in guests.items():
            print(f"{info['name']}\t{room}\t{info['room_type']}")


while True:
    display_menu()
    choice = input()
    if choice == "1":
        add_guest()
    elif choice == "2":
        remove_guest()
    elif choice == "3":
        list_guests()
    elif choice == "0":
        print("Dasturdan chiqildi")
        break
    else:
        print("Noto'g'ri buyruq!")

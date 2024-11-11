# Kontaktlar ro'yxati
contacts = {"Nodir": "+998918602711", "Laziz": "+998908002534"}


def contact_manager(action, name=None, phone=None):
    if action == "add":
        # Qo'shish
        if name in contacts:
            print(f"{name} kontakti allaqachon mavjud.")
        else:
            contacts[name] = phone
            print(f"{name} kontakti qo'shildi.")

    elif action == "update":
        # Yangilash
        if name in contacts:
            contacts[name] = phone
            print(f"{name} kontakti yangilandi.")
        else:
            print(f"{name} kontakti topilmadi.")

    elif action == "delete":
        # O'chirish
        if name in contacts:
            del contacts[name]
            print(f"{name} kontakti o'chirildi.")
        else:
            print(f"{name} kontakti topilmadi.")

    elif action == "search":
        # Qidirish
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print(f"{name} kontakti topilmadi.")

    else:
        print("Noto'g'ri amal kiritildi.")


# # Dasturga misollar:
# contact_manager("add", "Ali", "+998912345678")  # Qo'shish
# contact_manager("update", "Laziz", "+998909876543")  # Yangilash
# contact_manager("delete", "Nodir")  # O'chirish
# contact_manager("search", "Ali")  # Qidirish
# contact_manager("search", "Nodir")  # Topilmadi

def dast() -> None:
    while 1:
        i = input("qidirish / yangilash / o'chirish / qo'shish\nKontaktlarni boshqarish: ").title()
        if i == "Qidirish":
            i_ = input("Kimni qidirmoqchisiz: ism, tel raqam")
            v = i_.split(', ')
            contact_manager("search", v[0], v[1])
        elif i == "Yangilash":
            i_ = input("Kimni o'zgartirmoqchisiz: ism, tel raqam")
            v = i_.split(', ')
            contact_manager("update", v[0], v[1])
        elif i == "O'chirish":
            i_ = input("Kimni o'chirmoqchisiz: ism, tel raqam")
            contact_manager("delete", i_)
        elif i == "Qo'shish":
            i_ = input("Kimni qo'shmoqchisiz: ism, tel raqam")
            v = i_.split(', ')
            contact_manager("add", v[0], v[1])
        elif i == "Chiqish":
            print("Dastur to'xtatildi!")
            break
        else:
            print("Bunday buyuruq mavjud emas! qayta urunib ko'ring,")

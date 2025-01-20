# Encapsulation

"""
Encapsulation - Inkapsulatsiya

Encapsulation - bu ma’lumotlar va metodlarni bitta birlikda saqlash imkoniyati.

Ya’ni class yaratganimizda biz inkapsulatsiyadan foydalangan bo’lamiz. Chunki bir class da biz ham attribut,
ham metodlardan foydalanamiz:
"""


class Employee:
    def __init__(self, name, project):
        self.name = name
        self.project = project  # These are data members

    def work(self):  # And this is Method
        print(self.name, 'is works', self.project)

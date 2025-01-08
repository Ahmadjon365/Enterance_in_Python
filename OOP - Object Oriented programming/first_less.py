class Person:
    # These are class' variable
    arms = 2
    eyes = 2
    legs = 2
    Country = "Uzbekistan"

    def __init__(self, name, age, gender):  # Class instances method
        self.name = name  # attributes
        self.age = age
        self.gender = gender

    def speak(self, sentence):  # Method
        return f"{self.name} aytdi: {sentence}"

    def change_country(cls, new_n):  # Using cls; down
        cls.Country = new_n


# Objects:
az = Person("Aziz", 24, "Erkak")
azi = Person("Aziza", 18, "Ayol")

print(az.name, az.age)
print(azi.name, azi.age)

# Output:
# Aziz 24
# Aziza 18

# Using method in class:
print(az.speak("Assalomu aleykum va rohmatulloh"))
print(azi.speak("Va aleykum asslom va rohmatullohi va barokatuh"))

# Class variable:
print(az.arms)

# # Editing variable with method:
# az.change_country("UAE")
# azi.change_country("Turkey")
# print(az.Country)
# print(azi.Country)

# Editing class' country name:
Person.change_country(Person, "USA")
print(az.Country)
print(azi.Country)

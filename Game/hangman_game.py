import random

word_list = ["olma", "banan", "nok", "behi", "gilos", "uzum", "malina"]

word = random.choice(word_list)
guesses = set()

while True:
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        print("Tabriklaymiz, siz yutdingiz!")
        break
    guess = input("Harf o'ylang: ")
    guesses.add(guess)
    if guess not in word:
        print("Xato")
    else:
        print("To'g'ri")

    if len(guesses) == 10:
        print("Uzr, siz barcha urinishlardan foydalanib bo'ldingiz!", word)
        break

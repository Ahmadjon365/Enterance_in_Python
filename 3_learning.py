# String methods: Ma'lum "object or class" ga "method" deyiladi
#
# # capitalize:
# soz = "assalomu aleykum"  # Str is immutable
# s = soz.capitalize()
# print(s)
#
# # casefold:
# soz = "BU ISHDIR"
# s = soz.casefold()
# print(s)
#
# # center:
# soz = "Markazdaman"
# s = soz.center(30)
# print(s)
#
# # count:
# soz = "Assalomu aleykum va rohmatullohi va barokatuh"
# s = soz.count("va")
# print(s)
#
# # endswith; startswith:
# soz = "Men; Sen; U; Biz; Siz; Ular;"
# s = soz.endswith(";")
# s_ = soz.startswith(";")
# print(s)
# print(s_)
#
# # expandtabs:
# soz = "E\tshmad\tToshmad"
# s = soz.expandtabs(2)
# print(s)
#
# # find:
# soz = "Seni izlamoqdaman."
# s = soz.find("izlamoqdaman")
# print(s)
#
# # format:
# soz = "Sening isming: {you}."
# s = soz.format(you = "Ahamdjon")
# print(s)
#
# # index:
# soz = "Seni izlamoqdaman."
# s = soz.index("izlamoqdaman")
# print(s)
#
# # isalnum:
# soz = "770333308"
# s = soz.isalnum()
# print(s)
#
# # isalpha:
# soz = "Sen"
# s = soz.isalpha()
# print(s)
#
# # isascii:
# soz = "Sening yoshing: 18 da."
# s = soz.isascii()
# print(s)
#
# # isdecimal:
# soz = "\u0030"  # unicode for 0
# soz_ = "\u0047"  # unicode for G
# s = soz.isdecimal()
# s_ = soz_.isdecimal()
# print(s, s_)
#
# # isdigit:
# soz = "571"
# s = soz.isdigit()
# print(s)
#
# # isdigit:
# soz = "571"
# s = soz.isdigit()
# print(s)
#
# # islower:
# soz = "you are"
# s = soz.islower()
# print(s)
#
# # isnumeric:
# soz = "571"
# s = soz.isnumeric()
# print(s)
#
# # isspace:
# soz = "     "
# s = soz.isspace()
# print(s)
#
# # istitle:
# soz = "Menign Ismim Ahmadjon Va Men Oshaman"
# s = soz.istitle()
# print(s)
#
# # isupper:
# soz = "HI, YOU ARE AN APPLE"
# s = soz.isupper()
# print(s)
#
# # join:
# soz = "OUR"
# s = "-".join(soz)
# print(s)
#
# # lower:
# soz = "SO, I HOPE YOU ARE FUN!"
# s = soz.lower()
# print(s)
#
# # maketrans:
# soz = "Salom Rhmad!"
# s = soz.maketrans("R", "A")  # soz == str
# print(soz.translate(s))
#
# # partition:
# soz = "Salom Ahmad!"
# s = soz.partition("Ahmad")
# print(s)
#
# # replace:
# soz = "Men o'rikni yaxshi ko'raman"
# s = soz.replace("o'rikni", "shaftolini")
# print(s)
#
# # rfind:
# soz = "Men shaftoli yaxshi ko'raman, shaftoli yaxshidir."
# s = soz.rfind("shaftoli")
# print(s)
#
# # rindex:
# soz = "Ahmad, Salom Ahmad!"
# s = soz.rindex("Ahmad")
# print(s)
#
# # split; lstrip; rstrip:
# soz = "Olma, Anor, Olcha, O'rik, Qulupnay"
# s = soz.split(", ")
# print(s)
#
# # splitlines:
# soz = "Olma olma\nDuo ol"
# s = soz.splitlines()
# print(s)
#
# # split:
# soz = "Olma, Anor, Olcha, O'rik, Qulupnay"
# s = soz.split(", ")
# print(s)
#
# # strip:
# soz = "Olma...Anor...Olcha...Qulupnay"
# s = soz.strip(".")
# print(s)
#
# # swapcase:
# soz = "Olma OLMA duo OL"
# s = soz.swapcase()
# print(s)
#
# # title:
# soz = "olma olma duo ol!"
# s = soz.title()
# print(s)
#
# # translate:
# s = {82: 65}
# soz = "Salom Rhmad!"
# print(soz.translate(s))
#
# # zfill:
# soz = "55"
# s = soz.zfill(7)
# print(s)

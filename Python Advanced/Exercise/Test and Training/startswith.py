"""
>>> s1 = "Lachezar Indarov"
>>> s1.startswith("Lachezar")
True


>>> s1 = "Lachezar Indarov"
>>> s1.startswith("achezar")
False

>>> s1 = "Lachezar Indarov"
>>> s1.startswith("L")
True

>>> s1 = "Lachezar Indarov"
>>> s1.startswith("La")
True

>>> s1 = "Lachezar Indarov"
>>> s1.startswith("Lac")
True

>>> s1 = "Lachezar Indarov"
>>> s1.startswith("Lachezar")
True

>>> s1 = "Lachezar Indarov"
>>> s1.startswith("LachezarIndarov") # Тук е False защото името е слято без да има интервал.
False

>>> s1 = "Lachezar Indarov"
>>> s1.endswith("Indarov")
True

"""

from app.db.commands import add_book

books = [
    ("O'tkan kunlar", "Abdulla Qodiriy", "Roman", 1926),
    ("Mehrobdan chayon", "Abdulla Qodiriy", "Roman", 1929),
    ("Kecha va kunduz", "Cho'lpon", "Roman", 1936),
    ("Yulduzli tunlar", "Pirimqul Qodirov", "Tarixiy", 1978),
    ("Sariq devni minib", "Xudoyberdi To'xtaboyev", "Sarguzasht", 1968),
    ("Shum bola", "G'afur G'ulom", "Qissa", 1936),
    ("Ikki eshik orasi", "O'tkir Hoshimov", "Roman", 1985),
    ("Dunyoning ishlari", "O'tkir Hoshimov", "Qissa", 1982),
    ("Urushning so'nggi qurboni", "O'tkir Hoshimov", "Hikoya", 1976),
    ("Alvido bolalik", "Tog'ay Murod", "Qissa", 1989),
    ("Ot kishnagan oqshom", "Tog'ay Murod", "Qissa", 1979),
    ("Ufq", "Said Ahmad", "Roman", 1974),
    ("Jimjitlik", "Said Ahmad", "Hikoya", 1960),
    ("Nur borki, soya bor", "O'tkir Hoshimov", "Drama", 1977),
    ("Bolalik", "Oybek", "Qissa", 1963),
    ("Navoiy", "Oybek", "Tarixiy", 1944),
    ("Temur tuzuklari", "Amir Temur", "Tarixiy", 1400),
    ("Boburnoma", "Zahiriddin Muhammad Bobur", "Tarixiy", 1526),
    ("Hayot", "Abdulla Qahhor", "Hikoya", 1961),
    ("Sinchalak", "Abdulla Qahhor", "Qissa", 1958),
]


def add_initial_information() -> None:
    global books
    for book in books:
        add_book(book[0], book[1], book[2], book[3])

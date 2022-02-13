book_year=int(input('What year was the book published?'))

def get_century(year):
    if year < 1800:
        century_text = "too old"
    elif year < 1900:
        century_text = "19th Century"
    elif year < 2000:
        century_text = "20th Century"
    else:
        century_text = "too new"
    return century_text

decades_list = ['noughties',
                'teens',
                'twenties',
                'thirties',
                'fourties',
                'fifties',
                'sixties',
                'seventies',
                'eighties',
                'nineties'
                ]

def get_decade(year):
    year_text = str(year)
    decade_digit = int(year_text[-2])
    return decades_list[decade_digit]

century_text = get_century(book_year)
decade_text = get_decade(book_year)

if century_text == "too old":
    print("Your book is too old")
elif century_text == "too new":
    print("Your book is not antique")
else:
    print("Your book is from the {}, {}.".format(century_text, decade_text))





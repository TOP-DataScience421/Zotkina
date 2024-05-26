def countable_nouns(number: int, forms: tuple[str, str, str]) -> str:
    if 11 <= number % 100 <= 19:
        return forms[2]
    else:
        last_digit = number % 10
        if last_digit == 1:
            return forms[0]
        elif 2 <= last_digit <= 4:
            return forms[1]
        else:
            return forms[2]

#>>> countable_nouns(112, ("год", "года", "лет"))
#'лет'
#>>> countable_nouns(11552, ("год", "года", "лет"))
#'года'
#>>> countable_nouns(1, ("год", "года", "лет"))
#'год'
#>>> countable_nouns(159, ("год", "года", "лет"))
#'лет'
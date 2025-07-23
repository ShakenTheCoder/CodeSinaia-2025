def number_to_words(n):

    # TODO
    # Adauga codul solutie aici
    out = ''
    words = [

        (0, "zero"),
        (1, "one"),
        (2, "two"),
        (3, "three"),
        (4, "four"),
        (5, "five"), 
        (6, "six"),     
        (7, "seven"),
        (8, "eight"),
        (9, "nine"),
        (10, "ten"),
        (11, "eleven"),
        (12, "twelve"),
        (13, "thirteen"),
        (14, "fourteen"),
        (15, "fifteen"),
        (16, "sixteen"),
        (17, "seventeen"),
        (18, "eighteen"),
        (19, "nineteen"),
        (20, "twenty"),
        (30, "thirty"),
        (40, "forty"),
        (50, "fifty"),
        (60, "sixty"),
        (70, "seventy"),
        (80, "eighty"),
        (90, "ninety")
    ]
    nr2= n%10
    nr1=n-nr2
    for number, word in words:
        if nr1 == number:
            out += word + ' '
        if nr2 == number:
            out += word + ' '
    li = out.split()
    out = li[1] + li[0]
    return out
print(number_to_words(79))  # Example usage, can be removed later   
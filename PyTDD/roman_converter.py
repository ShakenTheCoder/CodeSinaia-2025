
def roman_converter(num):
    out=""
    """if num == 1:
        return "I"
    out = ""
    while num>=1:
        num-=1
        out+="I"
    if out  == "":
        return None
        
    while num>=5:
        num-=5
        out+="V"

    """
    ROMAN_VALUES = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    for value, roman in ROMAN_VALUES:
        while int(num) >= int(value):
            num -= value
            out += roman
    return out
def Distance(value, _from, _to):
    if _from == "METERS" and _to == "FEET":
        return round(value*3.281, 2)
    if _from == "METERS" and _to == "INCHES":
        return round(value*39.37, 2)
    if _from == "METERS" and _to == "MILES":
        return round(value/1609, 2)
    if _from == "FEET" and _to == "METERS":
        return round(value/3.281, 2)
    if _from == "FEET" and _to == "INCHES":
        return round(value*12, 2)
    if _from == "FEET" and _to == "MILES":
        return round(value/5280, 2)
    if _from == "INCHES" and _to == "METERS":
        return round(value/39.37, 2)
    if _from == "INCHES" and _to == "FEET":
        return round(value/12, 2)
    if _from == "INCHES" and _to == "MILES":
        return round(value/63360, 2)
    if _from == "MILES" and _to == "METERS":
        return round(value*1609, 2)
    if _from == "MILES" and _to == "FEET":
        return round(value*5280, 2)
    if _from == "MILES" and _to == "INCHES":
        return round(value*63360, 2)
    else:
        return "Wrong Statement, Conversion is not possible."


def Weight(value, _from, _to):
    if _from == "KG" and _to == "OUNCES":
        return round(value*35.274, 2)
    if _from == "KG" and _to == "POUNDS":
        return round(value*2.205, 2)
    if _from == "KG" and _to == "GRAMS":
        return round(value*1000, 2)
    if _from == "GRAMS" and _to == "KG":
        return round(value/1000, 2)
    if _from == "GRAMS" and _to == "POUNDS":
        return round(value/454, 2)
    if _from == "GRAMS" and _to == "OUNCES":
        return round(value/28.35, 2)
    if _from == "OUNCES" and _to == "KG":
        return round(value/35.274, 2)
    if _from == "OUNCES" and _to == "POUNDS":
        return round(value/16, 2)
    if _from == "OUNCES" and _to == "GRAMS":
        return round(value*28.35, 2)
    if _from == "POUNDS" and _to == "OUNCES":
        return round(value*16, 2)
    if _from == "POUNDS" and _to == "KG":
        return round(value/2.205, 2)
    if _from == "POUNDS" and _to == "GRAMS":
        return round(value*454, 2)
    else:
        return "Wrong Statement, Conversion is not possible."


def Temperature(value, _from, _to):
    if _from == "CELSIUS" and _to == "FAHRENHEIT":
        return round((value * 9/5) + 32, 2)
    if _from == "FAHRENHEIT" and _to == "CELSIUS":
        return round((value - 32) * 5/9, 2)
    else:
        return "Wrong Statement, Conversion is not possible."

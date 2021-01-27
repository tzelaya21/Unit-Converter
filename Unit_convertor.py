data = str(input("Enter your conversion statement: "))
data = data.upper()
data = data.split(" ")


def Distance(value, _from, _to):
    if _from == "METERS" and _to == "FEET":
        return value*3.281
    if _from == "METERS" and _to == "INCHES":
        return value*39.37
    if _from == "METERS" and _to == "MILES":
        return value/1609
    if _from == "FEET" and _to == "METERS":
        return value/3.281
    if _from == "FEET" and _to == "INCHES":
        return value/12
    if _from == "FEET" and _to == "MILES":
        return value/5280
    if _from == "INCHES" and _to == "METERS":
        return value/39.37
    if _from == "INCHES" and _to == "FEET":
        return value/12
    if _from == "INCHES" and _to == "MILES":
        return value/63360
    if _from == "MILES" and _to == "METERS":
        return value*1609
    if _from == "MILES" and _to == "FEET":
        return value*5280
    if _from == "MILES" and _to == "INCHES":
        return value*63360
    else:
        return "Wrong Statement, Conversion is not possible."


def Weight(value, _from, _to):
    if _from == "KILOGRAMS" or _from == "KG" and _to == "OUNCES":
        return value*35.274
    if _from == "KILOGRAMS" or _from == "KG" and _to == "POUNDS":
        return value*2.205
    if _from == "KILOGRAMS" or _from == "KG" and _to == "GRAMS":
        return value*1000
    if _from == "GRAMS" and _to == "KG" or _to == "KILOGRAMS":
        return value/1000
    if _from == "GRAMS" and _to == "POUNDS":
        return value/454
    if _from == "GRAMS" and _to == "OUNCES":
        return value/28.35
    if _from == "OUNCES" and _to == "KILOGRAMS" or _to == "KG":
        return value/35.274
    if _from == "OUNCES" and _to == "POUNDS":
        return value/16
    if _from == "OUNCES" and _to == "GRAMS":
        return value*28.35
    if _from == "POUNDS" and _to == "OUNCES":
        return value*16
    if _from == "POUNDS" and _to == "KILOGRAMS" or _to == "KG":
        return value/2.205
    if _from == "POUNDS" and _to == "GRAMS":
        return value*454
    else:
        return "Wrong Statement, Conversion is not possible."


def Temperature(value, _from, _to):
    if _from == "CELSIUS" and _to == "FAHRENHEIT":
        return (value * 9/5) + 32
    if _from == "FAHRENHEIT" and _to == "CELSIUS":
        return (value - 32) * 5/9
    else:
        return "Wrong Statement, Conversion is not possible."


val = int(data[len(data)-4])
_t1 = str(data[len(data)-3])
_t2 = str(data[len(data)-1])

if _t1 == "MILES" or _t1 == "INCHES" or _t1 == "METERS" or _t1 == "FEET":
    print(Distance(val, _t1, _t2), end="\n")
else:
    if _t1 == "GRAMS" or _t1 == "OUNCES" or _t1 == "POUNDS":
        print(Weight(val, _t1, _t2), end="\n")
    else:
        if _t1 == "KILOGRAMS" or _t1 == "KG":
            print(Weight(val, _t1, _t2), end="\n")
        else:
            if _t1 == "CELSIUS" or _t1 == "FAHRENHEIT":
                print(Temperature(val, _t1, _t2), end="\n")
            else:
                print("Wrong Statement, Conversion is not possible.")

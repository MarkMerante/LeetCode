# Jaden Casing Strings

def to_jaden_case(string):
    stringList = string.split()
    return " ".join([x.capitalize() for x in stringList])
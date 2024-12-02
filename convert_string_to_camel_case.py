def to_camel_case(text):      
    return replaceSymbols(text, ["-", "_"])

def replaceSymbols(text,symbols):
    result = []
    capitalizeNext = False
    for char in text:
        print(char)
        if char in symbols:
            print("char in symbols")
            capitalizeNext = True
        else:
            print("char not in symbols")
            if capitalizeNext:
                print(f"char: {char}")
                result.append(char.upper())
                capitalizeNext = False
            else:
                result.append(char)
    return "".join(result)

print(to_camel_case("-aA-B-C")) # theStealthWarrior
def rToI(r):
    if r == "M":
        return 1000
    elif r == "D":
        return 500
    elif r == "C":
        return 100
    elif r == "L":
        return 50
    elif r == "X":
        return 10
    elif r == "V":
        return 5
    elif r == "I":
        return 1
    else:
        print("Fehler rToI(" + r + ")")


def intToRomaniterativ(n):
    if n < 0:
        return "NEGATIV NICHT MÖGLICH"
    if n == 0:
        return ""
    else:
        result = ""
        while n > 0:
            if n >= 1000:
                result += "M"
                n -= 1000
            elif n >= 900:
                result += "CM"
                n -= 900
            elif n >= 500:
                result += "D"
                n -= 500
            elif n >= 400:
                result += "CD"
                n -= 400
            elif n >= 100:
                result += "C"
                n -= 100
            elif n >= 90:
                result += "XC"
                n -= 90
            elif n >= 50:
                result += "L"
                n -= 50
            elif n >= 40:
                result += "XL"
                n -= 40
            elif n >= 10:
                result += "X"
                n -= 10
            elif n >= 9:
                result += "IX"
                n -= 9
            elif n >= 5:
                result += "V"
                n -= 5
            elif n >= 4:
                result += "IV"
                n -= 4
            else :
                result += "I"
                n -= 1
        return result
"""
print("Test Test... 123...")
print("")
print("1: " + intToRomaniterativ(1))
print("0: " + intToRomaniterativ(0))
print("-1: " + intToRomaniterativ(-1))
print("10: " + intToRomaniterativ(10))
print("100: " + intToRomaniterativ(100))
print("1994: " + intToRomaniterativ(1994))
print("3: " + intToRomaniterativ(3))
print("20943: " + intToRomaniterativ(20943)) 
"""
def checkRomanLetters(roma):        # check if only valid letters
    romanNumbers = "IVXLCDM"
    for letter in roma:
        if letter not in romanNumbers:
            return False
    return True

def checkRomanString(roma):        # check if valid Roman Numeral Pattern
    validCombos = ["IV", "IX", "XL", "XC", "CD", "CM"]
    duplicate = False
    for x in range(1, len(roma)):
        if  roma[x-1] ==  roma[x]:
           duplicate = True 
        elif rToI(roma[x-1]) <  rToI(roma[x]):
            if duplicate == True:
                return False
            combo = roma[x-1] + roma[x]
            if combo not in validCombos:
                return False
            duplicate = False
        elif rToI(roma[x-1]) >  rToI(roma[x]):
            duplicate = False
    return True
    
"""
a = checkRomanString("XXL")
print("Testing: ", a)
"""

def romanToIntIterativ(roma):
    if roma == "":
        return 0
    elif isinstance(roma, str) == False:
        return "NOT A STRING!"
    else:
        roma = roma.upper()
        if checkRomanLetters(roma) == False or checkRomanString(roma) == False:
            return "Not a proper Roman Number!"
        else:
            result = rToI(roma[0])
            for x in range(1, len(roma)):
                result += rToI(roma[x])
                if rToI(roma[x-1]) <  rToI(roma[x]):
                    result -= 2 * rToI(roma[x-1])
            return result


"""
print("TEST ")
print("")
print("245: " + str(romanToIntIterativ(245)))
print("AXBL: " + str(romanToIntIterativ("AXBL")))
print("MXX: " + str(romanToIntIterativ("MXX")))
print("MCMXCIV: " + str(romanToIntIterativ("MCMXCIV")))
print("XXL: " , romanToIntIterativ("XXL"))
print("XLX: " , romanToIntIterativ("XLX"))
"""

recResult = ""

def intToRomanRec(n):
    global recResult
    if n < 0:
        return "NEGATIV NICHT MÖGLICH"
    if n == 0:
        result = recResult      # reset the global result var and assign its value to a local var
        recResult = ""
        return result
    else:
        if n >= 1000:
            recResult += "M"
            n -= 1000
        elif n >= 900:
            recResult += "CM"
            n -= 900
        elif n >= 500:
            recResult += "D"
            n -= 500
        elif n >= 400:
            recResult += "CD"
            n -= 400
        elif n >= 100:
            recResult += "C"
            n -= 100
        elif n >= 90:
            recResult += "XC"
            n -= 90
        elif n >= 50:
            recResult += "L"
            n -= 50
        elif n >= 40:
            recResult += "XL"
            n -= 40
        elif n >= 10:
            recResult += "X"
            n -= 10
        elif n >= 9:
            recResult += "IX"
            n -= 9
        elif n >= 5:
            recResult += "V"
            n -= 5
        elif n >= 4:
            recResult += "IV"
            n -= 4
        else :
            recResult += "I"
            n -= 1
        return intToRomanRec(n)

"""
print("----------------------------")
print("test recursive int to Rom:")
print()
print("1: ", intToRomanRec(1))
print("0: ", intToRomanRec(0))
print("-1: ", intToRomanRec(-1))
print("10: ", intToRomanRec(10))
print("100: ", intToRomanRec(100))
print("1994: ", intToRomanRec(1994))
print("3: ", intToRomanRec(3))
print("20943: ", intToRomanRec(20943)) 
"""

import scrypt as sc

#pyflexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def num2dac(value):
    sc.lightNumber(value)

#pyflexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def getValue():
    res = -42
    
    while res < -1:
        try:
            res = int(input())

            if res < -1:
                print("Incorrect input")
        
        except:
            print("Incorrect input")

    return res

#pyflexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

val = 0

while val != -1:
    print("Введите число (-1 для выхода)")

    val = getRightValue()

    num2dac(res)
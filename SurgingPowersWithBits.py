num = int(input("Enter a number: "))

def checkPowerOf2(num):
    if(num == 0):
        return False
    elif((num & (~(num-1))) == num):
        return True

    return False 

print(checkPowerOf2(num))
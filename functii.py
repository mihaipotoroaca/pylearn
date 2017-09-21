# def func(param):
#     # actiuni
#     pass
#     return # optional
#
# def suma (a=1,b=3):
#     s = a + b
#     return s
#
# s = suma([1,2,3], [2,5])
#
# print(s)

# 1 func  - citim de la tast si returnam int
# 2 funt - 2 nr, le comparam
# daca nr 1 >= nr 2 => true daca nu, false
# func 3
# cu output, daca e true, cerem de la tast alt nr
# func 4
# daca e false sa inlocuiasca cu primul numar impar mai mic ca el
def main():
    print("Hi, ")

def citnum():
    a = input('numar= ')
    return int(a)

def compara(nr1 , nr2):
    if nr1 >= nr2:
        return True
    else:
        return False

def impar(a):
    if a%2 == 0:
        a = a-1
    else:
        a = a-2
    return a


nr1 = citnum()
nr2 = citnum()
if compara(nr1, nr2):
    nr1 = citnum()
else:
    nr1 = impar(nr1)

print('nr1= ', nr1)
print('nr2= ', nr2)



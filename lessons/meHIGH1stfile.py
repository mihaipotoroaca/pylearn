#Hello Yall!

def main():
    print('Hello Yall')

if __name__ == '__main__':
    main()

a = 1 #int
b = 'asta e b' #string
c = True #Boolean
l = [] #list
t = (3,4) #tuple

d = {
    'a' : 'val',
    'key': 'value',
    'key2': 2
}

d['key3'] = 'blabla'

print(d)
d.keys()
d.items()
for k, v in d.items():
    print('{} > {}'.format(k, v))

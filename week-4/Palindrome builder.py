str = input("write something here: ")

def plli(x):
    x = list(x)
    x.reverse()
    joined = ''.join(x)
    print(joined)



plli(str)
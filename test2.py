print("this is my new practice")

sen=20
sen_pedar= 50

if sen>20:
    print("hanooz javooni")
    print("sene pedar az",sen_pedar,"rade")

if sen==20:
    print("bozorg shodi")
    print("sene pedar",sen_pedar,"bood?")

if sen<20:
    print("bache saali")
    print("pedar ham ke",sen_pedar,"nashode")

for i in range (1,101):
    #In mishe tavan2?
    print(i,i*i)
    print("----")

for i in {2,3,4,5,6,7}:
    print("8 /",i,"=",8/i)
    print("------")
    
print("8 adad aval nist")
print("--")

def is_prime(n):
    aval=True
    #har adadi bezari to n
    for i in range(2,n):
        if (n%i==0):
            aval=False
    return aval

for i in range(1,1001):
    if is_prime(i):
        print (i, end=", ")

# O (n^lg 3) which beats the regular multiplication algorithm which is O (n^2)

def karatsuba(x,y):
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		n = max(len(str(x)),len(str(y)))
		nby2 = n / 2
		a = x / 10**(nby2)
		b = x % 10**(nby2)
		c = y / 10**(nby2)
		d = y % 10**(nby2)
		ac = karatsuba(a,c)
		bd = karatsuba(b,d)
		ad_plus_bc = karatsuba(a+b,c+d) - ac - bd
		prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd
		return prod

import time

s = time.time()
res1 = karatsuba(12,34)
e = time.time()
t1 = e - s

s = time.time()
res2 = 12*34
e = time.time()
t2 = e - s



if res1 == res2:
    print("Values are equal")
else:
    print("Values are not equal")
print("Karatsuba's Algorithm took {} seconds".format(round(t1, 2)))
print("Normal Multiplication Algorithm took {} seconds".format(round(t2, 2)))

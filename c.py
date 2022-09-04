import time

a = 1
b = 1
z = 30
c = []
for i in range(1, 50):
    b = a + b
    print(b)
    c.append(b)
    a = a + b
    print(a)
    c.append(a)
    time.sleep(0.1)

print(c)
a = 1
b = 6
oa = a
ob = b

r = ''
for i in range(100):
    a %= b
    a *= 10
    r += str(a // b)


found = False
for i in range(1, 51):
    if r[:i] == r[i: 2 * i] and r[:i] == r[2*i: 3*i] and not found:
        print(".".join([str(oa // ob), "(" + str(r[:i]) + ")"]))
        found = True

if not found:
    print(oa/ob)




a = int(input())
f = []
f.append(a)
while a!=0:
    a = int(input())
    f.append(a)
f = f.remove
d=[]
for i in range(len(f)-2):
    if int(f[i]) > int(f[i - 1]) and int(f[i]) > int(f[i + 1]) and i != (len(f) - 1) and i != 0:
        d.append(i)
if len(d)<2:
    print('0')
else:
    print(int(d[-1]) - int(d[0]) - 1)

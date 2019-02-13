values=input().split()
f1=values[0]
s1=values[1]
t1=values[2]
if f1>=s1 and f1>=t1:
    print(f1)
elif s1>=f1 and s1>=t1:
    print(s1)
else:
    print(t1)

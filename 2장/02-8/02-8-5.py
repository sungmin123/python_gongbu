a=[1,2,3]
b=a[:]
a[1]=4
print(a)
print(b)
#b는 a의 복사한 서로 다른 객체이므로 b의값은 변경되지않

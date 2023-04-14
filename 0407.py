# 리스트 - 순서가 있는 sequence
# 모양에 따라서 자료구조가 달라짐.
s={1,2,3}
l=[1,2,3]
print(type(s)) #set
print(type(l)) #list
for i in l:
    print(i)
# add, remove, search 가능
# Once created, you can add, remove, or search for items in the list
## CRUD - 회원가입, 게시판, 블로그, TODO

#s='abc'
#s[0]=1

l=[1,2,3]
l[0]=5
l.append(4)
l.remove(2)

for i in l:
    print(i) # 정석

for i in range(len(l)):
    print(l[i])

print(l)

i = 5 # obj int 'i=5' != 'int i =5'
s = 'abc'

s.split()
s.upper().lower() #-> 객체라서 가능.

l=[1,2,3]
l.append('abc')
l.append(3.14)
l.append([1,2,3])
print(l) # [1, 2, 3, 'abc', 3.14, [1, 2, 3]]

# sort
# sorted -> 원본은 바뀌지 않음.
# * 연산자(unpack) , in 연산자 사용 많이 해보기

s='abcde'
print(s[::-1])

s='a,b,vc,d,e'.split('.')


# (x, y, z) = (5, 6, 7)


print('a' in 'abc')
print(3 in [1,2,3])

s='abc'
print(s[::-1])

s='abc'
print(list(s))

t=(1,2,3)
print(list(t))

print(range(3))
print(list(range(3)))
l=[range(3)]
print(l)

for i in range(3):
    print(i)
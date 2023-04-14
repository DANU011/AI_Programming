text = 'hello, world'
new_text = text.replace('h','r').replace('o','a')
num = 5
f_num = 3.14


print(new_text)

number = 23
guess = int(input('num:'))

if guess == number:
    print('축하합니다.')
elif guess < number:
     print('입력 숫자보다 큽니다.')
else:
     print('입력 숫자보다 작습니다.')
print('end')


fnum= eval(input('fnum :'))
snum= eval(input('snum :'))
tnum= eval(input('tnum :'))

largest = fnum
if snum>largest:
     largest=snum
if tnum>largest:
     largest=tnum
print(str(largest))

#for i in range(n):
#for (auto it : lists)

s_lst=['abc','def','hij']
l_lst=[1,2,3]

for i, s in zip(s_lst,l_lst):
     print(i,s)

dict = {'abc':1,'def':2,'hij':3}
for k,n in dict.items():
     print(k,n)


with open('hello.txt') as f:
     for l in f:
          print(l,end='')

infile = open('fileName.txt', 'r')
for line in infile:
     #indented block of statements
#infile.close()
#FIXME: TEST

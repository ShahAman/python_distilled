#String capitalize
st ="hello world"

print(' '.join([str(w.capitalize()) for w in st.split(' ')]))

#walrus operator (:=)
x=0
while(x := x+1) < 10:
    print(x)

##1.7 File Input and Output
#using with
with open('data.txt') as file:
    for line in file:
        print(line, end='\n')

#without with
file2 = open('data.txt')
for line in file2:
    print(line, end='\n')
file2.close()

with open('data.txt') as file3:
    data = file3.read()

print(data)

#read large file in chunks
with open('data.txt') as file4:
    while (chunk := file4.read(10000)):
        print("-----------")
        print(chunk, end='\n')

principal = 1000
rate = 0.05
numyears = 5
year = 1
with open('out.txt', 'wt') as out:
    while year <= numyears:
        principal = principal * (1 + rate)
        out.write(f'{year:>3d} {principal:0.2f}\n')
        year += 1

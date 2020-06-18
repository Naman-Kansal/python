import string

alpha = string.ascii_lowercase
N = 5
i = 0
j=0
for i in range(N-1,0,-1):
    for j in range(N - i):
        print(alpha[j+1])

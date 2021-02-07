from random import randint
length = int(input("enter seq's length: "))
seq = [randint(-10, 10) for i in range(length)]

S = [0]*len(seq) # создаем спис такой же длины
S[0] = seq[0] # граничные условия

for i in range(1, len(S)):
    S[i] = max(S[i-1] + seq[i], seq[i]) # максимум из предыдущей подсуммы илэлементаи его самого

r_border = 0  # индекс максимального элемента 2 массмива
local_max = S[0]

for k in range(len(S)):
    if S[k] > local_max:
        local_max = S[k]
        r_border = k

j = r_border
l_border = 0

for j in range(r_border, 0, -1):
    if S[j] == S[j-1] + seq[j]:
        l_border = j
        j -= 1
    else:
        break

print(seq)
print(S)
print(j)

print(r_border)




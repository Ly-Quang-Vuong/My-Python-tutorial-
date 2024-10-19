E = int (input())
X = int (input())

if (X < E - 100):
    vztah = ("je o mnoho mensi")
elif (E - 100 <= X < E):
    vztah = ("je mensi")
elif (X == E):
    vztah = ("je stejne")
elif (E < X <= E + 10):
    vztah = ("je vetsi")
elif (E + 10 < X):
    vztah = ("je o mnoho vetsi")

print (f"{X} {vztah}")

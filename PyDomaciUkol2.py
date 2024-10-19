numbers = []
while True:
    b = input()
    if b == "0":
        break

    if b == b[::-1]:      
        numbers.append(int(b))

for num in numbers:
    print(num, end=" ")




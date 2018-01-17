a = [12, 8, 0, 4]
m = min(a)
print("Минимум = %f" % m)

s = 0
i = 0
l = len(a)

while i < l:
    s = s + a[i]
    i += 1

print("Среднее арифметическое = %f" % (s / l))

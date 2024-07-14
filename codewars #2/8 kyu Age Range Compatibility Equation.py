def dating_range(age):
    if age > 14:
        min = age // 2  + 7
        max = (age - 7 )* 2 
    else:
        min = int(age - 0.10 * age)
        max = int(age + 0.10 * age)
    return f"{min}-{max}"

print(dating_range(16))
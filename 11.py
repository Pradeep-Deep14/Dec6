data = [("Alice", 28,"Engineer"),
        ("Bob",34, "Doctor"),
        ("Charlie", 45, "Teacher")]
for name, age, profession in data:
    if age > 30:
        print(f"{name}: {profession}")
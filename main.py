from ops.calculate import calc

print("Exit - выйти")
exp = input("\nВведите выражение\n")
while exp.lower() != "exit":
    print(f"Результат: {calc(exp)}")
    exp = input("\nВведите выражение\n")

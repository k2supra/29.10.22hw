try:
    print("Введіть символ для пошуку")
    sym = int(input("->"))


except Exception as ex:
    print(f"Error", {ex})
try:
    print("Введіть рядок")
    txt = input("->")
    print("Введіть слово для пошуку")
    sym = input("->")
    print("Введіть слово для заміни")
    chn = input("->")


    txxt = txt.replace(sym, chn)
    print(txxt)

except Exception as ex:
    print(f"Error", {ex})


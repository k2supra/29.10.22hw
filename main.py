try:
    print("Введіть символ для пошуку")
    sym = input("->")

    txt = "gsgtgBGGV *4824*+ rf r/757df 7g5 drnywtr wq%*^^#EThb^E&#E"

    exist = sym in txt
    print(exist)


except Exception as ex:
    print(f"Error", {ex})
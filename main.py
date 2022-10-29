try:
    print("Введіть символ для пошуку")
    sym = int(input("->"))

    txt = "gsgtgBGGV *4824*+ rf r/757df 7g5 drnywtr wq%*^^#EThb^E&#E"
    def symbols(tt):
        counter = 0
        for symbols in txt:
            if sym.isdigit():
                counter += 1

        print(f"Nums = {counter}, letters = {len(txt) - counter}")

    def main():
        slova(txt)

    main()

except Exception as ex:
    print(f"Error", {ex})
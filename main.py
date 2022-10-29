try:

    text = int(input("->"))
    def tring(text):
        return text[::-1]
    print()

    def main():
        tring(text)

    main()


except Exception as ex:
    print(f'Error', {ex})
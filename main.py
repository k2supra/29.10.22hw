try:

    text = int(input("->"))
    def tring(tt):
        return text[::-1]
    print()

    def main():
        tring(text)

    main()


except Exception as ex:
    print(f'Error', {ex})
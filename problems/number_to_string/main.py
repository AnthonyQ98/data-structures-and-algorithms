def to_string(number, base):
    convert_string = "0123456789ABCDEF"

    if number < base:
        return convert_string[number]
    else:
        return to_string(number // base, base) + convert_string[number % base]

def main():
    print(to_string(12, 10))

if __name__ == "__main__":
    main()
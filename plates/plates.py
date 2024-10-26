def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
       return(start_with_two_letters(s) and
        length(s) and
        numbers_at_end(s) and
        no_zero_as_first_number(s) and
        no_extra_characters(s))

def start_with_two_letters(s):
      return len(s)>=2 and s[0].isalpha() and s[1].isalpha()

def length(s):
    return True  


def no_extra_characters(s):
      return all(i.isalnum() for i in s)

def numbers_at_end(s):
    for i in range(len(s)):
        if s[i].isdigit():
            return s[i:].isdigit()
    return True

def no_zero_as_first_number(s):
    for i in range(len(s)):
        if s[i].isdigit():
            return s[i] != '0'
    return True

if __name__=="__main__":
    main()

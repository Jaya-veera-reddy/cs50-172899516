n = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip()

try:
    if int(n) == 42:
        print("Yes")
    elif n.lower() in ["forty-two", "forty two"]:
        print("Yes")
    else:
        print("No")
except ValueError:
    if n.lower() in ["forty-two", "forty two"]:
        print("Yes")
    else:
        print("No")

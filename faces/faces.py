def main():
    n=input()
    y=convert(n)
    print(y)

def convert(n):
    n=n.replace(":)","🙂")
    n=n.replace(":(","🙁")
    return(n)


if __name__ == "__main__":
    main()




y = input("File name: ").strip().lower()

if y.endswith(".gif"):
    print("image/gif")
elif y.endswith(".jpg"):
    print("image/jpeg")
elif y.endswith(".jpeg"):
    print("image/jpeg")
elif y.endswith(".png"):
    print("image/png")
elif y.endswith(".pdf"):
    print("application/pdf")
elif y.endswith(".txt"):
    print("text/plain")
elif y.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")

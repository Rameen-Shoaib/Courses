txt = input("File name: ").lower().strip()

txt = txt.split('.')
last = txt[-1]

if last == "gif":
    print("image/gif")
elif last == "jpg" or last == "jpeg":
    print("image/jpeg")
elif last == "png":
    print("image/png")
elif last == "pdf":
    print("application/pdf")
elif last == "txt":
    print("text/plain")
elif last == "zip":
    print("application/zip")
else:
    print("application/octet-stream")
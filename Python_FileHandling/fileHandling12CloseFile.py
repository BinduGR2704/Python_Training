try:
    file = open("sample.txt", "r")
    content = file.read()
    print(content)
except:
    print("File cannot be opened")
finally:
    file.close()
    print("File closed")
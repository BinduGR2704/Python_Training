with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("Created using write mode.\n")
    f.write("Second line.\n")

with open("sample.txt", "r", encoding = "utf-8") as f:
    print(f.read())
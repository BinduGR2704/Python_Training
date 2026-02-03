try:
    with open("file.txt", "x", encoding="utf-8") as f:
        f.write("Created usinf exclsuive mode.\n")

except FileExistsError:
    print("file.txt already exists, exclusive creation aborted.")
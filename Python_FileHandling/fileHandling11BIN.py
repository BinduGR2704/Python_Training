data = b'\x00\x01\x02\x03\x04'
with open("sample.bin", "wb") as f:
    f.write(data)

with open("sample.bin", "rb") as f:
    print(f.read())
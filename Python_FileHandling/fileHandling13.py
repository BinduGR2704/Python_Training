try:
    with open("transaction.log", "w") as f:
        f.write("Transaction successful")
    print("Transaction logged")

except Exception:
    print("Logging failed")


import hashlib
data = input("Enter data: ")

hash_value = hashlib.sha256(data.encode()).hexdigest()

print("\nGenerated SHA-256 Hash:")
print(hash_value)

given_hash = input("\nEnter hash to verify: ")

if hash_value == given_hash:

    print("\nHash verified Successfully!")
    print("The data is authentic and unchanged.")
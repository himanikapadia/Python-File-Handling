with open("sample.txt", "r") as file:
    content = file.read()

words = content.split()

print("📄 File Content:")
print(content)

print(f"\n📝 Total words: {len(words)}")
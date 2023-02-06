data = "hello"
with open("test-rw.txt", "w") as file:
    file.write(data)

with open("test-rw.txt", "r") as file:
    print("====파일 읽기 결과====")
    print(file.read())

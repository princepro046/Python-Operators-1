amount = int(input("Enter Your Amount :"))

notes1000 = amount // 1000
amount = amount % 1000

notes200 = amount // 200
amount = amount % 200

notes100 = amount // 100
amount = amount % 100
print("1000 Notes : , notes1000")
print("200 Notes :", notes200)
print("100 notes :", notes100)




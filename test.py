# print("Hello World", end=" ")
# print("Hello World","world",sep="#")
# print("a" > "b")

x="10.5"
print(int(float(x)))

print("\test\ntesting")
print(r"\test\ntesting")
print("\\test\\ntesting")
print("""hello
testing""")
x="hello"
print(x[0:3:2])#start:end:step
print(x[::-1])#reverse string

for i in range(1,10):
    if i%2==0:
        print(i)
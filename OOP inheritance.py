class phone :
    def call(self):
        print("You can call")

    def message(self):
         print("You can message")


class samsung(phone):
    def photo(self):
        print("You can take a photo")


print("For samsung...")
s = samsung()
s.call()
s.message()
s.photo()

print("\n")

print("For phone...")
p = phone()
p.message()
p.call()
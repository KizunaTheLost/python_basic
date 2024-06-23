# username = input("Enter you username:")
# password = input("Enter you password:")

# print(username, password)
# pip list
# pip install cameLcase
# python.exe -m pip install --upgrade pip
import camelcase
camel = camelcase.CamelCase()
txt = "hello world"
print(camel.hump(txt))
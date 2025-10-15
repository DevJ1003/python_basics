# WAP to check a string for alphanumeric characters
# isnumeric(), isdigit(), isdecimal(), islower(), isupper(), isspace(), istitle()

a = "hello"
b = "123Hello"
c = "123456"
d = "HELLO"
e = " "
f = "Hello 123"
g = "1.123"

print(a, a.isalnum())
print(b, b.isalnum())
print(c, c.isalnum())
print(d, d.isalnum())
print(e, e.isalnum())
print(f, f.isalnum())
print(g, g.isalnum())
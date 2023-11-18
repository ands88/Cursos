# dir, hasattr e getattr em Python

string = "Anderson"
method = "upper"

if hasattr(string, "upper"):
    print("Existe upper")
    print(getattr(string, method)())
else:
    print("Não existe o método", method)

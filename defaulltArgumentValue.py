# Belajar method Default Argumen Value 

def sayHello(firstName="Agitha", lastName=""):
    print(f"Hello {firstName} {lastName}")

sayHello("Gege", "Cantiq") # parameter disini jadi optional
sayHello()
sayHello(lastName="Huimin")
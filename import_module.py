color = 'red'
food = 'rice'

def cap_color():
    print('red'.capitalize())

def greetings(name):
    return "Good night", name

print(__name__, type(__name__))
cap_color()
# you can run your file by passing it to an interpreter - "__main__"
# import your file as a module - "modulename" and in this case "import_module"
def main():
    greetings('uoe')
    cap_color()

if __name__ == "__main__":
    main()

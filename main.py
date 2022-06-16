import eel

eel.init('webinterface', allowed_extensions=['.js', '.html'])

@eel.expose
def print_sum(a, b):
    print(a + b)

print_sum(1, 2)
eel.start('templates/main.html')

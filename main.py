import eel

eel.init('webinterface', allowed_extensions=['.js', '.html'])

@eel.expose
def print_sum_py(a, b):
    print(str(a + b))

print(eel._exposed_functions)


eel.start('templates/main.html', port=8001)

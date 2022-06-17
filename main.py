import eel

eel.init('webinterface', allowed_extensions=['.js', '.html'])

eel.start('templates/main_tab.html', port=8001, jinja_templates='templates', geometry={'position': (0,0)})

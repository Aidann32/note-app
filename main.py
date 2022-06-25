import eel

from db import DBStarter

eel.init('webinterface', allowed_extensions=['.js', '.html'])

db_starter = DBStarter('notes', 'sqlite')
print(db_starter.create_database())

eel.start('templates/base.html', port=8001, jinja_templates='templates', geometry={'position': (0,0)})

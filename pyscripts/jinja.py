from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("webinterface"),
    autoescape=select_autoescape()
)

template = env.get_template("main.html")
from flask import Blueprint


harbour_theme = Blueprint(
    "harbour_theme", __name__)


def page():
    return "Hello, harbour_theme!"


harbour_theme.add_url_rule(
    "/harbour_theme/page", view_func=page)


def get_blueprints():
    return [harbour_theme]

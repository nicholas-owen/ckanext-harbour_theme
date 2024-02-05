import ckan.plugins.toolkit as tk


def harbour_theme_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "harbour_theme_required": harbour_theme_required,
    }

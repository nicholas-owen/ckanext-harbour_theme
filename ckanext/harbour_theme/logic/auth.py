import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def harbour_theme_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "harbour_theme_get_sum": harbour_theme_get_sum,
    }

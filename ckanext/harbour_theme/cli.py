import click


@click.group(short_help="harbour_theme CLI.")
def harbour_theme():
    """harbour_theme CLI.
    """
    pass


@harbour_theme.command()
@click.argument("name", default="harbour_theme")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [harbour_theme]

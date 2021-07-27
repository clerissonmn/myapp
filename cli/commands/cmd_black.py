import subprocess

import click


@click.command()
@click.argument("path", default="myapp")
def cli(path):
    """
    Run black to format your code base.

    :param path: Test coverage path
    :return: Subprocess call result
    """

    cmd = f"black -v {path}"
    return subprocess.call(cmd, shell=True)

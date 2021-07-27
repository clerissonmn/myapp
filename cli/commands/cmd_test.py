import os
import subprocess

import click


@click.command()
@click.argument("path", default=os.path.join("tests"))
def cli(path):
    """
    Run tests with Pytest.

    :param path: Test path

    :return: Subprocess call result
    """
    cmd = f"pytest {path} -v --cov='myapp'"
    return subprocess.call(cmd, shell=True)

import boa
import click

from scripts.deploy import deploy_commands
from scripts.tests import test_commands
from settings.config import settings
from settings.logger import setup_logger

setup_logger()


@click.group("commands")
def commands():
    ...


if __name__ == "__main__":
    if settings.DEBUG:
        boa.env.fork(settings.WEB3_PROVIDER_URL)
    else:
        boa.set_network_env(settings.WEB3_PROVIDER_URL)
        # boa.env.add_account()

    commands.add_command(deploy_commands)
    commands.add_command(test_commands)
    commands()
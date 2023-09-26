import logging
from pathlib import Path

import click
import coloredlogs


logger = logging.getLogger(__name__)


def reset_log_handlers() -> None:
    logging.root.handlers = []


def setup_logs(log_file_path: Path, console_log: bool) -> None:
    logging.root.setLevel(logging.NOTSET)

    fmt = "%(asctime)s | %(name)-20s | %(levelname).1s | %(message)s"

    file_handler = logging.FileHandler(str(log_file_path))
    file_handler.setFormatter(logging.Formatter(fmt))
    logging.root.addHandler(file_handler)

    if console_log:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(coloredlogs.ColoredFormatter(fmt))
        logging.root.addHandler(console_handler)


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option(
    '-w',
    '--log-dir',
    type=click.Path(path_type=Path, file_okay=False, writable=True),
    default=Path.cwd(),
    help='Path to store log',
)
@click.option('-v', '--verbose', is_flag=True, default=False, help='Show logs')
def main(log_dir: Path, verbose: bool) -> None:
    setup_logs(log_dir / 'debug.log', verbose)
    logger.info("This is info")
    logger.debug("This is debug")
    logger.warning("This is warning")


if __name__ == '__main__':
    main()

from pathlib import Path

from patchright.sync_api import Page


def install_mouse_helper(page: Page) -> None:
    page.add_init_script(path=Path(__file__).parent.joinpath("../js/mouseHelper.js"))

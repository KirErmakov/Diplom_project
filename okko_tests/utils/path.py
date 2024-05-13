from pathlib import Path


def relative_from_root(path):
    return Path(__file__).parent.parent.joinpath(path).absolute().__str__()

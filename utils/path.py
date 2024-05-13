from pathlib import Path


def relative_from_root(path):
    return Path(__file__).parent.parent.joinpath(path).absolute().__str__()


def schema_path(file_name):
    return str(
        Path(__file__).parent.parent.joinpath(file_name).absolute()
    )

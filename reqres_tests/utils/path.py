from pathlib import Path


def schema_path(file_name):
    return Path(__file__).parents[2].joinpath('schemas', file_name)

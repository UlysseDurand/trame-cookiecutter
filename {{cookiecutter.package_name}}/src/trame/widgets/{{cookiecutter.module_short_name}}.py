from {{cookiecutter.import_name}}.widgets.{{cookiecutter.module_short_name}} import *  # noqa: F403


def initialize(server):
    from {{cookiecutter.import_name}} import module  # noqa: PLC0415

    server.enable_module(module)

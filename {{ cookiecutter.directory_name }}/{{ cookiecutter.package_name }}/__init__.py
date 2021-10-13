from importlib.metadata import PackageNotFoundError, version

from {{ cookiecutter.package_name }}.module import {{ cookiecutter.module_class_name }}

__all__ = ["{{ cookiecutter.module_class_name }}"]

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    # package is not installed
    pass

from importlib.metadata import PackageNotFoundError, version

from {{ cookiecutter.package_name }}.module import {{ cookiecutter.module_class_name }}

__all__ = ["{{ cookiecutter.module_class_name }}"]

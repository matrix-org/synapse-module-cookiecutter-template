# {{ cookiecutter.module_human_name }}

{{ cookiecutter.package_description }}


## Installation

From the virtual environment that you use for Synapse, install this module with:
```shell
pip install path/to/{{ cookiecutter.directory_name }}
```

Then alter your homeserver configuration, adding to your `modules` configuration:
```yaml
modules:
  - module: {{ cookiecutter.package_name }}.{{ cookiecutter.module_class_name }}
    config:
      # TODO: Complete this section with an example for your module
```


## Development

In a virtual environment, use:
```shell
pip install -e .[dev]
```

To run the unit tests, you can either use:
```shell
tox -e py
```
or
```shell
trial tests
```

To run the linters and `mypy` type checker, use `./scripts-dev/lint.sh`.


## Releasing

The exact steps for releasing will vary; but this is an approach taken by the
Synapse developers (assuming a Unix-like shell):

 1. Set a shell variable to the version you are releasing (this just makes
    subsequent steps easier):
    ```shell
    version=X.Y.Z
    ```

 2. Branch off from `{{ cookiecutter.main_git_branch }}` to `release-vX.Y.Z`:
    ```shell
    git checkout {{ cookiecutter.main_git_branch }}
    git checkout -b release-v$version
    ```

 3. Update `setup.py` so that the `version` is correct.

 4. Invoke `towncrier --version v$version` to generate the changelog.
    It's OK for `towncrier` to remove the newsfragments.

 5. Check the changelog `CHANGES.md` and make corrections if necessary.

 6. Stage the changed files and commit.
    ```shell
    git add -u
    git commit -m v$version -n
    ```

 7. Push your changes.
    ```shell
    git push -u origin release-v$version
    ```

 8. You can still check the changelog here (or even ask others to do so).
    If you make any corrections, stage, commit and push them once more.

 9. When ready, create a signed tag for the release:
    ```shell
    git tag -s v$version
    ```
    Base the tag message on the changelog.

10. Push the tag.
    ```shell
    git push origin tag v$version
    ```

11. If applicable:
    Create a *release*, based on the tag you just pushed, on GitHub or GitLab.

12. If applicable:
    Create a source distribution and upload it to PyPI.

# Synapse Module Cookiecutter Template

This is a [Cookiecutter] template for creating new [Synapse] modules.

[Cookiecutter]: https://pypi.org/project/cookiecutter/
[Synapse]: https://github.com/matrix-org/synapse

What you get:

* a Synapse module package
* a `README` with basic instructions on installation, development and releasing
* `setup.py` metadata
* CI configurations for
  * GitHub Actions
  * GitLab
* code checking tools (invokable with `tox`, checked in CI)
  * code formatting using `black` and `isort`
  * code style checking using `flake8`
  * type checking using `mypy` (with checking against Synapse supported in
    Synapse 1.46 and later)
    * strict by default (configurable in `mypy.ini`)
* unit testing using `trial` (invokable with `tox`, checked in CI)
* changelog management using `towncrier`

Please refer to [the Synapse 'Writing a module' documentation][synapse_writemodule]
for descriptions and examples (at the bottom of most pages) of using the Synapse
module API, including registering callbacks.

[synapse_writemodule]: https://matrix-org.github.io/synapse/develop/modules/writing_a_module.html

## How to use this template

### Install Cookiecutter

To use this template, you will first need to install Cookiecutter.

Full instructions to do so can be found in [the Cookiecutter documentation](https://cookiecutter.readthedocs.io/en/stable/installation.html),
but in summary, `pip install --user cookiecutter` or `sudo apt install cookiecutter`
will do if you use `pip` or `apt`.


### Use Cookiecutter to get your project going

`cd` to a directory where you would like to create a new project as a subdirectory, then run
```shell
cookiecutter https://github.com/matrix-org/synapse-module-cookiecutter-template.git
```

You will then be asked a series of questions to populate your project:

1. `directory_name`: Specify the name of a project directory.
   This directory will be created.
2. `module_human_name`: Specify a human-readable module name here.
   This is used in the `README` file and the changelog.
3. `package_description`: Specify a human-readable module description.
   This is used in the `README` file and `setup.py` file.
4. `package_name`: Specify a **snake_case** Python package name here.
   This will be used as the package name for your module.
5. `module_class_name`: Specify a **PascalCase** Python class name here.
   This will be used as the class name for your module class.
6. `author_name`: Specify your name here, to be used in the Python package
   metadata in `setup.py`.
7. `author_email`: Specify your e-mail address here, to be used in the Python package
   metadata in `setup.py`.
8. `towncrier_pr_link_format`: Specify a template for how links to pull requests
   or merge requests will appear in the changelog.
   `{issue}` will be substituted with the PR/MR number.
   For GitHub, `[\#{issue}](https://github.com/me/my-repo/issues/{issue})` is sensible;
   just replace `me/my-repo`.
   For GitLab, `[\!{issue}](https://my.gitlab.example.org/me/my-repo/-/merge_requests/{issue})` is sensible;
   just replace `my.gitlab.example.org` and `me/my-repo`.
9. `main_git_branch`: Specify the name of your main Git branch here.
   Although this template does not initialise a Git repository automatically,
   the changelog linter script depends on it.
   This is commonly `main`, `master` or `develop`.

If all goes well, you should now have a project starter!


### Set up Git

What you do from here on is up to you!

However, it's probably worth initialising a Git repository and making the first
commit be exactly what is produced by this template.
(Doing this may make it easier to upgrade an existing project to a later version
of the template in the future: you could branch off from the initial commit,
re-run the template generator, commit, and then merge that branch into your main
branch.)

If you use GitHub or GitLab, you should use their web interface to enable the
included CI configuration.


## Notes for developing this template

During development, you can clone this repository and call
```shell
cookiecutter path/to/synapse-module-cookiecutter-template
```
when needed, to test your changes.

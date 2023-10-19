# Synapse Module Cookiecutter Template

This is a [Cookiecutter] template for creating new [Synapse] modules.

[Cookiecutter]: https://pypi.org/project/cookiecutter/
[Synapse]: https://github.com/matrix-org/synapse

What you get:

* a Synapse module package
* a `README` with basic instructions on installation, development and releasing
* `setup.cfg` metadata (the declarative equivalent of `setup.py`)
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
* *Specific to the 'Synapse Team' variant:*
  * `CODEOWNERS` for automatic review requests for the `synapse-core` team on
    GitHub when a pull request is opened
  * The Apache 2.0 licence with copyright notices

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
   This is used in the `README` file and `setup.cfg` file.
4. `package_name`: Specify a **snake_case** Python package name here.
   This will be used as the package name for your module.
5. `module_class_name`: Specify a **PascalCase** Python class name here.
   This will be used as the class name for your module class.
6. `main_git_branch`: Specify the name of your main Git branch here.
   Although this template does not initialise a Git repository automatically,
   the CI configuration and suggested release instructions mention it.
   This is commonly `main`, `master`, `trunk`, `default` or `develop`.
7. `variant`: Choose whether or not to include the 'Synapse Team'-specific
   customisations; pick `synapse_team` if the module will be maintained
   by the Synapse Team. Otherwise, pick `standard`.
8. `use_scm_version`: Choose whether to use SCM info to set the version of the module.
   This will use `setuptools_scm` for that, so check its manual for more info.


If all goes well, you should now have a project starter!


### Set up Git

What you do from here on is up to you!

However, it's probably worth initialising a Git repository and making the first
commit be exactly what is produced by this template.
(Doing this may make it easier to upgrade an existing project to a later version
of the template in the future: you could branch off from the initial commit,
re-run the template generator, commit, and then merge that branch into your main
branch.)

If you use GitHub or GitLab, you should use its web interface to enable the
included CI configuration.


## Notes for developing this template

During development, you can clone this repository and call
```shell
cookiecutter path/to/synapse-module-cookiecutter-template
```
when needed, to test your changes.

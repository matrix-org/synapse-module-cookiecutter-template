# We use a Python script as a post-generation hook because that's more portable
# (mainly with respect to Windows)
import subprocess
import sys

# this will be substituted by cookiecutter.
main_branch_name = '{{ cookiecutter.main_git_branch }}'

try:
    subprocess.run(
        ['git', 'init', '--initial-branch', main_branch_name]
    )
except subprocess.CalledProcessError:
    print(
        "Unable to initialise git repository! "
        f"Please do so with branch name: '{main_branch_name}'",
        file=sys.stderr
    )

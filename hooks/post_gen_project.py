# We use a Python script as a post-generation hook because that's more portable
# (mainly with respect to Windows)
import subprocess
import sys
import os

# this will be substituted by cookiecutter.
main_branch_name = '{{ cookiecutter.main_git_branch }}'

# we use this to remove optional files
variant_name = '{{ cookiecutter.variant }}'

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

# Remove files that don't correspond to this variant
files_to_remove = []

if variant_name != 'synapse_team':
    files_to_remove = [
        ".github/CODEOWNERS",
        "LICENSE"
    ]

for file_to_remove in files_to_remove:
    os.unlink(file_to_remove)

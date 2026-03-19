# Changelog

## v0.3.2 (2026-03-19)

Migrate GitHub Actions publish workflow to OIDC trusted publishing,
removing the need for API token secrets. No changes to package
functionality.

## v0.3.1 (2026-03-19)

Fix broken GitHub Actions publish workflow: updated `actions/setup-python`
from `v1` to `v5` and switched Python version spec from the unavailable
`3.10.5` to `"3.x"`. No changes to package functionality.

## v0.3 (2026-03-19)

- Added working tree status to output of `print_cwd_git_version()`:
  appends `(working tree clean)` or `(working tree dirty)` depending on
  whether there are unstaged changes to tracked files.
- Added optional `print_timestamp` parameter to prepend the current
  system time to the output.
- Fixed `NameError` when `print_timestamp=True` (variable was misnamed
  `output_str` instead of `output_string`).
- Added nox-based test infrastructure.
- Dropped support for Python 3.8 and 3.9.

## v0.2

Initial stable release with support for Python 3.8+. Returns a
one-line string with the git repository name, current branch, and
short commit hash.

## v0.1

First public release.

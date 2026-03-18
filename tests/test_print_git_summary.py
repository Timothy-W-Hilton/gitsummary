import gitsummary

def test_print_cwd_git_version_no_timestamp():
    s = gitsummary.print_cwd_git_version()
    print(s)

def test_print_cwd_git_version_with_timestamp():
    s = gitsummary.print_cwd_git_version(print_timestamp=True)
    print(s)

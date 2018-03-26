# Example of setuptools bug

The following is an example showing how setuptools fails when running unit
tests with a custom test runner.

Uses setuptools version **39.0.1** on **Ubuntu 17.10**

## Usage

In the root of the package, run the following:

    > python -m setup.py test -r main.runner.TestRunner

    running test
    running egg_info
    writing setuptools_example.egg-info/PKG-INFO
    writing dependency_links to setuptools_example.egg-info/dependency_links.txt
    writing top-level names to setuptools_example.egg-info/top_level.txt
    reading manifest file 'setuptools_example.egg-info/SOURCES.txt'
    writing manifest file 'setuptools_example.egg-info/SOURCES.txt'
    running build_ext
    Traceback (most recent call last):
      File "setup.py", line 12, in <module>
        include_package_data=True,
      File "/home/user/.virtualenvs/setuptools_bug/lib/python3.6/site-packages/setuptools/__init__.py", line 129, in setup
        return distutils.core.setup(**attrs)
      File "/usr/lib/python3.6/distutils/core.py", line 148, in setup
        dist.run_commands()
      File "/usr/lib/python3.6/distutils/dist.py", line 955, in run_commands
        self.run_command(cmd)
      File "/usr/lib/python3.6/distutils/dist.py", line 974, in run_command
        cmd_obj.run()
      File "/home/user/.virtualenvs/setuptools_bug/lib/python3.6/site-packages/setuptools/command/test.py", line 226, in run
        self.run_tests()
      File "/home/user/.virtualenvs/setuptools_bug/lib/python3.6/site-packages/setuptools/command/test.py", line 247, in run_tests
        testRunner=self._resolve_as_ep(self.test_runner),
      File "/home/user/.virtualenvs/setuptools_bug/lib/python3.6/site-packages/setuptools/command/test.py", line 268, in _resolve_as_ep
        return parsed.resolve()()
      File "/home/user/.virtualenvs/setuptools_bug/lib/python3.6/site-packages/pkg_resources/__init__.py", line 2297, in resolve
        module = __import__(self.module_name, fromlist=['__name__'], level=0)
    ModuleNotFoundError: No module named 'main.runner.TestRunner'

As you can see, the tests do run if I omit the custom test runner.

    $ python -m setup.py test

    running test
    running egg_info
    writing setuptools_example.egg-info/PKG-INFO
    writing dependency_links to setuptools_example.egg-info/dependency_links.txt
    writing top-level names to setuptools_example.egg-info/top_level.txt
    reading manifest file 'setuptools_example.egg-info/SOURCES.txt'
    writing manifest file 'setuptools_example.egg-info/SOURCES.txt'
    running build_ext
    test_hello (main.tests.TestMain) ... ok

    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK

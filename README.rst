======
iniget
======

A command-line tool to extract, normalize, and JSONify values from an
`iniherit <https://pypi.python.org/pypi/iniherit>`_ -enabled "INI"
file.


Installation
============

.. code-block:: bash

  $ pip install iniget


Usage
=====

Given the following two files, ``base.ini``:

.. code-block:: ini

  [sect1]
  foo = bar

and ``config.ini``:

.. code-block:: ini

  [DEFAULT]
  %inherit = base.ini

The following will extract the inherited ``foo`` value:

.. code-block:: bash

  $ iniget config.ini sect1 foo
  bar

Much more is possible, including:

* listing sections
* listing options
* JSON-encoding the configuration
* JSON-interpreting option values
* Control case-sensitivity, interpolation, and default values


Options
=======

* ``-s SECTION, --section SECTION``

  Specify additional sections to extract from; can be specified
  multiple times to add multiple sections.

* ``-C, --no-case``

  Handle option names case insensitively.

* ``-I, --no-inherit``

  Disable processing of "%inherit" directives.

* ``-E, --no-expansion``

  Disable ConfigParser option expansion ("interpolation").

* ``-F, --no-fallback``

  Disables falling back to the raw option value when an option value
  cannot be interpolated (this generally happens when it is
  incorrectly formatted or it references undefined substitutions),
  and causes an exception to be thrown.

* ``-K, --list-options``

  List the option names only, not the values.

* ``-S, --list-sections``

  List the section names only.

* ``-J, --json-parse``

  If option values are JSON-parseable, parse as such; additionally,
  the following are interpreted as boolean values: 'yes', 'true',
  'on', 'off', 'no', 'false'.

* ``-j, --json-output``

  Render the output using JSON syntax.

* ``-d JSON, --defaults JSON``

  Set the ConfigParser default values from this JSON-parsed
  dictionary.

* ``-r, --raw``

  Don't do anything fancy: show exactly what ConfigParser interprets
  (requires exactly one section and one option); note that options
  "--no-case", "--no-inherit", "--no-expansion" and "--defaults" are
  still honored, but "--json-parse" is not.

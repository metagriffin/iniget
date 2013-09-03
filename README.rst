======
iniget
======

A command-line tool to extract values from an iniherit-enabled "INI"
file.


Installation
============

.. code-block:: bash

  $ pip install iniget


Usage
=====

.. code-block:: bash

  $ cat base.ini
  [sect1]
  foo = bar

  $ cat config.ini
  [DEFAULT]
  %inherit = base.ini

  $ iniget config.ini foo
  bar


Options
=======

* 
``coroner``
===========

Wraps python invocations in code to do post-mortem debugging
and sundry usefulnesses.

``coroner`` was adapted from a stackoverflow.com `response`_
by `synthesizerpatel`_.

.. _response: http://stackoverflow.com/questions/3911624/3911725#3911725
.. _synthesizerpatel: http://stackoverflow.com/users/210613/synthesizerpatel


Usage
-----

``coroner`` is meant to be used as a command line module,
invoked with code like::

    python -m coroner some_sketchy_module.py

When the sketchy script invariably throws an exception,
``coroner`` will initiate a ``pdb.pm`` post-mortem debugging session.

You can also use it in the other ways that ``python`` can be used
on the command line, e.g. with ``-c`` or ``-``.


Bugs
----

That's all, folks.  I might add more sometime soon.

Oh yeah, it doesn't do recursive module invocation yet.

Also I haven't really tested it, just tried it with ``-c`` a couple of times.

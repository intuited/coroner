``coroner``
===========

Wraps python invocations in code to do post-mortem debugging
and sundry usefulnesses.

Usage
-----

``coroner`` is meant to be used as a command line module,
invoked with code like::

    python -m coroner some_sketchy_module.py

When the sketchy script invariably throws an exception,
``coroner`` will initiate a ``pdb.pm`` post-mortem debugging session.


Bugs
----

That's all, folks.  I might add more sometime soon.

Oh yeah, it doesn't do module invocation yet.

Also I haven't really tested it, just tried it with ``-c`` a couple of times.

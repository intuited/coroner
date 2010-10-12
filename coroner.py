"""Sets up a sys.excepthook that launches ``pdb.pm``.

Adapted from a stackoverflow.com `response`_ by `synthesizerpatel`_.

The main point of this module is to pass it via::

    python -m coroner some_sketchy_python_script.py

which will run that script with a post-mortem debugger enabled.

This ended up being sort of complicated,
mostly because ``argparse`` doesn't provide a way
to have an option-style parameter consume all remaining arguments.

.. _response: http://stackoverflow.com/questions/3911624/3911725#3911725
.. _synthesizerpatel: http://stackoverflow.com/users/210613/synthesizerpatel
"""
from contextlib import contextmanager
def info(type, value, tb):
    import sys
    if hasattr(sys, 'ps1') or not sys.stderr.isatty():
        # we are in interactive mode or we don't have a tty-like
        # device, so we call the default hook
        sys.__excepthook__(type, value, tb)
    else:
        import traceback, pdb
        # we are NOT in interactive mode, print the exception...
        traceback.print_exception(type, value, tb)
        print
        # ...then start the debugger in post-mortem mode.
        pdb.pm()

def inquest():
    import sys
    do = parse_args(sys.argv)
    return act(do)

def cmdline_help():
    from textwrap import dedent
    return dedent("""\
        python -m coroner [-h] [-c COMMAND | -m MODULE | - | SCRIPTNAME
                                [ARG [ARG ..] ] ]

        The coroner module wraps a python invocation
        with post-mortem interactive debugging.

        This just wraps a normal Python invocation with an exception handler
        that starts a post-mortem ``pdb`` session.

        The invocation can be passed as one of
            -c COMMAND [ARG [ARG ..] ]
            -m MODULE [ARG [ARG ..] ]
            - [ARG [ARG .. ] ]
            SCRIPTNAME [ARG [ARG ..] ]

        Additional ARGs are passed on to the invoked code.

        The ``-`` argument indicates
        that commands are to be read from standard input.
        """)

def parse_args(args):
    """Parses ``args`` in an appropriate manner.

    This works in vaguely the same way as python itself:
    
    -   The argument following -c is considered a command
    -   The argument following -m is considered a module name
    -   The argument "-" invokes import from standard input
    -   Any other `-*` argument is an OptionError exception
    -   Anything else is a filename to be executed.

    Further arguments following those ones are considered
    arguments to be passed in ``sys.argv``
    to the code determined by the above method.

    Returns either
    -   a dict keying 'help' to some text, or
    -   a dict containing one of 'cmd', 'file', or 'filename',
        as well as a tuple 'args' which contains the remaining arguments.
    """
    import sys
    args = iter(args)
    this_module = args.next()
    do = {}
    for arg in args:
        if arg in ('-h', '--help'):
            do['help'] = cmdline_help()
        elif arg == '-m':
            print ("Modules are not yet supported by the coroner's office.  "
                   "Try back later.")
            exit(1)
        elif arg in ('-c', '--cmd'):
            do['cmd'] = args.next()
            do['args'] = ['-c'] + list(args)
        elif arg == '-':
            do['file'] = sys.stdin
            do['args'] = ['-'] + list(args)
        elif arg[0] == '-':
            raise OptionError('Unknown option: {0}'.format(arg))
        else:
            do['filename'] = args.next()
            do['args'] = [do['filename']] + list(args)

    return do

@contextmanager
def swap_argv(args):
    import sys
    old_argv = sys.argv
    sys.argv = args
    yield
    sys.argv = old_argv

def act(do):
    if do.has_key('help'):
        print do['help']
        exit(0)
    else:
        with swap_argv(do['args']):
            import sys
            sys.excepthook = info
            new_dict = {}
            if do.has_key('file'):
                exec do['file'] in new_dict
            elif do.has_key('filename'):
                execfile(do['filename'], new_dict)
            elif do.has_key('cmd'):
                exec do['cmd'] in new_dict
            elif do.has_key('module'):
                return NotImplemented

if __name__ == '__main__':
    inquest()

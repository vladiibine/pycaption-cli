pycaption-cli
=============

A command line interface for the pycaption module.

Setup
=====

    python setup.py install

Usage
=====

From your command line:

    pycaption <path to caption file> [--sami --dfxp --srt --transcript]
    
e.g.

    pycaption ../caption.scc --dfxp --transcript

Output is written to the screen. To write to a file, use something like this:

    pycaption ../caption.scc --dfxp > caption.xml

Supported Formats
=================

 - SCC (read)
 - SRT (read/write)
 - SAMI (read/write)
 - DFXP (read/write)
 - VTT (read/write)
 - Transcript (write)

Extra parameters
=================

 - read_invalid_positioning (a bool parameter with this key will be passed to all readers who accept it)

License
=======

This module is Copyright 2012 Joe Norton and is available under the [Apache License, Version 2.0][1].

[1]: http://www.apache.org/licenses/LICENSE-2.0

pycaption-cli
=============

A command line interface for the pycaption module.

Setup
=====

    python setup.py install

Usage
=====

From your command line:

    pycaption <path to caption file> [--sami --dfxp --srt --transcript --vtt --unpositioned_dfxp]
    
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

 - ```--read_invalid_positioning``` (a bool parameter with this key will be passed to all readers who accept it). This parameter has effect only on the DFXPReader currently. Its effect is that the reader will try to parse positioning info the best it can, even if it doesn't conform to the specs (for instance attributes like ```tts:origin``` that are specified on elements where they should have no meaning.

- ```--video_height``` and ```--video_width```. These will serve when converting to webvtt, if the input source file has units other than percents. WebVTT will only output percent units, but in order to do this, the video height and witdh must be specified (so we know that 32px means 5% of 640 for instance)

- ```--unpositioned_dfxp```. This acts like ```--dfxp```, but the file it outputs, will only contain a default positioning of bottom center, for every caption

License
=======

This module is Copyright 2012 Joe Norton and is available under the [Apache License, Version 2.0][1].

[1]: http://www.apache.org/licenses/LICENSE-2.0

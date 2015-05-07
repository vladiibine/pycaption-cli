import optparse
import codecs

import pycaption
import pycaption.dfxp


def main():
    parser = optparse.OptionParser("usage: %prog [options]")
    parser.add_option("--sami",
            action='store_true',
            dest='sami',
            help="write captions in SAMI format",
            default=False,)
    parser.add_option("--dfxp",
            action='store_true',
            dest='dfxp',
            help="write captions in DFXP format",
            default=False,)
    parser.add_option(
        "--unpositioned_dfxp",
        action='store_true',
        dest='unpositioned_dfxp',
        help="write captions in DFXP format, ignoring all positioning "
             "information (will only use a default of bottom center)",
        default=False,)
    parser.add_option("--srt",
            action='store_true',
            dest='srt',
            help="write captions in SRT format",
            default=False,)
    parser.add_option("--vtt",
            action='store_true',
            dest='vtt',
            help="write captions in WebVTT format",
            default=False,)        
    parser.add_option("--transcript",
            action='store_true',
            dest='transcript',
            help="write transcript for captions",
            default=False,)
    parser.add_option("--scc_lang",
            dest='lang',
            help="choose override language for input",
            default='',)
    parser.add_option("--scc_offset",
            dest='offset',
            help="choose offset for SCC file; measured in seconds",
            default=0)
    parser.add_option(
        "--read_invalid_positioning",
        dest="read_invalid_positioning",
        help="Whether to try to read the invalidly specified positioning "
             "information",
        action="store_true",
        default=False
    )
    parser.add_option(
        "--video_height",
        dest="video_height",
        help="Required for relativization (converting measuring units to "
             "percents). WebVTT requires the relativization of all units",
        action="store"
    )
    parser.add_option(
        "--video_width",
        dest="video_width",
        help="Required for relativization (converting measuring units to "
             "percents). WebVTT requires the relativization of all units",
        action="store"
    )

    (options, args) = parser.parse_args()

    try:
        filename = args[0]
    except:
        raise Exception(
        ('Expected usage: python caption_converter.py <path to caption file> ',
        '[--sami --dfxp --srt --transcript --vtt --unpositioned_dfxp]'))

    try:
        captions = codecs.open(filename, encoding='utf-8', mode='r').read()
    except:
        captions = open(filename, 'r').read()
        captions = unicode(captions, errors='replace')

    content = read_captions(captions, options)
    write_captions(content, options)


def read_captions(captions, options):
    reader_kwargs = {
        'read_invalid_positioning': options.read_invalid_positioning}

    scc_reader = pycaption.SCCReader(**reader_kwargs)
    srt_reader = pycaption.SRTReader(**reader_kwargs)
    sami_reader = pycaption.SAMIReader(**reader_kwargs)
    dfxp_reader = pycaption.DFXPReader(**reader_kwargs)
    vtt_reader = pycaption.WebVTTReader(**reader_kwargs)

    if scc_reader.detect(captions):
        if options.lang:
            return scc_reader.read(captions, lang=options.lang,
                                   offset=int(options.offset))
        else:
            return scc_reader.read(captions, offset=int(options.offset))
    elif srt_reader.detect(captions):
        return srt_reader.read(captions)
    elif sami_reader.detect(captions):
        return sami_reader.read(captions)
    elif dfxp_reader.detect(captions):
        return dfxp_reader.read(captions)
    elif vtt_reader.detect(captions):
        return vtt_reader.read(captions)    
    else:
        raise Exception('No caption format detected :(')


def write_captions(content, options):
    writer_kwargs = {
        'video_width': int(options.video_width) if options.video_width else None,   # noqa
        'video_height': int(options.video_height) if options.video_height else None  # noqa
    }
    if options.sami:
        print(pycaption.SAMIWriter(**writer_kwargs).write(content).encode("utf-8"))  # noqa
    if options.dfxp:
        print(pycaption.DFXPWriter(**writer_kwargs).write(content).encode("utf-8"))  #noqa
    if options.srt:
        print(pycaption.SRTWriter(**writer_kwargs).write(content).encode("utf-8"))  # noqa
    if options.transcript:
        print(pycaption.TranscriptWriter(**writer_kwargs).write(content).encode("utf-8"))  # noqa
    if options.vtt:
        print(pycaption.WebVTTWriter(**writer_kwargs).write(content).encode("utf-8"))  # noqa
    if options.unpositioned_dfxp:
        print(
            pycaption.dfxp.SinglePositioningDFXPWriter(**writer_kwargs)
            .write(content).encode("utf-8")
        )


if __name__ == '__main__':
    main()

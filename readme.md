# musicforprogramming

CLI song downloader for http://musicforprogramming.net

    $ musicforprogramming --help
    Usage: musicforprogramming [OPTIONS] [TRACKS]

      Download tracks from musicforprogramming.net, track argument should be
      either a number or range, e.g. 1 or 1-5

    Options:
      --show  just show track names in tracks range
      --help  Show this message and exit.

## example

    $ musicforprogramming 27 --show
    27-michael_hicks.mp3
    $ musicforprogramming 27
    27-michael_hicks.mp  28%[====>               ]  26.31M  2.23MB/s    eta 31s

## install

requires `python3.6` and *nix os with `wget`:

    pip install --user git+https://github.com/Granitosaurus/musicforprogramming-dl

depends on `click` and `requests` packages because everyone should have them already
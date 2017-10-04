#! /usr/bin/env python3
from collections import namedtuple
from typing import List

import click
import re
import requests
from urllib.parse import urlparse
import subprocess

"""
Simple cli downloader for music tracks from http://musicforprogramming.net powered by click and requests
author: granitosaurus, under GPLv3
"""

Song = namedtuple('Song', ['index', 'name', 'url'])


def download_song_data() -> List[Song]:
    """Download song data from rss page"""
    resp = requests.get('http://musicforprogramming.net/rss.php')
    urls = re.findall('<guid>(.+?)</guid>', resp.text)[::-1]
    for url in urls:
        name = urlparse(url).path.split('programming_')[-1]
        yield Song(int(name.split('-')[0]), name, url)


def show(track_range: range = None):
    if not track_range:
        click.echo('\n'.join([song.name for song in download_song_data()]))
        return
    for song in download_song_data():
        if song.index in track_range:
            click.echo(song.name)


def download(track_range: range = None):
    for song in download_song_data():
        if song.index in track_range:
            subprocess.call(f'wget "{song.url}" -O "{song.name}" -q --show-progress', shell=True)


@click.command()
@click.argument('tracks', required=False)
@click.option('--show', 'to_show', help='just show track names in tracks range', is_flag=True)
def cli(tracks, to_show):
    """
    Download tracks from musicforprogramming.net,
    track argument should be either a number or range, e.g. 1 or 1-5
    """
    if not tracks:
        click.echo('available tracks:')
        show()
        click.echo('* see --help for download')
        return
    if '-' in tracks:
        track_range = range(*[int(i) for i in tracks.split('-')])
    else:
        tracks = int(tracks)
        track_range = range(tracks, tracks + 1)

    if to_show:
        show(track_range)
    else:
        download(track_range)


if __name__ == '__main__':
    cli()

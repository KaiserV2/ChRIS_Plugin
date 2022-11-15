#!/usr/bin/env python

from pathlib import Path
from argparse import ArgumentParser, Namespace, ArgumentDefaultsHelpFormatter
from importlib.metadata import Distribution
from PIL import Image

from chris_plugin import chris_plugin

__pkg = Distribution.from_name(__package__)
__version__ = __pkg.version


DISPLAY_TITLE = r"""
ChRIS Plugin Template Title
"""


parser = ArgumentParser(description='cli description',
                        formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument('-n', '--name', default='foo',
                    help='argument which sets example output file name')
parser.add_argument('-V', '--version', action='version',
                    version=f'%(prog)s {__version__}')

# parser.add_argument('--name', required=True)
# options = parser.parse_args(['--something', '2.2'])

# documentation: https://fnndsc.github.io/chris_plugin/chris_plugin.html#chris_plugin
@chris_plugin(
    parser=parser,
    title='Invert image',
    plugin_type='ds',
    category='',                 # ref. https://chrisstore.co/plugins
    min_memory_limit='100Mi',    # supported units: Mi, Gi
    min_cpu_limit='1000m',       # millicores, e.g. "1000m" = 1 CPU core
    min_gpu_limit=0              # set min_gpu_limit=1 to enable GPU
)

def invert_image(inputdir, outputdir):
    im = Image.open(inputdir)
    im = im.convert("RGB")
    # for all of the pixels, invert the rgb values
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            r, g, b = im.getpixel((x, y))
            im.putpixel((x, y), (255 - r, 255 - g, 255 - b))
    im.save(outputdir)


# def main(options: Namespace, inputdir: Path, outputdir: Path):
def main(options: Namespace, inputdir: Path, outputdir: Path):
    print(f'hello, {parser.name}')
    """
    :param options: non-positional arguments parsed by the parser given to @chris_plugin
    :param inputdir: directory containing input files (read-only)
    :param outputdir: directory where to write output files
    """
    invert_image(inputdir, outputdir)
    # print(DISPLAY_TITLE)

    # output_file = outputdir / f'{options.name}.txt'
    # output_file.write_text('did nothing successfully!')


if __name__ == '__main__':
    inputdir = "/users/KaiserW/ChRIS_Plugin/input.jpg"
    outputdir = "output.jpg"
    # invert_image(inputdir, outputdir)
    main(options=global, inputdir=inputdir, outputdir=outputdir)
    # main(inputdir=inputdir, outputdir=outputdir)
    # main(inputdir, outputdir)

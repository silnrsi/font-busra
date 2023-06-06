#!/usr/bin/python3
# this is a smith configuration file

# set the default output folders for release docs
DOCDIR = ["documentation", "web"]

# set the font name and description
APPNAME = 'BusraTestA'
sourcefontfamily = "Busra"
DESC_SHORT = "Font family for the Khmer script"

TESTDIR = ["tests"]

# Get version and authorship information from Regular UFO (canonical metadata); must be first function call:
getufoinfo('source/masters/' + sourcefontfamily  + '-Regular.ufo')

# Set up the FTML tests
# ftmlTest('tools/ftml-smith.xsl')

# cmds = [cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['source/instances/${DS:FILENAME_BASE}.ufo'])]

designspace('source/' + sourcefontfamily + 'UprightRB.designspace',
    target = "${DS:FILENAME_BASE}.ttf",
#    target = process("${DS:FILENAME_BASE}.ttf", *cmds),
    params = "--decomposeComponents --removeOverlap",
    opentype = fea('source/${DS:FILENAME_BASE}.fea',
        master = 'source/Busra.feax',
        params = '-m source/${DS:FILENAME_BASE}.map'),
#    woff = woff('web/${DS:FILENAME_BASE}.woff',
#        metadata=f'../source/{FAMILY}-WOFF-metadata.xml',
#        cmd='psfwoffit -m ${SRC[1]} --woff ${TGT} --woff2 ${TGT}2 ${SRC[0]}'
#        ),
    script = 'khmr',
    pdf = fret(params='-oi')
)

#!/usr/bin/python3
# this is a smith configuration file

# set the default output folders for release docs
DOCDIR = ["documentation", "web"]

# set the font name and description
APPNAME = 'Busra'
FAMILY = APPNAME
DESC_SHORT = "Font family for the Khmer script"

TESTDIR = ["tests"]

opts = preprocess_args({'opt': '--nofinalc'})
# Get version and authorship information from Regular UFO (canonical metadata); must be first function call:
getufoinfo('source/masters/' + FAMILY  + '-Regular.ufo')
# BUILDLABEL = 'beta1'

# Set up the FTML tests
# ftmlTest('tools/ftml-smith.xsl')

mparams = []
if "--nofinalc" not in opts:
    mparams.append("-D finalc=1")

# cmds = [cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['source/instances/${DS:FILENAME_BASE}.ufo'])]

designspace('source/' + FAMILY + 'UprightRB.designspace',
    target = "${DS:FILENAME_BASE}.ttf",
#    target = process("${DS:FILENAME_BASE}.ttf", *cmds),
    params = "--decomposeComponents --removeOverlap",
    opentype = fea('source/${DS:FILENAME_BASE}.fea',
        master = 'source/Busra.feax',
        make_params = " ".join(mparams),
        params = '-m source/${DS:FILENAME_BASE}.map'),
#    woff = woff('web/${DS:FILENAME_BASE}.woff',
#        metadata=f'../source/{FAMILY}-WOFF-metadata.xml',
#        cmd='psfwoffit -m ${SRC[1]} --woff ${TGT} --woff2 ${TGT}2 ${SRC[0]}'
#        ),
    script = 'khmr',
    pdf = fret(params='-oi -r')
)

# build auxiliary 'Lolo' RIBBI family
extralightpackage = package(appname = "BusraExtraLight", docdir = DOCDIR)

getufoinfo('source/masters/' + FAMILY  + '-Regular.ufo', extralightpackage)

designspace('source/' + FAMILY + 'UprightXLonly.designspace',
    target = "${DS:FILENAME_BASE}.ttf",
    params = "--decomposeComponents --removeOverlap",
    opentype = fea('source/${DS:FILENAME_BASE}.fea',
        master = 'source/Busra.feax',
        make_params = " ".join(mparams),
        params = '-m source/${DS:FILENAME_BASE}.map'),
    script = 'khmr',
    pdf = fret(params='-oi -r')
)

#!/usr/bin/python3
# this is a smith configuration file

# set the default output folders for release docs
DOCDIR = ["documentation", "web"]

# set the font name and description
APPNAME = 'Busra'
FAMILY = APPNAME

TESTDIR = ["tests"]

opts = preprocess_args({'opt': '--nofinalc'})
# Get version and authorship information from Regular UFO (canonical metadata); must be first function call:
getufoinfo('source/masters/' + FAMILY  + '-Regular.ufo')

# Set up the FTML tests
# ftmlTest('tools/ftml-smith.xsl')

mparams = ["--ignoreglyphs"]
if "--nofinalc" not in opts:
    mparams.append("-D finalc=1")

cmds = [cmd('gftools fix-nonhinting -q --no-backup ${DEP} ${TGT}')]

designspace('source/' + FAMILY + 'Upright.designspace',
#    target = "${DS:FILENAME_BASE}.ttf",
    target = process("${DS:FILENAME_BASE}.ttf", *cmds),
    params = f"--removeOverlap --compregex ^_",
    opentype = fea('source/${DS:FILENAME_BASE}.fea',
        master = 'source/Busra.feax',
        make_params = " ".join(mparams),
        params = '-m source/${DS:FILENAME_BASE}.map'),
    woff = woff('web/${DS:FILENAME_BASE}.woff',
        metadata=f'../source/busra-WOFF-metadata.xml'),
    script = 'khmr',
    pdf = fret(params='-oi -r')
)

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

# compreg = r"^(_|uni(?:200B|17C0.*?SS01|17B[79]\.ms|0302030[0139]|03060)|six\.001|nonmarkingreturn)"
# compreg = r"^(_|uni(?:200B|17DD\.(wide|a)|17D6\.alt2|17D217A(1\.[^a]|1\.altlow|1$)|17D1\.a|17C[FEDB]\.a|17CA\.lower|17(C5|B6|94)\.l|17C0.*?SS01|17B[79]\.ms|179[AC]\.spc|178A17CF|030[26].|01A0.)|six\.001|nonmarkingreturn)"
#compreg = r"^(_|uni(?:|17D1\.a|17C0.rightpart..SS01|17B[79]\.ms|179[AC]\.spc|178A17CF|030[26].)|nonmarkingreturn)"

mparams = ["--ignoreglyphs"] # , "'"+compreg+"'"]
if "--nofinalc" not in opts:
    mparams.append("-D finalc=1")

cmds = [cmd('gftools fix-nonhinting -q --no-backup ${DEP} ${TGT}')]

designspace('source/' + FAMILY + 'Upright.designspace',
#    target = "${DS:FILENAME_BASE}.ttf",
    target = process("${DS:FILENAME_BASE}.ttf", *cmds),
    params = f"--decomposeComponents --removeOverlap --compregex ^_",
    opentype = fea('source/${DS:FILENAME_BASE}.fea',
        master = 'source/Busra.feax',
        make_params = " ".join(mparams),
        params = '-m source/${DS:FILENAME_BASE}.map'),
    woff = woff('web/${DS:FILENAME_BASE}.woff',
        metadata=f'../source/busra-WOFF-metadata.xml'),
    script = 'khmr',
    pdf = fret(params='-oi -r')
)

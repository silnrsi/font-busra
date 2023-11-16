#!/usr/bin/python3

import argparse, re, os
import defcon
from collections import namedtuple

BBox = namedtuple("BBox", ["xmin", "ymin", "xmax", "ymax"])

def addAnchor(a, g, name, x, y):
    '''Adds an anchor to anchors on a glyph:
        anchor, glyph, name, x, y'''
    if name not in a:
        a[name] = defcon.objects.anchor.Anchor(None, {'name': name, 'x': x, 'y': y})

def anchorVal(a):
    if a is None or not len(a):
        return 0
    return a['x'] + 1j * a['y']

def addAP(a, name, v):
    if name not in a:
        a[name] = defcon.objects.anchor.Anchor(None, {'name': name, 'x': int(v.real), 'y': int(v.imag)})

def getAP(a, name):
    return anchorVal(a.get(name, None))

def renameAP(a, old, new):
    if old in a:
        ap = a[old]
        del a[old]
        ap['name'] = new
        a[new] = ap

def deleteAP(a, old):
    if old in a:
        del a[old]


def some(f):
    '''Create driver callback function for groups of glyphs. Callback parameters are:
        glyph, dict of anchors, bounding box (BBox), advance'''
    def fun(glyphs):
        for n in glyphs:
            try:
                g = font[n]
            except KeyError:
                continue
            if not len(g) and not len(g.components):
                b = BBox(0, 0, 0, 0)
                anchors = {}
            else:
                anchors = dict((a.name, a) for a in g.anchors)
                b = BBox(*g.bounds)
            f(g, anchors, b, g.width)
            if len(g) or len(g.components):
                g.anchors = [v for k, v in sorted(anchors.items())]
            cover.add_glyph(n, 2)
    return fun

def unilist(a, suffices=[], prefix="uni17"):
    res = []
    for s in suffices + [""]:
        st = "." + s if len(s) else s
        res.extend(["{}{:02X}{}".format(prefix, x, st) for x in a])
    return res

class Coverage:
    def __init__(self):
        self.classes = {}
        self.all_glyphs = {}

    def add_glyph(self, name, mode, prefix="uni17", specials = [0xD2]):
        self.all_glyphs[name] = mode
        if not name.startswith(prefix):
            return
        val = name[len(prefix):len(prefix)+2]
        namelen = len(prefix) + 2
        try:
            num = int(val, 16)
        except ValueError:
            return
        subcategory = ""
        if num in specials:
            subcategory = hex(num)
            val = name[len(prefix)+4:len(prefix)+6]
            try:
                num = int(val, 16)
                namelen += 4
            except ValueError:
                num = int(subcategory, 16)
                subcategory = ""
        category = ""
        extpos = name.find(".")
        if extpos > namelen + 3 or (extpos < 0 and len(name) > namelen + 3):
            try:
                category += hex(int(name[namelen+2:namelen+4], 16))
            except ValueError:
                pass
        if "." in name:
            category = category + name[name.index("."):]
        if len(subcategory):
            category = subcategory + "+" + category
        self.classes.setdefault(category, {})[num] = mode

    def has_glyph(self, name, mode):
        return self.all_glyphs.get(name, 0) == mode

    def print_stats(self):
        codes = [" ", ".", "+"]
        res = []
        for k, v in sorted(self.classes.items()):
            if len(k):
                res.append(f"{k}:")
            res.append("        " + " ".join("{:1X}".format(x) for x in range(16)))
            i = min(v.keys())
            a = max(v.keys())
            start = i & ~15
            end = (a & ~15) + 15
            for j in range(start, end, 16):
                line = [codes[v.get(j+x, 0)] for x in range(16)]
                res.append(" {:02X}     ".format(j) + " ".join(line))
            res.append("")
        return "\n".join(res)

def fixup_plist(f):
    lines = []
    with open(f, encoding="utf-8") as inf:
        for l in inf.readlines():
            for i in range(len(l)):
                if l[i] != " ":
                    start = 2 if i > 1 else 0
                    l = l[start:]
                    break
            lines.append(l)
    with open(f, "w", encoding="utf-8") as outf:
        for l in lines:
            outf.write(l)

parser = argparse.ArgumentParser()
parser.add_argument("infile", help="Input UFO")
parser.add_argument("outfile", nargs="?", help="Output UFO")
parser.add_argument("-n","--dryrun",action="store_true",default=False,help="Don't save the output")
parser.add_argument("--stats",action="store_true",default=False,help="Output glyph coverage statistics")
parser.add_argument("-g","--glyphs",action="append",default=[],help="Regexp to or with other regexps for glyphs to include")
parser.add_argument("-e","--excludes",action="append",default=[],help="Regexp of glyphs to exclude from selection (after -g)")
parser.add_argument("-c","--code",default="",help="Code snippet to execute on each glyph: g=glyph, a=aps, b=bounding box, w=advance")
args = parser.parse_args()

font = defcon.objects.font.Font(args.infile)
allglyphs = [g.name for g in font]

cover = Coverage()
for g in allglyphs:
    cover.add_glyph(g, 1)

regs = [re.compile(r) for r in args.glyphs]
excl = [re.compile(e) for e in args.excludes]
procglyphs = []
for g in allglyphs:
    res = None
    if not len(regs):
        procglyphs.append(g)
        continue
    for r in regs:
        if r.search(g):
            res = g
            break
    if res is None:
        continue
    for e in excl:
        if e.search(res):
            res = None
            break
    if res is not None:
        procglyphs.append(res)

@some
def process(g, a, b, w):
    if args.dryrun:
        print(g.name)
    if len(args.code):
        exec(args.code)

process(procglyphs)

if not args.dryrun:
    outp = args.outfile if args.outfile else args.infile
    font.save(outp)
    for f in ("fontinfo", "lib", "layercontents", "contents"):
        fn = f + ".plist"
        for dp, dns, fs in os.walk(outp):
            if fn in fs:
                fixup_plist(os.path.join(dp, fn))

if args.stats:
    print(cover.print_stats())


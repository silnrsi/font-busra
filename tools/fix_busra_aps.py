#!/usr/bin/python3

import argparse, re
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

def addAnchorVal(a, name, v):
    if name not in a:
        a[name] = defcon.objects.anchor.Anchor(None, {'name': name, 'x': int(v.real), 'y': int(v.imag)})

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
                continue
            anchors = dict((a.name, a) for a in g.anchors)
            b = BBox(*g.bounds)
            mid = 0.5 * (b.xmin + b.xmax)
            f(g, anchors, b, g.width)
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

parser = argparse.ArgumentParser()
parser.add_argument("infile", help="Input UFO")
parser.add_argument("outfile", nargs="?", help="Output UFO")
parser.add_argument("-n","--dryrun",action="store_true",default=False,help="Don't save the output")
args = parser.parse_args()

font = defcon.objects.font.Font(args.infile)
allglyphs = [g.name for g in font]
l_shift = -245 # add this to right aligned AP positions default to advance
# lc_pos is def or N or NC or (xmin+xmax)/2 and y=0
baseglyphs = unilist(range(0x80, 0xB4), suffices=["alt"])
baseglyphs += ["uni17B6", "uni17C5.rightpart", "dottedcircle"]
b6ligs = [x for x in allglyphs if x.endswith("17B6") or x.endswith("17C5.right")] # add .alts
belowdias = unilist(range(0x80, 0xB4), prefix="uni17D217", suffices=["alt", "low", "low.alt"]) \
          + unilist(range(0xBB, 0xBE), suffices=["low", "narrow", "low.narrow"]) + ["uni17D2", "uni17D2.lower"]
belowcentres = ["uni17D2178E"]
belowfullheights = unilist([0x83, 0x8D, 0x99, 0x9A, 0x9E, 0x9F], prefix="uni17D217", suffices=["alt", "low", "low.alt"])
belowdias = set(belowdias) - set(belowcentres) - set(belowfullheights)
baseheights = {}
baseheights.update({x: 260j for x in unilist([0x84, 0x87, 0x8A, 0x8B, 0x90, 0x95, 0x9C, 0xA5, 0xA6, 0xA8, 0xAF, 0xB1, 0xB3])})
baseheights.update({x: 380j for x in unilist([0xA6, 0xAA])})
#baseheights.update({x: 250 for x in ["uni17AA", "uni17B1.alt", "uni17B3.alt"])
baseheights.update({x: 260j for x in unilist([0xB7, 0x95, 0xA5, 0xA8, 0xAF])})


# vertical shifts
below1 = unilist(range(0xAB, 0xAF)) # -600 coengs 80-B3 minus 83 88 8D 94 99 9A 9E 9F A1 (incl A1.alt) that is all coengs that are not tall and not coeng ro
below2 = unilist([0xA1, 0xA6, 0xB0])  # -700 coengs A1.alt A3-B3
below3 = unilist([0xAA, 0xB1, 0xB3])  # -190 BB BC BD D2
centre_left = unilist([0x81, 0x83, 0x88, 0x89, 0x8E, 0x91, 0x99, 0x9B, 0x9F, 0xA0, 0xA7])
centre_marks = unilist([0xC6, 0xC9, 0xCB, 0xCD, 0xCE, 0xCF, 0xD1, 0xD3], suffices=["narrow", "a", "x", "lower", "alt"])
abovedias = unilist(list(range(0xB7, 0xBB)) + [0xCA, 0xCC, 0xD0], suffices=["narrow", "alt"])
centre_shift = 49
u_base = -715 + 1580j
shifts = {'uni17B1': 60j, 'uni17B3': 100j, 'uni17AA': 260j}

cover = Coverage()
for g in allglyphs:
    cover.add_glyph(g, 1)

@some
def bases(g, a, b, adv):
    name = g.name
    old = a.copy()
    a.clear()
    if 'N' in old:
        c = anchorVal(old['N']) + l_shift
    else:
        c = (b.xmin + b.xmax) // 2
    if b.ymin < -100:
        c += 1j * b.ymin
    addAnchorVal(a, 'LC', c)
    r = adv + l_shift
    addAnchorVal(a, 'L', r + (1j * b.ymin if b.ymin < -100 else 0))
    addAnchorVal(a, 'U', r + 1580j + baseheights.get(name, 0))
    if 'H' in old:
        u = anchorVal(old['H']) - 700   # all udias have _H = -700
    else:
        u = adv + u_base
    u += shifts.get(name, 0)
    if name in centre_left:
        u += centre_shift
    addAnchorVal(a, 'UC', u + baseheights.get(name, 0))

def getbasepos(g, aname, b, ratio, shift):
    if g is not None:
        for a in g.anchors:
            if a.name == aname:
                return anchorVal(a)
    return (b.xmin + b.xmax) // ratio

@some
def clear_aps(g, a, b, adv):
    if g.name.startswith("uni17") and not cover.has_glyph(g.name, 2):
        a.clear()

@some
def ligs(g, a, b, adv):
    name = g.name
    old = a.copy()
    a.clear()
    base = name[:7] + (name[name.index("."):] if "." in name else "")
    base = base.replace(".right", "")
    if base in font:
        baseg = font[base]
    else:
        baseg = None
    c = getbasepos(baseg, "LC", b, 3, 0)
    addAnchorVal(a, 'LC_1', c)
    c = b.xmax - 700 # (half stem width, what a hack)
    addAnchorVal(a, "LC_2", c)
    c = getbasepos(baseg, "L", b, 2, 0)
    addAnchorVal(a, "L_1", c)
    addAnchorVal(a, "U_1", c + 1580j + baseheights.get(base, 0))
    addAnchorVal(a, "L_2", adv + l_shift)
    addAnchorVal(a, "U_2", adv + l_shift + 1580j + baseheights.get(base, 0))
    c = getbasepos(baseg, "UC", b, 3, 1580j)
    addAnchorVal(a, "UC_1", c + baseheights.get(base, 0))
    c = b.xmax - 700
    addAnchorVal(a, "UC_2", c + 1580j + baseheights.get(base, 0))

@some
def aboveright(g, a, b, adv):
    old = a.copy()
    a.clear()
    addAnchorVal(a, "_U", l_shift + 1580j)
    addAnchorVal(a, "_UU", l_shift + 20 + 1580j)
    addAnchorVal(a, "UU", l_shift + 20 + 1j * max(b.ymax + 40, l_shift.imag + 1860))
    addAnchorVal(a, "UA", u_base.real + 20 + 1j * max(b.ymax + 40, u_base.imag + 280))

@some
def abovecentre(g, a, b, adv):
    old = a.copy()
    a.clear()
    addAnchorVal(a, "_UC", u_base)
    addAnchorVal(a, "_UA", u_base + 20)
    above = u_base + 20 + 280j
    addAnchorVal(a, "UA", above.real + 1j * max(b.ymax + 40, above.imag))
    addAnchorVal(a, "UU", l_shift + 20 + max(above.imag, 1860, b.ymax + 40) * 1j)

@some
def belowright(g, a, b, adv):
    old = a.copy()
    a.clear()
    offset = -670j if "low" in g.name else 0
    addAnchorVal(a, "_L", l_shift + offset)
    addAnchorVal(a, "_LL", l_shift + 20 + offset)
    addAnchorVal(a, "LL", l_shift + 20 - 670j + offset)
    if "def" in old:
        c = anchorVal(old["def"])
    else:
        c = (b.xmin + b.xmax) // 2
    addAnchorVal(a, "LA", c - 20 - 670j)

@some
def belowcentre(g, a, b, adv):
    old = a.copy()
    a.clear()
    if "def" in old:
        c = anchorVal(old["def"])
    else:
        c = (b.xmin + b.xmax) // 2
    addAnchorVal(a, "_LC", c)
    addAnchorVal(a, "_LA", c - 20)
    addAnchorVal(a, "LA", c - 20 - 670j)
    addAnchorVal(a, "LL", l_shift + 20 - 670j)

bases(baseglyphs)
bases(belowfullheights)
ligs(b6ligs)
aboveright(abovedias)
abovecentre(centre_marks)
belowright(belowdias)
belowcentre(belowcentres)
clear_aps(allglyphs)

if not args.dryrun:
    font.save(args.outfile if args.outfile else args.infile)

print(cover.print_stats())

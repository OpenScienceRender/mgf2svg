#!/usr/bin/python

import sys
import matplotlib
# plot to svg
matplotlib.use('SVG')

import pylab
from pyteomics import mgf
import urllib
import tempfile
import os.path


def createSpectrumFigure(spectrum, device, title=True, color="black"):
    if title:
        device.title(spectrum["params"]["title"])

    device.xlabel("m/z")
    device.ylabel("Intensity")
    device.bar(spectrum["m/z array"], spectrum["intensity array"],
              width=0.5, linewidth=1, edgecolor=color)
    return

def plotSingleSpectrum(filename, spectrum):
    pylab.figure()
    createSpectrumFigure(spectrum, pylab)
    pylab.savefig(filename)
    return

## main
if len(sys.argv) == 2:
    ## download file
    filename, header = urllib.urlretrieve (sys.argv[1])

    spectra = mgf.read(filename)
    ## we only support the first spectrum now
    spectrum = next(spectra)

    tmpdir = tempfile.mkdtemp()
    filename = os.path.join(tmpdir, "output.svg")

    plotSingleSpectrum(filename, spectrum)
    ## write to stdout
    with open(filename, "r") as fin:
        print(fin.read())
else:
    print("Usage:\n\t" + sys.argv[0] + " URL")  


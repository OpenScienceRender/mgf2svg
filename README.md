# mgf2svg: View mgf files

Given a url pointing to a valid `mgf` file ([Mascot Generic Format](http://en.wikipedia.org/wiki/Mascot_%28software%29)), prints the corresonding `svg` to `stdout`. 

# Installation: 

```bash
## install python requirements (debian packages)
sudo apt-get install python-setuptools python-dev build-essential python-tk python-matplotlib
## install pyteomics (not in debian yet)
sudo pip install pyteomics
```

# Usage:

```bash
./mgf2svg.py https://raw.githubusercontent.com/lgatto/MSnbase/master/inst/extdata/test.mgf > output.svg
```

# Know bugs/limitations:

Only the first spectrum in a `mgf` file is supported.

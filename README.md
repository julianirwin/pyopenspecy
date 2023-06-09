<!-- These are examples of badges you might want to add to your README:
     please update the URLs accordingly

[![Built Status](https://api.cirrus-ci.com/github/<USER>/pyopenspecy.svg?branch=main)](https://cirrus-ci.com/github/<USER>/pyopenspecy)
[![ReadTheDocs](https://readthedocs.org/projects/pyopenspecy/badge/?version=latest)](https://pyopenspecy.readthedocs.io/en/stable/)
[![Coveralls](https://img.shields.io/coveralls/github/<USER>/pyopenspecy/main.svg)](https://coveralls.io/r/<USER>/pyopenspecy)
[![PyPI-Server](https://img.shields.io/pypi/v/pyopenspecy.svg)](https://pypi.org/project/pyopenspecy/)
[![Conda-Forge](https://img.shields.io/conda/vn/conda-forge/pyopenspecy.svg)](https://anaconda.org/conda-forge/pyopenspecy)
[![Monthly Downloads](https://pepy.tech/badge/pyopenspecy/month)](https://pepy.tech/project/pyopenspecy)
[![Twitter](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter)](https://twitter.com/pyopenspecy)
-->

[![Project generated with PyScaffold](https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold)](https://pyscaffold.org/)

# pyopenspecy

> Quickly grab spectra from Open Specy through python!

`pyopenspecy` allows you to grab specific or random Raman and FTIR spectra from the Open Specy libraries.

# Example

Get a random spectrum

     import pyopenspecy

     spectrum, metadata = pyopenspecy.random_raman_spectrum()


Get a specific spectrum

     spectrum, metadata = pyopenspecy.raman_spectrum_by_id(801)


Fuzzy search for a spectrum by sample material name.

     pyopenspecy.fuzzy_search_raman("Fe O3", limit=10)
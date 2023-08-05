# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Deep-LASI'
copyright = '2023, Fablab'
author = 'Ploetz'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Evelyn Test: Numbering of figures:
import sys
import os
html_theme = 'sphinx_rtd_theme'
numfig = True

# Packages that need to be included for colored text in Sphinx
# These folders are copied to the documentation's HTML output
#html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
#html_css_files = [
#    'css/custom.css',
#]

# -- Color Support by Sphinx from the standard definition file s5defs.txt
rst_prolog = """
.. include:: <s5defs.txt>
.. default-role::

"""

# -*- coding: utf-8 -*-
#
# igraph documentation build configuration file, created by
# sphinx-quickstart on Thu Jun 17 11:36:14 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

from datetime import datetime

import sys
import os
import importlib
from pathlib import Path


# Check if we are inside readthedocs, the conf is quite different there
rtd_version = os.getenv("READTHEDOCS_VERSION", "")
rtd_version_type = os.getenv("READTHEDOCS_VERSION_TYPE", "unknown")

# Utility functions
# NOTE: these could be improved, esp by importing igraph, but that
# currently generates a conflict with pydoctor. It is funny because pydoctor's
# docs indeed import itself... perhaps there's a decent way to solve this.
def get_root_dir():
    """Get project root folder"""
    return str(Path(".").absolute().parent.parent)


def get_igraphdir():
    """Get igraph folder"""
    return Path(importlib.util.find_spec("igraph").origin).parent


def get_igraph_version():
    """Get igraph version"""
    if rtd_version and rtd_version_type == "tag":
        return rtd_version

    version_file = get_igraphdir() / "version.py"
    with open(version_file, "rt") as f:
        version_info = f.readline().rstrip("\n").split("=")[1].strip()[1:-1].split(", ")
    version = ".".join(version_info)

    return version


# -- General configuration -----------------------------------------------------

_igraph_dir = str(get_igraphdir())
_igraph_version = get_igraph_version()

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.intersphinx",
    "sphinx_gallery.gen_gallery",
    #'sphinx_panels',
    "pydoctor.sphinx_ext.build_apidocs",
]

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.append(os.path.abspath('.'))

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "igraph"
copyright = "2010-{0}, The igraph development team".format(datetime.now().year)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = _igraph_version
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["include/*.rst"]

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# Inspired by pydoctor's RTD page itself
# https://github.com/twisted/pydoctor/blob/master/docs/source/conf.py
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = "_static/logo-black.svg"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = "igraphdoc"

# Integration with Read the Docs since RTD is not manipulating the Sphinx
# config files on its own any more.
# This is according to:
# https://about.readthedocs.com/blog/2024/07/addons-by-default/
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")
html_context = {}
if os.environ.get("READTHEDOCS", "") == "True":
    html_context["READTHEDOCS"] = True

# -- Options for pydoctor ------------------------------------------------------


def get_pydoctor_html_outputdir(pydoctor_url_path):
    """Get HTML output dir for pydoctor"""
    # NOTE: obviously this is a little tricky, but it does work for both
    # the sphinx-build script and the python -m sphinx module calls. It works
    # locally, on github pages, and on RTD.
    return str(Path(sys.argv[-1]) / pydoctor_url_path.strip("/"))


# API docs relative to the rest of the docs, needed for pydoctor to play nicely
# with intersphinx (https://pypi.org/project/pydoctor/#pydoctor-21-2-0)
# NOTE: As of 2022 AD, pydoctor requires this to be a subfolder of the docs.
pydoctor_url_path = "api/"

pydoctor_args = [
    "--project-name=igraph",
    "--project-version=" + version,
    "--project-url=https://python.igraph.org",
    "--introspect-c-modules",
    "--docformat=epytext",
    "--intersphinx=https://docs.python.org/3/objects.inv",
    "--html-output=" + get_pydoctor_html_outputdir(pydoctor_url_path),
    "--html-viewsource-base=https://github.com/igraph/python-igraph/tree/main/src/igraph",
    "--project-base-dir=" + _igraph_dir,
    "--template-dir=" + get_root_dir() + "/doc/source/_pydoctor_templates",
    "--theme=readthedocs",
    _igraph_dir,
]
pydoctor_url_path = "/en/{rtd_version}/api"


# -- Options for sphinx-gallery ------------------------------------------------

sphinx_gallery_conf = {
    "examples_dirs": "../examples_sphinx-gallery",  # path to your example scripts
    "gallery_dirs": "tutorials",  # path to where to save gallery generated output
    "filename_pattern": "/",
    "matplotlib_animations": True,
    "remove_config_comments": True,
}

# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
# latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
# latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    (
        "index",
        "igraph.tex",
        "igraph Documentation",
        "The igraph development team",
        "manual",
    ),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Additional stuff for the LaTeX preamble.
# latex_preamble = ''

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ("index", "igraph", "igraph Documentation", ["The igraph development team"], 1)
]


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = "igraph"
epub_author = "The igraph development team"
epub_publisher = "The igraph development team"
epub_copyright = "2010-2022, The igraph development team"

# The language of the text. It defaults to the language option
# or en if the language is not set.
# epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
# epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
# epub_identifier = ''

# A unique identification for the text.
# epub_uid = ''

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_post_files = []

# A list of files that should not be packed into the epub file.
# epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
# epub_tocdepth = 3


# -- Intersphinx ------------------------------------------------

intersphinx_mapping = {
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "networkx": ("https://networkx.org/documentation/stable/", None),
}

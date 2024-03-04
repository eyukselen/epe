# Configuration file for the Sphinx documentation builder.
import sys
import os


sys.path.insert(0, os.path.abspath(".."))

project = "eprofiler"
copyright = "2024, emre"
author = "emre"
release = "0.0.4"
source_suffix = ".rst"
master_doc = "index"
version = "0.0.4"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.idea']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

html_theme_options = {
    "show_powered_by": False,
    "github_user": "eyukselen",
    "github_repo": "eprofiler",
    "github_banner": True,
    "show_related": False,
}

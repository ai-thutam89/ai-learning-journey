# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

master_doc = 'index'

project = 'AI-Learning-Journey'
copyright = '2025, Tam Nguyen Study'
author = 'Tam Nguyen Study'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

html_context = {
    "display_github": True,           # Enable GitHub integration
    "github_user": "ai-thutam89",   # GitHub username
    "github_repo": "ai-learning-journey",  # Repository name
    "github_version": "main",         # Branch name
    "conf_py_path": "/source/",       # Path to your docs folder in the repo
}


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.imgmath',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',  # Optional: for Google-style docstrings
    'myst_parser',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

epub_enabled = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


# Default theme : alabaster
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
def setup(app):
    app.add_css_file('custom.css')

# Highlighting programming languages
highlight_language = 'java'
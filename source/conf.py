# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

master_doc = 'index'

project = 'AI-Learning-Journey'
copyright = '2025, Tam Nguyen Study'
author = 'Tam Nguyen Study'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.imgmath',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
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
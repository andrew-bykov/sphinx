# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Быков Андрей Юрьевич'
copyright = '2020, Быков Андрей Юрьевич'
author = 'Быков Андрей'

# The short X.Y version
version = '1.2'
# The full version, including alpha/beta/rc tags
release = '1'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '2.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinx.ext.extlinks'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'ru'
html_search_language = 'ru'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'docs']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

# If you want to have a consistent, platform independent look
# sphinxemoji_style = 'twemoji'

# -- Options for ToDo output -------------------------------------------------

todo_include_todos = True
# todo_emit_warnings = True
todo_link_only = True

# -- Options for ExtLink output ----------------------------------------------

# Now, you can use the alias name as a new role, e.g. :issue:`123`. 
# This then inserts a link to https://github.com/sphinx-doc/sphinx/issues/123. 
# As you can see, the target given in the role is substituted in the base URL in the place of %s.

extlinks = {'gh': ('https://github.com/andrew-bykov/sphinx/issues/%s','# ')}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
  "external_links": [
      ("Github", "https://github.com/andrew-bykov/sphinx")
  ]
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# The default `html_sidebars` of Press theme: ['util/searchbox.html', 'util/sidetoc.html']
#
# html_sidebars = {'**': ['util/sidetoc.html']}
html_logo = '_static/bykov.jpg'
html_css_files = ["css/custom.css"]

#---sphinx-themes-----
html_theme = 'press'

# -*- coding: utf-8 -*-
# -- General configuration ------------------------------------------------
extensions = [
    'sphinx.ext.coverage', 'sphinx.ext.imgmath', 'sphinx.ext.githubpages'
]

templates_path = ['_templates']

source_suffix = ['.rst', '.md']

master_doc = 'index'

project = u'Numerus'
copyright = u'2017, Arden Rasmussen'
author = u'Arden Rasmussen'

version = u'0.0'
release = u'0.0'

language = None

exclude_patterns = []

pygments_style = 'sphinx'

todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

import sphinx_bootstrap_theme
#  from crate.theme.rtd.conf import *

html_theme = 'bootstrap'

html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

html_show_sourcelink = False

html_show_sphinx = False

html_theme_options = {
    'navbar_site_name': "Numerus",
    'bootswatch_theme': "flatly",
}

html_static_path = ['_static']

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Numerusdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Numerus.tex', u'Numerus Documentation', u'Arden Ramussen',
     'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'numerus', u'Numerus Documentation', [author], 1)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Numerus', u'Form Documentation', author, 'Numerus',
     'Mathematical operator engine', 'Miscellaneous'),
]

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

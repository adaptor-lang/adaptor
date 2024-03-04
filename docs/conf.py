
project = 'adaptor-lang'
copyright = 'contributors'
author = 'contributors'
release = '1'

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
extensions = ['myst_parser']

templates_path = ['_templates']

language = 'en'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


html_theme = 'alabaster'

html_theme_options = {
    "nosidebar": "true",
}

html_title = 'The Adaptor Programming Language'

html_static_path = ['_static']

html_css_files = ['customstyle.css']

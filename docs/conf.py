project = "PyYandexLMS"
copyright = "2022, lav."
author = "lav."

release = "0.1.0"

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
    "sphinx.ext.ifconfig",
    "sphinx.ext.intersphinx",
    "sphinx-prompt",
    "sphinx_substitution_extensions",
    "sphinx_copybutton",
    'm2r',
]

templates_path = ["_templates"]
html_theme = "furo"
html_static_path = ["_static"]
todo_include_todos = True
pygments_style = "sphinx"
htmlhelp_basename = project
html_theme_options = {}
html_css_files = [
    "stylesheets/extra.css",
]
highlight_language = "python3"

language = "ru"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

source_suffix = ['.rst', '.md']
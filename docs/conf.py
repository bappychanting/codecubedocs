import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = ["_themes", ]

master_doc = 'index'
copyright = "2022, Mahadi Hasan"
version = "1.0.0"

html_title = "CodeCube"
html_logo = "https://user-images.githubusercontent.com/22908406/200573841-1b090676-6692-4762-9657-782dd98b56ab.png"
html_favicon = "https://user-images.githubusercontent.com/22908406/200559448-e76b9b36-89aa-4463-b9a1-72c330dc1dba.png"
html_theme_options = {
    "logo_only": True,
    "display_version": False,
}
html_sidebars = {
    '**': [
        'globaltoc.html',
        'searchbox.html',
        'relations.html'
    ]
}

# sphinx-notfound-page
# https://github.com/readthedocs/sphinx-notfound-page
notfound_context = {
    "title": "Page Not Found",
    "body": """
<h1>Page Not Found</h1>
<p>Sorry, we couldn't find that page.</p>
<p>Try using the search box or go to the homepage.</p>
""",
}
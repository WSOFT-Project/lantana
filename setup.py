from setuptools import setup, find_packages

VERSION = '2.6.0'

setup(
    name="lantana",
    version=VERSION,
    url='http://wsoft-project.github.io/lantana/',
    license='MIT',
    description='Bootstrap theme for MkDocs',
    author='WSOFT',
    author_email='info@wsoft.ws',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['mkdocs>=1.1','mkdocs-material>=7.0','mkdocs-awesome-pages-plugin>=2.3','mkdocs-macros-plugin>=0.6.3','mkdocs-git-authors-plugin>=0.6.2','mkdocs-mermaid2-plugin>=0.5.0','mkdocs-git-revision-date-plugin>=0.3.1','natsort>=8.3.1'],
    python_requires='>=3.5',
    entry_points={
        'mkdocs.themes': [
            'lantana = lantana',
        ],
        "console_scripts":[
            'lantana = lantana.__main__:cli',
        ],
        "markdown.extensions": [
            "mdx_cards = lantana.extensions.mdx_cards:CardsExtension",
            "mdx_wsid = lantana.extensions.mdx_wsid:WSIDExtension",
            "mdx_embedly = lantana.extensions.mdx_embedly:EmbedlyExtension"
        ]
    },
    zip_safe=False
)
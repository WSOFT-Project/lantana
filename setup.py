from setuptools import setup, find_packages

VERSION = '2.12.1'

setup(
    name="lantana",
    version=VERSION,
    url='https://lantana.wsoft.ws/',
    license='MIT',
    description='Bootstrap theme for MkDocs',
    author='WSOFT',
    author_email='info@wsoft.ws',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[ 'markdown<3.4','mkdocs>=1.1','pymdown-extensions','mkdocs-material','mkdocs-awesome-pages-plugin>=2.3','mkdocs-macros-plugin>=0.6.3','mkdocs-git-authors-plugin>=0.6.2','mkdocs-mermaid2-plugin>=0.5.0','mkdocs-git-revision-date-plugin>=0.3.1','natsort>=8.3.1',"beautifulsoup4>=4.12.3","html5lib>=1.1"],
    python_requires='>=3.5',
    entry_points={
        'mkdocs.themes': [
            'lantana = lantana',
        ],
        "console_scripts":[
            'lantana = lantana.__main__:cli',
        ],
        "markdown.extensions": [
            "mdx_wsid = lantana.extensions.mdx_wsid:WSIDExtension",
            "mdx_embedly = lantana.extensions.mdx_embedly:EmbedlyExtension",
            "lantana = lantana.extensions.lantana:LantanaExtension",
            "lantana.cards = lantana.extensions.cards:CardsExtension",
            "lantana.mtables = lantana.extensions.mtables:MetaTablesExtension",
            "lantana.alerts = lantana.extensions.alerts:AlertsExtension",
            "lantana.alerts2 = lantana.extensions.alerts2:Alerts2Extension",
            "lantana.selector = lantana.extensions.selector:SelectorExtension",
            "lantana.accordion = lantana.extensions.accordion:AccordionExtension",
            "lantana.link_opennewtab = lantana.extensions.link_opennewtab:OpenNewTabExtension",
            "lantana.codeblock_copybtn = lantana.extensions.codeblock_copybtn:CodeBlockCopyBtnExtension",
            "lantana.mermaid_precompile = lantana.extensions.mermaid_precompile:MermaidPrecompileExtension",
        ]
    },
    zip_safe=False
)
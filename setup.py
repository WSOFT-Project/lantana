from setuptools import setup, find_packages

VERSION = '1.6.2'

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
    install_requires=['mkdocs>=1.1','mkdocs-material>=7.0','mkdocs-awesome-pages-plugin>=2.3'],
    python_requires='>=3.5',
    entry_points={
        'mkdocs.themes': [
            'lantana = lantana',
        ]
    },
    zip_safe=False
)
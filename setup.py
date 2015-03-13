from setuptools import setup, find_packages

setup(name = "artist",
      version = "0.14.1",
      packages = find_packages(),
      url = "http://github.com/davidfokkema/artist/",
      bugtrack_url='http://github.com/davidfokkema/artist/issues',
      license='GPLv3',
      author = "David Fokkema",
      author_email = "davidfokkema@icloud.com",
      description = "A plotting library for Python with LaTeX output",
      long_description=open('README.rst').read(),
      keywords=['plots', 'plotting', 'data visualization'],
      classifiers=['Intended Audience :: Science/Research',
                   'Intended Audience :: Education',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.4',
                   'Topic :: Scientific/Engineering :: Visualization',
                   'Topic :: Education',
                   'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'],
      install_requires = ['jinja2', 'numpy', 'Pillow'],
      package_data={'artist': ['templates/*.tex']},
)

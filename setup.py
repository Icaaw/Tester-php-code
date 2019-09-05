from distutils.core import setup
from setuptools import setup, find_packages

# long_description
readme_path = directory.joinpath("README.md")
with readme_path.open() as read_file:
    long_description = read_file.read()

setup(
    name = 'dialamoon',
    packages = find_packages(),
    version = '1.2',
    license='MIT',
    description = 'Gets moon visualizations courtesy of NASA/Ernie Wright',
    long_description_content_type="text/markdown",
    long_description = long_description,
    author = 'Sadie Parker',
    author_email = 'sadiemparker@gmail.com',
    url = 'https://github.com/spacerest/dialamoon',
    download_url = 'https://github.com/spacerest/dialamoon/archive/v_1_2.tar.gz',
    keywords = ['MOON', 'ART'],
    install_requires=[
        'numpy~=1.16',
        'opencv-python~=4.1.1.26'
    ],
    classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Other Audience',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)

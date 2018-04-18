import setuptools

import versioneer


with open('README.rst') as f:
    readme = f.read()

setuptools.setup(
    name='gitignoreio',
    description="Update .gitignore from config and gitignore.io.",
    long_description=readme,
    long_description_content_type='text/x-rst',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author='Kyle Altendorf',
    author_email='sda@fstab.net',
    url='https://github.com/altendky/gitignoreio',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            (
                'gitignoreio'
                '= gitignoreio.cli.updategitignore:cli'
            ),
        ],
    },
    install_requires=[
        'click',
        'requests',
    ],
)

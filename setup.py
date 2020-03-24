import os.path

from setuptools import setup, find_packages

PATH = os.path.realpath(os.path.dirname(__file__))

README = open(os.path.join(PATH, 'README.md')).read()
LICENSE = open(os.path.join(PATH, 'LICENSE')).read()


def _requirements(filename: str = 'requirements.txt'):
    with open(os.path.join(PATH, filename)) as f:
        return list(map(lambda r: r.replace('\n', ''), f.readlines()))


setup(
    name='repomaker',
    use_scm_version=True,
    license=LICENSE,
    author='Jorge F. Sánchez (George)',
    author_email='jfsanchez.email@gmail.com',
    maintainer='Jorge F. Sánchez (George)',
    maintainer_email='jfsanchez.email@gmail.com',
    url='https://github.com/jfsanchez-gh/repomaker',
    description='APT mobile repository creator.',
    long_description=README,
    platforms='any',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet',
        'Topic :: System :: Management',
        'Topic :: System :: Networking',
    ],
    packages=find_packages(),
    setup_requires=[
        'setuptools_scm',
    ],
    install_requires=_requirements('requirements.txt'),
    tests_require=_requirements('requirements-dev.txt'),
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'repomaker=repomaker.main:main'
        ]
    },
    zip_safe=False,
)

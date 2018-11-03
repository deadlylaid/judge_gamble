from setuptools import setup


setup_requires = [
    'setuptools>=35.0.2',
]

install_requires = [
    'pip>=18',
    'django>=2.0',
    'pytest',
    'django-extensions',
]

setup(
    name='judge_gamble',
    url='https://github.com/deadlylaid/judge_gamble',
    description='judge gamble',
    install_requires=install_requires
)

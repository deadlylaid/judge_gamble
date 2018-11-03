from setuptools import setup


setup_requires = [
    'setuptools>=35.0.2',
]

install_requires = [
    'pip>=18',
    'flask',
    'pytest',
]

setup(
    name='judge_gamble',
    url='https://github.com/deadlylaid/judge_gamble',
    description='judge gamble',
    install_requires=install_requires
)
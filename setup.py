from setuptools import setup, find_packages

setup(
    name='suikawari',
    version="0.0.1",
    packages=find_packages(),
    description='スイカ割りのゲームです',
    url='https://github.com/tamako1025h/suikawari',
    author='tamako',
    author_email='tamakoDev@gmail.com',
    include_package_data=True,
    entry_points={'console_scripts': [
        'suikawari = suikawari.main:main',
    ]},
)
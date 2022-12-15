from setuptools import setup, find_packages

setup(
    name='suikawari',
    version="0.0.1",
    packages=['suikawari','suikawari.image'],
    description='スイカ割りのゲームです',
    url='https://github.com/tamako1025h/suikawari',
    author='tamako',
    author_email='tamakoDev@gmail.com',
    include_package_data=True,
)
console_scripts = ['suikawari=suikawari.main:main']
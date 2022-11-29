from setuptools import setup, find_packages

setup(
    name='Module_7_dz',
    version='1',
    description='Very useful code',
    url='https://github.com/Nataleia08/Module_7_dz',
    author='Orlovska Nataliia',
    author_email='nataleia.orlovska@gmail.com',
    license='MIT',
    packages=find_packages(include=["Module7dz"]),
    # install_requires=['markdown'],
    entry_points={'console_scripts': [
        'clean-folder = Module_7_dz.clean']},
)

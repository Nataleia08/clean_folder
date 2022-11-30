from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1',
    description='Very useful code',
    url='https://github.com/Nataleia08/clean_folder',
    author='Orlovska Nataliia',
    author_email='nataleia.orlovska@gmail.com',
    package_dir={"clean_folder:clean_folder"}
    # license='MIT',
    packages=find_packages(include=["cleanfolder"]),
    entry_points={'console_scripts': [
        'clean-folder = clean_folder.clean:main']},
)

from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1',
    description='Very useful code',
    long_description="A function that sorts files and folders.",
    url='https://github.com/Nataleia08/clean_folder',
    author='Orlovska Nataliia',
    author_email='nataleia.orlovska@gmail.com',
    packages=find_packages(include=["cleanfolder"]),
    entry_points={'console_scripts': [
        'clean-folder = clean_folder.clean:main']},
    classifiers=[
        "Python version :: Python :: 3",
        "Licence :: OSI :: MIT Licence"
    ],
    package_dir={"clean_folder": "clean_folder"},
    python_requires=">=3.7"

)

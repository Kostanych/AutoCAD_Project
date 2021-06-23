import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="AutocadProject",
    version="0.0.1",
    author="Konstantin Sviblov",
    author_email="kostanych1@gmail.com",
    description="Let's make AutoCAD and Python bff!",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=required
)

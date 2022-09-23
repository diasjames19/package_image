from setuptools import setup, processando_img

with open("README.md", "r") as f:
    page_description = f.read()

with open("requerimento.txt") as f:
    requerimento = f.read().splitlines()

setup(
    name="processando_img",
    version="0.0.1",
    author="James",
    author_email="diasjames@hotmail.com",
    description="Teste de pacote",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="my_github_repository_project_link"
    packages=find_packages(),
    install_requires=requerimento,
    python_requires='>=3.10.5',
)
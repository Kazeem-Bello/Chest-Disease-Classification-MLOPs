import setuptools

with open("README.md", "r", encoding = "utf-8") as file:
    long_description = file.read()


__version__ = "0.0.0"

repo_name = "Chest-Disease-Classification-MLOPs "
author_user_name = "Kazeem-Bello"
src_repo = "chest_disease_classification"
author_email = "bel.kazeem@gmail.com"

setuptools.setup(
    name = src_repo,
    version = __version__,
    author = author_user_name,
    author_email = author_email,
    description = "A python package for CNN App",
    long_description = long_description,
    url = f"https://github.com/{author_user_name}/{repo_name}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{author_user_name}/{repo_name}/issues"
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where = "src")
)
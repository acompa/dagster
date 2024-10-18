from pathlib import Path

from setuptools import find_packages, setup


def get_version():
    version = {}
    with open(Path(__file__).parent / "dagster_notdiamond/version.py", encoding="utf8") as fp:
        exec(fp.read(), version)

    return version["__version__"]


ver = get_version()
# dont pin dev installs to avoid pip dep resolver issues
pin = "" if ver == "1!0+dev" else f"=={ver}"
setup(
    name="dagster-notdiamond",
    version=ver,
    author="Not Diamond",
    author_email="support@notdiamond.ai",
    license="Apache-2.0",
    description="A Not Diamond client resource for interacting with the Not Diamond API.",
    url="https://github.com/dagster-io/dagster/tree/master/python_modules/libraries/dagster-notdiamond",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=["dagster_notdiamond_tests*"]),
    install_requires=[
        f"dagster{pin}",
        "notdiamond",
    ],
    zip_safe=False,
)

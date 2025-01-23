import re
from pathlib import Path
import pkg_resources as pkg
from setuptools import find_packages, setup

# Settings
FILE = Path(__file__).resolve()
ROOT = FILE.parent  # root directory
README = (ROOT / "README.md").read_text(encoding="utf-8")
REQUIREMENTS = [f'{x.name}{x.specifier}' for x in pkg.parse_requirements((ROOT / 'requirements.txt').read_text())]

def get_version():
    file = ROOT / 'ultralytics/__init__.py'
    return re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', file.read_text(), re.M)[1]

setup(
    name="YOLOv8-DeepSORT-Object-Tracking",  # Change this to your project's name
    version=get_version(),  # version of your package
    python_requires=">=3.7.0",
    license='GPL-3.0',
    description='YOLOv8 with DeepSORT for Object Tracking',
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/YOLOv8-DeepSORT-Object-Tracking",  # Change to your repo
    project_urls={
        'Bug Reports': 'https://github.com/your_username/YOLOv8-DeepSORT-Object-Tracking/issues',
        'Source': 'https://github.com/your_username/YOLOv8-DeepSORT-Object-Tracking',
    },
    author="Your Name",
    author_email='your_email@example.com',
    packages=find_packages(),  # Automatically find all packages
    include_package_data=True,
    install_requires=REQUIREMENTS,  # Use the requirements.txt file for dependencies
    extras_require={
        'dev': [
            'check-manifest', 'pytest', 'pytest-cov', 'coverage', 'mkdocs', 'mkdocstrings[python]', 'mkdocs-material'
        ],
    },
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
    ],
    keywords="machine-learning, deep-learning, vision, ML, DL, AI, YOLO, YOLOv8, object-tracking, DeepSORT",
    entry_points={
        'console_scripts': [
            'yolo = ultralytics.yolo.cli:cli',  # Entry point for running YOLO commands
            'ultralytics = ultralytics.yolo.cli:cli',
        ],
    },
)

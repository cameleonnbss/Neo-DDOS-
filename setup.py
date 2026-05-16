from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="neo-strike",
    version="3.0.0",
    author="Security Researcher",
    author_discord="cameleonmortis_new",
    description="Advanced multi-vector network stress testing tool for authorized security research",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cameleonnbss/Neo-DDOS",
    packages=find_packages(),
    install_requires=[
        'requests>=2.31.0',
        'fake-useragent>=1.4.0',
        'dnspython>=2.4.0',
        'colorama>=0.4.6',
        'psutil>=5.9.0',
        'scapy>=2.5.0',
        'cryptography>=41.0.0',
    ],
    entry_points={
        'console_scripts': [
            'neo-strike=main:main',
        ],
    },
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Security",
    ],
)

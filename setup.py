from setuptools import setup, find_packages
import os
path = os.path.join(os.path.dirname(__file__),"requirements.txt")

about = {}

with open(path,"r") as req_files:
    requirements = req_files.readlines()

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

NAME = "binance-ema"
DESCRIPTION = ("Get crypto coin informations & calculate the custom or constant indicators. (WITH BINANCE API)")
AUTHOR = "Emre MENTESE"
URL = "https://github.com/emrementese/binance-ema"
VERSION = "0.1.0"

setup(
    name=NAME,
    version=VERSION,
    license="MIT",
    description=DESCRIPTION,
    long_description=readme,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email= "emrmentese@gmail.com",
    url=URL,
    keywords=["Binance", "Public API","EMA","MACD","TRADE","Crypto","Coin","Indicators","BTC","ETH","USDT"],
    install_requires=[req for req in requirements],
    packages=find_packages('binancema'),
    package_dir={'': 'binancema'},
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.6",
)

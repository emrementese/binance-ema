from setuptools import setup, find_packages

about = {}

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

NAME = "binance-ema"
DESCRIPTION = ("Get crypto coin informations & calculate the custom or constant indicators. (WITH BINANCE API)")
AUTHOR = "Emre MENTESE"
URL = "https://github.com/emrementese/binance-ema"
VERSION = "0.1.7"
URLS = {
  'MyWebsite': 'http://www.emrementese.com/',
  'Github': 'https://github.com/emrementese',
  'Source': 'https://github.com/emrementese/binance-ema',
  'Download': 'https://pypi.org/project/binance-ema/#files',
}

setup(
    name=NAME,
    version=VERSION,
    license="MIT",
    description=DESCRIPTION,
    long_description=readme,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email= "emrmentese@gmail.com",
    project_urls = URLS,
    url=URL,
    keywords=["Binance", "Public API","EMA","MACD","TRADE","Crypto","Coin","Indicators","BTC","ETH","USDT"],
    install_requires=[
        "binance-connector==1.10.0",
    ],
    packages=find_packages('src'),
    package_dir={'':'src'},
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

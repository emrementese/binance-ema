from setuptools import setup, find_packages

about = {}

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

NAME = "binance-ema"
DESCRIPTION = ("Get crypto coin informations & calculate the custom or constant indicators. (WITH BINANCE API)")
AUTHOR = "Emre MENTESE"
URL = "https://github.com/emrementese/binance-ema"
VERSION = "0.1.5"
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
        "attrs==21.4.0",
        "autobahn==21.11.1",
        "Automat==20.2.0",
        "binance-connector==1.10.0",
        "certifi==2021.10.8",
        "cffi==1.15.0",
        "charset-normalizer==2.0.10",
        "constantly==15.1.0",
        "cryptography==36.0.1",
        "hyperlink==21.0.0",
        "idna==3.3",
        "incremental==21.3.0",
        "pyasn1==0.4.8",
        "pyasn1-modules==0.2.8",
        "pycparser==2.21",
        "pyOpenSSL==21.0.0",
        "requests==2.27.1",
        "service-identity==21.1.0",
        "six==1.16.0",
        "Twisted==21.7.0",
        "txaio==21.2.1",
        "typing_extensions==4.0.1",
        "urllib3==1.26.8",
        "zope.interface==5.4.0",
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

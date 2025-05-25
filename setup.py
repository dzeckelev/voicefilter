from setuptools import setup, find_packages

setup(
    name="voicefilter-lite",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch>=1.12",
        "torchaudio",
    ],
    include_package_data=True,
)

from setuptools import setup, find_packages

setup(
    name="voicefilter",
    version="0.1.0",
    description="Speaker-conditioned VoiceFilter-Lite implementation",
    packages=find_packages(),         # найдёт модуль voicefilter и подмодули
    install_requires=[
        "torch>=1.7",
        "torchaudio",
    ],
    include_package_data=True,
)

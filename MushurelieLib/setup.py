from setuptools import setup, find_packages

setup(
    name="MushurelieLib",
    version="0.1",
    author="Mushurelie",
    author_email="mushurelieoff@gmail.com",
    description="Une bibliothèque Python pour simplifier des tâches réseau et Discord.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Mushurelie/MushurelieLib",
    packages=find_packages(),
    install_requires=[
        "psutil",  # Ajoute ici les dépendances nécessaires
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

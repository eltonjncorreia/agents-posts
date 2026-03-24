from setuptools import setup, find_packages

setup(
    name="produzir_substack",
    version="0.1.0",
    description="Pipeline multi-agente para Substack com PydanticAI e GitHub Models",
    author="Elton",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pydantic-ai",
        "pydantic-settings",
        "requests",
        "feedparser",
        "python-dotenv",
    ],
)

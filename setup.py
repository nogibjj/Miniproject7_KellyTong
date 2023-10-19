from setuptools import setup, find_packages

# make sure the etl script outputs properly

setup(
    name="ETLKellyTong",
    version="0.1.0",
    description="ETLpipline",
    author="Kelly Tong",
    author_email="ht117@duke.edu",
    packages=find_packages(),
    install_requires=[
        "databricks-sql-connector",
        "pandas",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "etl_query=main:main",
        ],
    },
)

from setuptools import find_packages, setup

setup(
    name="jaffle_shop",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        "jaffle_shop": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-bigquery<1.9",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)


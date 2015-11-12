import setuptools


if __name__ == '__main__':
    setuptools.setup(
        name="shoop-simple-theme",
        version="1.0.0",
        description="Shoop Simple Theme",
        packages=setuptools.find_packages(),
        include_package_data=True,
        entry_points={"shoop.addon": "shoop_simple_theme=shoop_simple_theme"}
    )

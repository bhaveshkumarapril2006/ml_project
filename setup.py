from setuptools import setup, find_packages

def get_requirements(file_path):
    with open(file_path) as file:
        requirements = [
            req.strip()
            for req in file
            if req.strip() and not req.strip().startswith("-e")
        ]
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Bhavesh",
    author_email="bhaveshkumarapril2006@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)

from setuptools import setup, find_packages

setup(
    name="rt_viz_framework",
    version="1.0.0",
    author="Your Name",
    description="A high-performance real-time telemetry visualization toolkit",
    packages=find_packages(),
    install_requires=[
        "matplotlib",
        "numpy",
    ],
    entry_points={
        'console_scripts': [
            'rt-viz=src.dashboard:main', # This creates a terminal command
        ],
    },
    python_requires='>=3.10',
)
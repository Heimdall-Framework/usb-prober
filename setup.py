import setuptools

with open('README.md') as readme:
    long_description = readme.read()

setuptools.setup(
    name='USB Prober',
    version='1.0.2',
    author='Ivan Zlatanov',
    author_email='me@iv.an',
    description='A lightweight script that lists all connected USB devices.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Heimdall-Framework/usb-prober',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts':[
            'uprobe = prober.prober:main' 
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4'   
)
import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='pynamicui',
    version='0.0.5',
    description='dynamic web-like UIs using a declarative syntax',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/zacharie410/PynamicUI',
    author='zacharie410',
    license='Apache Software License',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only'
    ],
    python_requires='>=3.7',
    packages=setuptools.find_packages(),
    install_requires=[
        'customtkinter'
    ],
    include_package_data=True
)

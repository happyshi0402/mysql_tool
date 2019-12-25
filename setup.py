import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='MySQL-Tool',
    version='1.0.1',
    description='pymysql module use.',
    url='https://github.com/happyshi0402/mysql_tool.git',
    author='Wang Shifeng',
    author_email='wsf121116@163.com',
    maintainer="Wang Shifeng",
    maintainer_email="wsf121116@163.com",
    license='MIT',
    install_requires=["pymysql>=0.9.3"],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    packages=setuptools.find_packages(),
    python_requires='>=2.7',
    
)

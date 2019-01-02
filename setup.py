import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='MySQL-Tool',
    version='0.0.3',
    description='MysqlDb module use.',
    long_description=long_description,
    url='https://github.com/happyshi0402/mysql_tool.git',
        
    author='Wang Shifeng',
    author_email='wsf121116@163.com',
    license='MIT',

    install_requires=["Mysql-python"
    ],

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
    
)

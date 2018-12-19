from distutils.core import setup

setup(
    name='MySQL-Tool',
    version='0.0.1',
    description='MysqlDb工具的进一步封装调用，使调用方法更简单.',
    url='https://github.com/happyshi0402/mysql_tool.git',
        
    author='Wang Shifeng',
    author_email='wsf121116@163.com',
    license='MIT',

    install_requires=[
    ],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: Chinese',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
    ],
    packages=['mysql_tool'],
    
)

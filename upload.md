python setup.py sdist
python setup.py upload -r http://upload.pypi.org/legacy

python setup.py sdist bdist_wheel

python -m pip install --user --upgrade twine

https://packaging.python.org/tutorials/packaging-projects/#uploading-your-project-to-pypi

twine upload dist/*

twine upload --repository-url https://test.pypi.org/legacy/ dist/*
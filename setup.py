from setuptools import setup


setup(
    name='pytest-blockage',
    url='https://github.com/singleplatform-eng/pytest-blockage',
    version='0.3.0+singleplatform.1',
    description='Disable network requests during a test run.',
    long_description=(open('README.rst').read() +
                      open('CHANGELOG.rst').read()),
    license='BSD',
    author='SinglePlatform Engineering Team',
    author_email='techservices@singleplatform.com',
    install_requires=['pytest'],
    py_modules=['pytest_blockage'],
    entry_points={'pytest11': ['blockage = pytest_blockage']},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Private :: Do Not Upload',
    ]
)

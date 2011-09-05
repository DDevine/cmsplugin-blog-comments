from setuptools import setup, find_packages
import os

setup(
    name='cmsplugin-blog-comments',
    version='0.7',
    description='',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.txt')).read(),
    author='Oyvind Saltvik',
    author_email='oyvind.saltvik@gmail.com',
    url='http://github.com/fivethreeo/cmsplugin-blog-comments/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    test_suite = "cmsplugin_blog_comments.test.run_tests.run_tests",
    include_package_data=True,
    zip_safe=False,
    install_requires=['cmsplugin-blog'],
)

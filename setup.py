from setuptools import setup, find_packages

# get around issues importing sqlalchemy
main_ns = {}
ver_path = convert_path('sabridge/version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

tests_require = [
    'Django>=1.2,<1.4',
]
setup(
    name='django-sabridge',
    version=main_ns['__version__'],
    author='John Paulett, Laszlo Hegedus',
    author_email='john@paulett.org, laszlo.hegedus@cherubits.hu',
    url='https://django-sabridge.readthedocs.org',
    description = 'Provides SQLAlchemy access to Django models.',
    license='BSD',
    packages=find_packages(exclude=('tests',)),
    zip_safe=True,
    install_requires=[
        'sqlalchemy>=0.6.0',
    ], 
    tests_require=tests_require,
    extras_require={'test': tests_require},
    test_suite='runtests.runtests',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Database',
        'Topic :: Software Development'
    ],
)

from setuptools import setup, find_packages
import os
import cms


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

def get_version():
    import glob
    import re
    import os

    version = None
    for d in glob.glob('*'):
        if not os.path.isdir(d):
            continue
        module_file = os.path.join(d, '__init__.py')
        if not os.path.exists(module_file):
            continue
        for v in re.findall("""__version__ *= *['"](.*)['"]""",
                open(module_file).read()):
            assert version is None
            version = v
        if version:
            break
    assert version is not None
    if os.path.exists('.git'):
        import subprocess
        p = subprocess.Popen(['git','describe','--dirty','--match=v*'],
                stdout=subprocess.PIPE)
        result = p.communicate()[0]
        assert p.returncode == 0, 'git returned non-zero'
        new_version = result.split()[0][1:]
        assert not new_version.endswith('-dirty'), 'git workdir is not clean'
        assert new_version.split('-')[0] == version, '__version__ must match the last git annotated tag'
        version = new_version.replace('-', '.')
    return version

setup(
    author="Patrick Lauber",
    author_email="digi@treepy.com",
    name='django-cms',
    version=get_version(),
    description='An Advanced Django CMS',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='https://www.django-cms.org/',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.4,<1.6',
        'django-classy-tags>=0.3.4.1',
        'south>=0.7.2',
        'html5lib',
        'django-mptt>=0.5.1,<0.5.3',
        'django-sekizai>=0.7',
    ],
    tests_require=[
        'django-reversion>=1.6.6',
        'Pillow==1.7.7',
        'Sphinx==1.1.3',
        'Jinja2==2.6',
        'Pygments==1.5',
        'dj-database-url==0.2.1',
        'django-hvad',
    ],
    packages=find_packages(exclude=["project", "project.*"]),
    include_package_data=True,
    zip_safe=False,
    test_suite='runtests.main',
)

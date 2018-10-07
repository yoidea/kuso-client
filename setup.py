from setuptools import setup, find_packages


setup(
    name='kuso',
    version='0.1',
    packages=find_packages(),
    install_requires=['numpy'],
    entry_points={
        'console_scripts':
            'kuso = kuso.main:main'
    },
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
)

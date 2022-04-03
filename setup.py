from setuptools import setup

setup(
    name='doodstream_api',
    version='0.0.1',
    description='unofficial doodstream API wrapper.',
    long_description=open("README.md", "r",encoding="utf8").read(),
    long_description_content_type="text/markdown",
    keywords="api doodstream video hosting unlimited wrapper",
    url='https://github.com/adityash4rma/doodstream',
    author='Aditya Sharma',
    author_email='adityasharma13373@gmail.com',
    packages=['doodstream_api'],
    install_requires=[
          'requests',
          'click',
          'bs4',
      ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
      ],
    zip_safe=False
)
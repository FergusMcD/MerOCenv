from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setup(name='MerOCenv',
      version='0.0.1',
      description='Python module for the netCDF files manipulations',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url="https://github.com/carmelosammarco/MerOCenv",
      author='Carmelo Sammarco',
      author_email='sammarcocarmelo@gmail.com',
      license='gpl-3.0',
      python_requires='~=3.6',

      install_requires=[
        'ftputil>=3.4',
        'motuclient>=1.8.1',
        'netCDF4>=1.4.2',
        'csv342>=1.0.0', 
        'pandas>=0.23.4', 
        'xarray>=0.11.0', 
        'shapely>=1.6.4.post1', 
        'fiona>=1.8.4',
        'cdo>=1.4.0',
        'nco'
      ],
      packages=find_packages(),
      
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python :: 3.6',
       ], 

)

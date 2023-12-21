from setuptools import setup

setup(name='clean_folder',
      version='0.0.1',
      description='Very usefull code',
      url='https://github.com/AlyonaEcnos/clean_folder',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']},
      packages=['clean_folder'],
      zip_safe=False)
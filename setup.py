import subprocess
import os
from setuptools import setup

path = __file__

setup(name='completions',
      version='0.1',
      description='Auto completions for argparse without argcomplete bugs',
      url='https://github.com/eytans/PythonCompletions',
      author='Eytan Singher',
      author_email='eytan.singher@gmail.com',
      license='MIT',
      install_requires=[
          'argcomplete',
      ],
      packages=['completions'],
      scripts=['bin/get_python_completions', 'bin/python_autocomplete.sh'],
      zip_safe=False,
      include_package_data=True)

# subprocess.call(['python_autocomplete.sh', '--install'])
from distutils.core import setup
setup(
  name = 'reclassification',         # How you named your package folder (MyLib)
  packages = ['reclassification'],   # Chose the same as "name"
  version = '0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Functions for calculation of reclassification metrics NRI and IDI.',   # Give a short description about your library
  long_description = 'Defines NRI(Net reclassification index) and IDI(Integrated discrimination improvement)',
  author = 'Theodore Morley',                   # Type in your name
  author_email = 'ted@elmgatefarm.com',      # Type in your E-Mail
  url = 'https://github.com/user/morleytj',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/morleytj/reclassification/archive/refs/tags/v_02.tar.gz',    # I explain this later on
  keywords = ['RECLASSIFICATION','DATA','MACHINE LEARNING', 'NRI', 'IDI', 'MODELLING', 'PERFORMANCE'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.10'
  ],
)


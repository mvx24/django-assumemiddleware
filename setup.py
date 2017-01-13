from setuptools import setup, find_packages

setup(
	name='django-assumemiddleware',
	version='1.0.0',
	description='Simple Django middleware that allows people to assume the identity of another user when making requests.',
	url='https://github.com/mvx24/django-assumemiddleware',
	author='mvx24',
	author_email='cram2400@gmail.com',
	license='MIT',
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Console',
		'Framework :: Django',
		'License :: OSI Approved :: MIT License',
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: POSIX',
		'Operating System :: Unix',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 2 :: Only',
		'Topic :: System :: Systems Administration'
	],
	keywords='django assume mimic login user access middleware',
	packages=find_packages(),
	install_requires=['django'],
)

from setuptools import setup, find_packages
import PPark
 
setup(
	name='PPark',
	version=PPark.__version__,
	packages=find_packages(),
	author="aabbfive",
	author_email="diffyheart@gmail.com",
	description="Advanced Lexer",
	long_description=open('README.md').read(),
	include_package_data=False,
	url='https://github.com/aabbfive/PPark',
	download_url = 'https://github.com/aabbfive/PPark/releases',
	keywords = ['lexer', 'ast', 'compiler'],
	classifiers=[
		"Programming Language :: Python",
		"Development Status :: 4 - Beta",
		"License :: OSI Approved :: MIT License",
		"Natural Language :: English",
		"Programming Language :: Python :: 2",
		"Programming Language :: Python :: 3",
		"Topic :: Text Processing",
	],
	license="MIT",
)
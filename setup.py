#!/usr/bin/env python3
# encoding: utf-8

import os
#from distutils.core import setup, Extension
from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
from distutils import sysconfig
from distutils.ccompiler import new_compiler
from distutils import sysconfig

def readme():
	with open("README.md", "r") as fh:
		long_desc = fh.read()
	return long_desc

def get_version():
	with open("VERSION", 'r') as f:
		v = f.readline().strip()
		return v


#os.environ["CC"] = "gcc"
cc = ["-O", "-g", "-msse2"]
cflags = ["-DSHOW_HELP", "-DSHOWSIM", "-DUNIX", "-DTIMES", "-DHZ=100", "-DTHR_EXIT=pthread_exit", "-DM10_CONS", "-DUSE_MMAP", "-DUSE_FSEEKO", "-DHAS_INTTYPES", "-DSAMP_STATS", "-DPGM_DOC", "-DBIG_LIB64"]
hflags = ['-o']
lflags = ['-lm']
#compile_args = ["-Wno-sign-compare -std=c++11"] # -Wall -O2"]

filenames = {'pylib' : [],
			 'comp_lib9' : ['-DCOMP_MLIB'], 'compacc2e' : ['-DCOMP_MLIB'],
			 'initfa' : ['-DFASTA'], 'cal_cons2' : ['-DFASTA'],
			 'scaleswn' : ['-DLOCAL_SCORE'],
			 'wm_align' : [], 'dropnfa' : [], 'mmgetaa' : [], 'build_ares' : [], 'doinit' : [], 'mshowbest' : [],
			 'nmgetlib' : [], 'c_dispn' : [], 'lib_sel' : [], 'ncbl2_mlib' : [], 'karlin' : [], 're_getlib' : [],
			 'url_subs' : [], 'mrandom' : [], 'apam' : [], 'htime' : [], 'mshowalign2' : [], 'doalign2' : []
			 }

def extension(name, cflags, lflags):
	module = Extension(name,
			#language='c++',
			extra_compile_args = cflags,
			extra_link_args    = lflags,
			include_dirs       = [os.path.join(os.getcwd(), 'src')],
			#library_dirs       = [os.getcwd(),],
			sources            = ['src/' + name + '.c']  )
	return module

def compiler(name, cflags): 
	c = new_compiler()
	c.compiler_so.extend(cflags)
	c.add_include_dir( sysconfig.get_python_inc() )
	c.add_include_dir("./src")
	#print(vars(c))
	c.compile(['src/' + name + '.c'])
	#c.link_shared_lib(objects, "fasta36", output_dir=workdir)

def extension(name, cflags, lflags):
	ext = Extension(name,
			extra_compile_args = cflags,
			extra_link_args    = lflags,
			include_dirs       = ['.','..',os.path.join(os.getcwd(), 'src')],
			library_dirs       = [os.getcwd(),],
			sources            = ['src/python.c'],
			extra_objects      = ['src/' + f + '.o' for f in filenames]
			)
	print(vars(ext))
	return ext


def main():
	for name,flags in filenames.items():
		compiler(name, cc + cflags + flags)
	setup (
		name = 'fasta36',
		version = get_version(),
		author = "Katelyn McNair, W.R. Pearson & D.J. Lipman",
		author_email = "deprekate@gmail.com",
		description = 'A python port of the fasta36 C code',
		long_description = readme(),
		long_description_content_type="text/markdown",
		url =  "https://github.com/deprekate/fasta36",
		scripts=[],
		classifiers=[
			"Programming Language :: Python :: 3",
			"License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
			"Operating System :: OS Independent",
		],
		python_requires='>3.5.2',
		packages=find_packages(),
		#install_requires=[''],
		ext_modules = [
						extension('fasta36', cc, lflags)
					  ]
		#depends=['comp_lib9']
		#cmdclass={"build_ext":custom_build_ext}
		#cmdclass={"build_ext":build_ext}
	)


if __name__ == "__main__":
	main()

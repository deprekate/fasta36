#!/usr/bin/env python3
# encoding: utf-8

import os
#from distutils.core import setup, Extension
from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
from distutils import sysconfig
from distutils.ccompiler import new_compiler
from distutils import sysconfig

class custom_build_ext(build_ext):
	def build_extensions(self):
		# Override the compiler executables. Importantly, this
		# removes the "default" compiler flags that would
		# otherwise get passed on to to the compiler, i.e.,
		# distutils.sysconfig.get_var("CFLAGS").
		#print(distutils.sysconfig._config_vars)
		compiler = sysconfig.get_config_vars("CC")
		self.compiler.set_executable("compiler_so", compiler)
		self.compiler.set_executable("compiler_cxx", compiler)
		self.compiler.set_executable("linker_so", compiler)
		build_ext.build_extensions(self)

#os.environ["CC"] = "gcc"
compile_args = ["-O", "-g", "-msse2", "-DSHOW_HELP", "-DSHOWSIM", "-DUNIX", "-DTIMES", "-DHZ=100", "-DTHR_EXIT=pthread_exit", "-DM10_CONS", "-DUSE_MMAP", "-DUSE_FSEEKO", "-DHAS_INTTYPES", "-DSAMP_STATS", "-DPGM_DOC", "-DBIG_LIB64"]
#compile_args = ["-Wno-sign-compare -std=c++11"] # -Wall -O2"]
link_args	= []

def extension(name, cargs):
	module = Extension(name,
			#language='c++',
			extra_compile_args=cargs + ['-DCOMP_MLIB'],
			extra_link_args=link_args,
			include_dirs=[
						 '.',
						 '...',
						 os.path.join(os.getcwd(), 'src'),
			],
			library_dirs = [os.getcwd(),],
			sources = ['src/' + name + '.c']  )
	return module

ofiles = "pylib.o comp_lib9.o compacc2e.o mshowbest.o build_ares.o re_getlib.o mshowalign2.o htime.o apam.o doinit.o initfa.o scaleswn.o karlin.o dropnfa.o wm_align.o cal_cons2.o nmgetlib.o mmgetaa.o c_dispn.o ncbl2_mlib.o lib_sel.o mrandom.o url_subs.o"
mod = Extension('fasta36',
		#language='c++',
		extra_compile_args=compile_args, #['-O','-g','-msse2'],
		extra_link_args = ['-lm'],
		include_dirs=[
					 '.',
					 '...',
					 os.path.join(os.getcwd(), 'src'),
		],
		library_dirs = [os.getcwd(),],
		sources = ['src/python.c'], #, 'src/pylib.c'],
		#extra_objects = ['libfasta36.so']
		extra_objects = ['src/' + f for f in ofiles.split(' ')]
		)

def readme():
	with open("README.md", "r") as fh:
		long_desc = fh.read()
	return long_desc

def get_version():
	with open("VERSION", 'r') as f:
		v = f.readline().strip()
		return v

def main():
	cfiles = "pylib.c comp_lib9.c compacc2e.c mshowbest.c build_ares.c re_getlib.c mshowalign2.c htime.c apam.c doinit.c initfa.c scaleswn.c karlin.c dropnfa.c wm_align.c cal_cons2.c nmgetlib.c mmgetaa.c c_dispn.c ncbl2_mlib.c lib_sel.c mrandom.c url_subs.c"
	c = new_compiler()
	c.compiler_so.extend(compile_args)
	c.compiler_so.append('-DCOMP_MLIB')
	workdir = "."
	c.add_include_dir( sysconfig.get_python_inc() )
	c.add_include_dir("./src")
	objects = c.compile(['src/' + f for f in cfiles.split(' ')])
	#c.link_shared_lib(objects, "fasta36", output_dir=workdir)
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
						mod
					  ],
		depends=['comp_lib9']
		#cmdclass={"build_ext":custom_build_ext}
		#cmdclass={"build_ext":build_ext}
	)


if __name__ == "__main__":
	main()

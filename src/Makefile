# makefile for fasta3, fasta3_t.  Use makefile.pvm for pvcompxx.
#
#  $Name:  $ - $Id: Makefile.os_x86_64 1228 2013-09-26 19:46:29Z wrp $
#
# 12-Dec-2007 - modified to allow compilation of both accelerated and
# non-accelerated Smith-Waterman

# the -DDEBUG option provides additional debugging information, particularly
# with -D on the command line.

# use -DBIG_LIB64 to generate 64-bit offsets in map_db .xin files

SHELL=/bin/bash

#CC= cc -O -g -arch x86_64 -msse2
CC= cc -O -g -msse2
LIB_DB=
#LIB_DB=-lz

#
# standard line for normal searching
CFLAGS= -DSHOW_HELP -DSHOWSIM -DUNIX -DTIMES -DHZ=100 -DMAX_WORKERS=4 -DTHR_EXIT=pthread_exit  -DM10_CONS -DIS_LITTLE_ENDIAN -DUSE_MMAP -DUSE_FSEEKO -DHAS_INTTYPES -DSAMP_STATS -DPGM_DOC -DBIG_LIB64 -DLIB_MEM=12

LDFLAGS= -arch x86_64

HFLAGS= -o

#for Linux, MacOS, DEC Unix V4.0
THR_SUBS = pthr_subs2
THR_LIBS =
THR_CC =

# set up files for SSE2/Altivec acceleration
#
#include ../make/Makefile.sse_alt

# Altivec acceleration
#
#DROPGSW_O = $(DROPGSW_SSE_O)
#DROPLAL_O = $(DROPLAL_SSE_O)
#DROPGNW_O = $(DROPGNW_SSE_O)
#DROPLNW_O = $(DROPLNW_SSE_O)

#include Makefile36m.common

COMP_LIBO=comp_mlib9.o	# reads database into memory for multi-query without delay
COMP_THRO=comp_mthr9.o	# threaded version

WORK_THRO=work_thr2.o
GETSEQO = 

# memory mapping for 0FASTA, 5PIRVMS, 6GCGBIN
LGETLIB= $(GETSEQO) lgetlib.o lgetaa_m.o
NGETLIB=nmgetlib

LIB_M= -lm 
NCBL_LIB=ncbl2_mlib.o

#
#DROPNSW_O = dropnsw.o  wm_align.o calcons_sw.o
#DROPBD_O = dropsbd.o wm_align.o calcons_fa.o
#DROPTFA_O = drop_tfa.o wm_align.o calcons_tfa.o
#DROPFF_O = drop_ff2.o calcons_ff.o
#DROPFS_O = drop_fs2.o calcons_fs.o
#DROPFM_O = drop_fm.o calcons_fm.o
#DROPTFF_O = drop_tff.o calcons_tff.o
#DROPTFS_O = drop_tfs.o calcons_tfs.o
#DROPTFM_O = drop_tfm.o calcons_tfm.o

#COMPACC_TO = compacc.o	# used with comp_lib5.c/comp_lib7.c
#COMPACC_SO = compacc.o
#COMPACC_TO = compacc2_t.o  # used with comp_lib5e.c/comp_lib7e.c/comp_lib8.c
COMPACC_SO = compacc2_s.o

SHOWBESTC = mshowbest.c
SHOWBESTO = showbest.o build_ares.o
SHOWALIGN = mshowalign2
SHOWALIGN_T = mshowalign2_t
SHOWALIGN_S = mshowalign2_s
LSHOWALIGN = lshowalign
#MWH = mw.h 
#MWHP = mw.h

DROPNFA_O = drop_nfa.o wm_align.o calcons_fa.o

fasta36 : $(COMP_LIBO) $(COMPACC_SO) $(SHOWBESTO) re_getlib.o $(SHOWALIGN_S).o htime.o apam.o doinit.o init_fa.o scale_se.o karlin.o $(DROPNFA_O) $(LGETLIB) c_dispn.o $(NCBL_LIB) lib_sel.o mrandom.o url_subs.o
	$(CC) $(HFLAGS) fasta36 $(COMP_LIBO) $(COMPACC_SO) $(SHOWBESTO) re_getlib.o $(SHOWALIGN_S).o htime.o apam.o doinit.o init_fa.o $(DROPNFA_O) scale_se.o karlin.o $(LGETLIB) c_dispn.o $(NCBL_LIB) lib_sel.o url_subs.o mrandom.o $(LIB_M) $(LIB_DB)

comp_mlib9.o : comp_lib9.c mw.h structs.h defs.h param.h
	$(CC) $(THR_CC) $(CFLAGS) -DCOMP_MLIB -c comp_lib9.c -o comp_mlib9.o

doinit.o : doinit.c defs.h param.h rstruct.h upam.h structs.h uascii.h aln_structs.h
	$(CC) $(THR_CC) $(CFLAGS) -c doinit.c

init_fa.o : initfa.c defs.h param.h rstruct.h upam.h structs.h aln_structs.h
	$(CC) $(THR_CC) $(CFLAGS) -c -DFASTA initfa.c -o init_fa.o

htime.o : htime.c
	$(CC) $(THR_CC) $(CFLAGS) -c htime.c

compacc2_s.o : compacc2e.c upam.h uascii.h param.h rstruct.h structs.h $(MWH) defs.h aln_structs.h drop_func.h dyn_string.h
	$(CC) $(THR_CC) $(CFLAGS) -DCOMP_MLIB -c compacc2e.c -o compacc2_s.o

apam.o : apam.c defs.h param.h uascii.h upam.h
	$(CC) $(THR_CC) $(CFLAGS) -c apam.c

showbest.o : $(SHOWBESTC) $(MWH) defs.h param.h rstruct.h structs.h  aln_structs.h drop_func.h
	$(CC) $(THR_CC) $(CFLAGS) -c $(SHOWBESTC) -o showbest.o

build_ares.o : build_ares.c $(MWH) defs.h param.h rstruct.h structs.h  aln_structs.h drop_func.h dyn_string.h
	$(CC) $(THR_CC) $(CFLAGS) -c build_ares.c -o build_ares.o

$(SHOWALIGN_T).o : $(SHOWALIGN).c $(MWHP) defs.h structs.h param.h rstruct.h aln_structs.h drop_func.h dyn_string.h
	$(CC) $(THR_CC) $(CFLAGS) -DCOMP_THR -c $(SHOWALIGN).c -o $(SHOWALIGN_T).o

$(SHOWALIGN_P).o : $(SHOWALIGN).c $(MWHP) defs.h structs.h param.h rstruct.h aln_structs.h drop_func.h dyn_string.h
	$(CC) $(THR_CC) $(CFLAGS) -DMPI_SRC -c $(SHOWALIGN).c -o $(SHOWALIGN_P).o

$(SHOWALIGN_S).o : $(SHOWALIGN).c $(MWHP) defs.h structs.h param.h rstruct.h aln_structs.h drop_func.h dyn_string.h
	$(CC) $(THR_CC) $(CFLAGS) -c $(SHOWALIGN).c -o $(SHOWALIGN_S).o

$(LSHOWALIGN).o : $(SHOWALIGN).c $(MWHP) defs.h structs.h param.h rstruct.h aln_structs.h drop_func.h dyn_string.h
	$(CC) $(THR_CC) $(CFLAGS) -DLALIGN -c $(SHOWALIGN).c -o $(LSHOWALIGN).o

re_getlib.o : re_getlib.c mw.h mm_file.h
	$(CC) $(THR_CC) $(CFLAGS) -c re_getlib.c

lib_sel.o : lib_sel.c defs.h structs.h rstruct.h
	$(CC) $(THR_CC) $(CFLAGS) -c lib_sel.c

c_dispn.o : c_dispn.c defs.h structs.h param.h rstruct.h aln_structs.h
	$(CC) $(THR_CC) $(CFLAGS) -c c_dispn.c

karlin.o : karlin.c param.h rstruct.h
	$(CC) $(THR_CC) $(CFLAGS) -c karlin.c

scale_se.o : scaleswn.c defs.h param.h rstruct.h structs.h $(MWH) alt_parms.h
	$(CC) $(THR_CC) $(CFLAGS) -DLOCAL_SCORE -c scaleswn.c -o scale_se.o

drop_nfa.o : dropnfa.c dropnfa.h param.h rstruct.h defs.h drop_func.h dyn_string.h
	$(CC) $(THR_CC) $(CFLAGS) -c dropnfa.c -o drop_nfa.o

calcons_fa.o : cal_cons2.c defs.h param.h rstruct.h a_mark.h
	$(CC) $(THR_CC) $(CFLAGS) -DFASTA -c cal_cons2.c -o calcons_fa.o

lgetlib.o : $(NGETLIB).c altlib.h upam.h uascii.h mm_file.h
	$(CC) $(THR_CC) $(CFLAGS) -c $(NGETLIB).c -o lgetlib.o

lgetaa_m.o : mmgetaa.c altlib.h ncbl2_head.h upam.h uascii.h mm_file.h
	$(CC) $(THR_CC) $(CFLAGS) -c mmgetaa.c -o lgetaa_m.o


ncbl2_mlib.o : ncbl2_mlib.c ncbl2_head.h mm_file.h
	$(CC) $(THR_CC) $(CFLAGS) -c ncbl2_mlib.c -o ncbl2_mlib.o

url_subs.o : url_subs.c structs.h param.h rstruct.h
	$(CC) $(THR_CC) $(CFLAGS) -c url_subs.c


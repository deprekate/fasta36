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

#
# standard line for normal searching
#CFLAGS= -DSHOW_HELP -DSHOWSIM -DUNIX -DTIMES -DHZ=100 -DMAX_WORKERS=4 -DTHR_EXIT=pthread_exit  -DM10_CONS -DIS_LITTLE_ENDIAN -DUSE_MMAP -DUSE_FSEEKO -DHAS_INTTYPES -DSAMP_STATS -DPGM_DOC -DBIG_LIB64 -DLIB_MEM=12
CFLAGS= -DSHOW_HELP -DSHOWSIM -DUNIX -DTIMES -DHZ=100 -DTHR_EXIT=pthread_exit -DM10_CONS -DUSE_MMAP -DUSE_FSEEKO -DHAS_INTTYPES -DSAMP_STATS -DPGM_DOC -DBIG_LIB64

HFLAGS= -o

COMP_LIBO=comp_mlib9.o	# reads database into memory for multi-query without delay

# memory mapping for 0FASTA, 5PIRVMS, 6GCGBIN
LGETLIB= lgetlib.o lgetaa_m.o
NGETLIB=nmgetlib

LIB_M= -lm 
NCBL_LIB=ncbl2_mlib.o

COMPACC_SO = compacc2_s.o

SHOWBESTC = mshowbest.c
SHOWBESTO = showbest.o build_ares.o
SHOWALIGN = mshowalign2
SHOWALIGN_S = mshowalign2_s
MWH = mw.h 
MWHP = mw.h

DROPNFA_O = drop_nfa.o wm_align.o calcons_fa.o

fasta36 : $(COMP_LIBO) $(COMPACC_SO) $(SHOWBESTO) re_getlib.o $(SHOWALIGN_S).o htime.o apam.o doinit.o init_fa.o scale_se.o karlin.o $(DROPNFA_O) $(LGETLIB) c_dispn.o $(NCBL_LIB) lib_sel.o mrandom.o url_subs.o
	$(CC) $(HFLAGS) fasta36 $(COMP_LIBO) $(COMPACC_SO) $(SHOWBESTO) re_getlib.o $(SHOWALIGN_S).o htime.o apam.o doinit.o init_fa.o $(DROPNFA_O) scale_se.o karlin.o $(LGETLIB) c_dispn.o $(NCBL_LIB) lib_sel.o url_subs.o mrandom.o $(LIB_M)

comp_mlib9.o : comp_lib9.c mw.h structs.h defs.h param.h
	$(CC) $(CFLAGS) -DCOMP_MLIB -c comp_lib9.c -o comp_mlib9.o

compacc2_s.o : compacc2e.c upam.h uascii.h param.h rstruct.h structs.h $(MWH) defs.h aln_structs.h drop_func.h dyn_string.h
	$(CC) $(CFLAGS) -DCOMP_MLIB -c compacc2e.c -o compacc2_s.o

showbest.o : $(SHOWBESTC) $(MWH) defs.h param.h rstruct.h structs.h  aln_structs.h drop_func.h
	$(CC) $(CFLAGS) -c $(SHOWBESTC) -o showbest.o

build_ares.o : build_ares.c $(MWH) defs.h param.h rstruct.h structs.h  aln_structs.h drop_func.h dyn_string.h
	$(CC) $(CFLAGS) -c build_ares.c -o build_ares.o

re_getlib.o : re_getlib.c mw.h mm_file.h
	$(CC) $(CFLAGS) -c re_getlib.c

$(SHOWALIGN_S).o : $(SHOWALIGN).c $(MWHP) defs.h structs.h param.h rstruct.h aln_structs.h drop_func.h dyn_string.h
	$(CC) $(CFLAGS) -c $(SHOWALIGN).c -o $(SHOWALIGN_S).o

htime.o : htime.c
	$(CC) $(CFLAGS) -c htime.c

apam.o : apam.c defs.h param.h uascii.h upam.h
	$(CC) $(CFLAGS) -c apam.c

doinit.o : doinit.c defs.h param.h rstruct.h upam.h structs.h uascii.h aln_structs.h
	$(CC) $(CFLAGS) -c doinit.c

init_fa.o : initfa.c defs.h param.h rstruct.h upam.h structs.h aln_structs.h
	$(CC) $(CFLAGS) -c -DFASTA initfa.c -o init_fa.o

scale_se.o : scaleswn.c defs.h param.h rstruct.h structs.h $(MWH) alt_parms.h
	$(CC) $(CFLAGS) -DLOCAL_SCORE -c scaleswn.c -o scale_se.o

karlin.o : karlin.c param.h rstruct.h
	$(CC) $(CFLAGS) -c karlin.c

drop_nfa.o : dropnfa.c dropnfa.h param.h rstruct.h defs.h drop_func.h dyn_string.h
	$(CC) $(CFLAGS) -c dropnfa.c -o drop_nfa.o

# wm_align?

calcons_fa.o : cal_cons2.c defs.h param.h rstruct.h a_mark.h
	$(CC) $(CFLAGS) -DFASTA -c cal_cons2.c -o calcons_fa.o

lgetlib.o : $(NGETLIB).c altlib.h upam.h uascii.h mm_file.h
	$(CC) $(CFLAGS) -c $(NGETLIB).c -o lgetlib.o

lgetaa_m.o : mmgetaa.c altlib.h ncbl2_head.h upam.h uascii.h mm_file.h
	$(CC) $(CFLAGS) -c mmgetaa.c -o lgetaa_m.o

c_dispn.o : c_dispn.c defs.h structs.h param.h rstruct.h aln_structs.h
	$(CC) $(CFLAGS) -c c_dispn.c

ncbl2_mlib.o : ncbl2_mlib.c ncbl2_head.h mm_file.h
	$(CC) $(CFLAGS) -c ncbl2_mlib.c -o ncbl2_mlib.o

lib_sel.o : lib_sel.c defs.h structs.h rstruct.h
	$(CC) $(CFLAGS) -c lib_sel.c

# mrandom?

url_subs.o : url_subs.c structs.h param.h rstruct.h
	$(CC) $(CFLAGS) -c url_subs.c

clean : 
	$(RM) $(wildcard *.o)
	$(RM) fasta36

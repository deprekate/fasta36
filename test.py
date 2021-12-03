#!/usr/bin/env python3
import fasta36
import faulthandler; faulthandler.enable()

seq = ">fig|101570.3.peg.1  [Salmonella typhimurium bacteriophage ES18] [Phage terminase, small subunit]\nMTGLTIKQEAFCQAYIETGNASEAYRTAYAADKMKPEVVHVQACKLQDNP\nKIALRIKELRGEIKQRHNVTVDSLLAELEEARQKALSAETPQSSAAVAAT\nMGKAKLVGLDKQIIDHTSSDGTMATKPTTIRLVGVDPANGKPS"

filename = '/Users/katelyn/develop/fasta36/10702.1.fas'

print(fasta36.best_pid(seq, filename))

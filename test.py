#!/usr/bin/env python3
import fasta36
import faulthandler; faulthandler.enable()

seq = ">test\nMTGLTIKQEAFCQAYIETGNASEAYRTAYAADKMKPEVVHVQACKLQDNPKIALRIKELRGEIKQRHNVTVDSLLAELEEARQKALSAETPQSSAAVAATMGKAKLVGLDKQIIDHTSSDGTMATKPTTIRLVGVDPANGKPS"

filename = '/Users/katelyn/develop/fasta36/10702.1.fas'

print(fasta36.best_pid(seq, filename))

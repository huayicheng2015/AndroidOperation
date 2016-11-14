import os
from argparse import ArgumentParser

parser = ArgumentParser()
group = parser.add_mutually_exclusive_group ()
group.add_argument ("-d","--debug",action="store_true",help="gradle debug")
group.add_argument ("-p","--preview",action="store_true",help="gradle preview")
group.add_argument ("-r","--release",action="store_true",help="gradle release")
args = parser.parse_args ()

if args.debug:
    print "gradle assembleDebug"
    os.system ("gradle assembleDebug")
elif args.preview:
    print "gradle assemblePreview"
    os.system ("gradle assemblePreview")
elif args.release:
    print "gradle assembleRelease"
    os.system ("gradle assembleRelease")
else:
    print "gradle assembleDebug"
    os.system ("gradle assembleDebug")

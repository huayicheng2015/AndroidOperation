import os
from argparse import ArgumentParser

parser = ArgumentParser()
group = parser.add_mutually_exclusive_group ()
parser.add_argument ("-p","--path",nargs="?",default="Cloud",type=str,help="the subdirectory in this project")
parser.add_argument ("-f","--file",nargs="?",default="strings_ecg.xml",type=str,help="the file to be operated")
group.add_argument ("-c","--copy",action="store_true",help="copy files")
group.add_argument ("-a","--add",action="store_true",help="git add files")
group.add_argument ("-d","--delete",action="store_true",help="delete the files")
arg = parser.parse_args ()
countries = ["af","am","ar","az",\
             "be","bg","bn","bs",\
             "ca","cs",\
             "da","de",\
             "el","es","et",\
             "fa","fi","fr",\
             "gu",\
             "he","hi","hr","hu","hy",\
             "id","in","is","it","iw",\
             "ja",\
             "ka","kk","km","kn","ko",\
             "lo","lt","lv",\
             "mk","ml","mn","mr","ms","my",\
             "nb","ne","nl","no",\
             "pa","pl","pt",\
             "rm","ro","ru",\
             "sh","si","sk","sl","sq","sr","su","sv","sw",\
             "ta","te","th","tl","tr",\
             "uk","ur",\
             "vi",\
             "zu"]
path = arg.path + os.sep + "res" + os.sep
file_name = arg.file
print path,file_name
for i in countries:
    if arg.copy:
        status = os.system ("copy " + path + "values-en" + os.sep + file_name + " " + path + "values-" + i + os.sep)
        print "copy " + path + "values-en" + os.sep + file_name + " " + path + "values-" + i + os.sep + "-----> " + str(status)
    elif arg.add:
        os.system ("git add " + path + "values-" + i + os.sep + file_name)
        print "git add " + path + "values-" + i + os.sep + file_name
    elif arg.delete:
        file_path_name = path + "values-" + i + os.sep + file_name
        if os.path.exists (file_path_name):
            os.system ("del " + file_path_name)
            print "del " + file_path_name
        else:
            print "There does not exist {}".format (file_path_name)
    else:
        print "No tasks"
        break

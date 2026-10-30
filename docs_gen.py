import os
from datetime import datetime
import shutil

#####################
### useful functions
#####################

def GetDateTimeNotice():
    dtArr=["!!! notice",
          f"\tPage generated: {datetime.now().date()} ({datetime.now().time()})",
          "\tFor updates/fixes contact: wraightATcern.ch"
        ]
    ### convert to string
    dtStr=""
    for ia in dtArr:
        dtStr+=f"{ia}\n\n"
    
    return dtStr

def GetFileList(theDir, theDict):

    print("Working on:",theDir)
    
    ### loop over files
    for f in [f for f in os.listdir(theDir)]:
        
        if "javascript" in f:
            print("- skip javascript stuff",f)
            continue

        ### files
        if os.path.isfile(os.path.join(theDir, f)):
            print("- got file:",f)
            theDict['files'].append(f)
        ### directory
        elif os.path.isdir(os.path.join(theDir, f)):
            print("- got directory:",f)
            theDict[f]={'files':[]}
            GetFileList(os.path.join(theDir, f), theDict[f])
        ### unknown
        else:
            print("- unknown:",f)
    
    return 


### build overview table
def BuildTable(theDict):
    
    tableArr=[]

    tableArr.append("| No. |  Title |  Comment | State |")
    tableArr.append("| --- | --- | --- | --- |")

    for k in sorted(theDict.keys()):
        # skip non-numerics (no chapters)
        if not k[0].isnumeric():
            continue
        tableArr.append(f"| {k} |")
        if type(theDict[k])==type({}) and "files" in theDict[k].keys():
            for f in theDict[k]['files']:
                # extract info.
                try:
                    numStr=f.split('_')[0]
                    nameStr=f.replace(numStr+"_",'').replace('.md','')
                # skip if wrong format
                except IndexError:
                    continue
                tableArr.append(f"| {numStr} | {nameStr} | | maintained |")

    return tableArr


#####################
### main function
#####################
def main():

    # timestamp index file
    with open("docs/index.md", "a") as content_file:
        content_file.write(GetDateTimeNotice())

    # # overview table
    # theDict={'files':[]}
    # GetFileList(os.getcwd()+"/docs", theDict)
    # with open("docs/0_Introduction/000_Overview.md", "a") as content_file:
    #     content_file.write("\n".join(BuildTable(theDict)))


    # ### update yml
    # # notebooks
    # with open("mkdocs.yml", "a") as content_file:
    #     for k,v in readmeFiles.items():
    #         content_file.write(f"  - {k}:\n")
    #         for x in v:
    #             content_file.write(f"    - {x}: {k+'/'+x+'.md'}\n")




### for commandline running
if __name__ == "__main__":
    main()
    print("All done.")

#! env python3
import src.website as website
import sys
import json

#ws = website.Website("d")
def main():
    syntax = json.load(open("config/syntax.json", 'r'))

    #args = sys.argv
    #print(args)

    if len(sys.argv) == 1:
        print(syntax["programName"] + syntax["syntaxMsg"]) #data.keys():
        sys.exit(1)
    else:
        command = findCommand(sys.argv, syntax)
        if command == None:
            print(syntax["programName"] + ": " +syntax["cmdNotFoundMsg"])
        
        if command["command"] == "--help":
            if len(sys.argv) == 2:
                print(syntax["programName"] + ": ")

                for key in syntax.keys():
                        if type(syntax[key]) == dict:
                            for curKey in syntax[key]:
                                print(printHelpSyntax(syntax, key, curKey))
            elif len(sys.argv) == 3:
                if sys.argv[2] in syntax:
                    print(f"{sys.argv[2]}: ")
                    for curKey in syntax[sys.argv[2]]:
                        print(printHelpSyntax(syntax, sys.argv[2], curKey))
                else:
                    print(f'{sys.argv[2]}: {syntax["cmdNotFoundMsg"]}')
        elif command["command"] == "website":
            if len(sys.argv) == 2:
                print(syntax["programName"] + ": " + syntax["invalidSyntaxMsg"])

                print(printHelpSyntax(syntax, sys.argv[1], "website"))            
            elif len(sys.argv) == 3:
                curWebsite = website.Website(sys.argv[2])
                print(curWebsite.isUrlValid)
                if curWebsite.isUrlValid != True:
                    print(syntax["programName"] + ": " + syntax["urlNotValidMsg"])
                else:
                    print(curWebsite.url)
                    curWebsite.analyse()


def findCommand(arguments, syntax):
    for key in syntax.keys():
        if type(syntax[key]) == dict:   # FIND ALL DICTS IN WHOLE JSON ARRAY
            #print("dict") 
            for curKey in syntax[key]:
                #print(syntax[key][curKey])
                if "alias" in syntax[key][curKey]:
                    #print("alias")
                    if sys.argv[1] == syntax[key][curKey]["command"] or sys.argv[1] == syntax[key][curKey]["alias"]:
                        return syntax[key][curKey]
                        break
                else:
                    if sys.argv[1] == syntax[key][curKey]["command"]:
                        return syntax[key][curKey]
                        break
def printHelpSyntax(syntax, key, secondKey):
    if "alias" in syntax[key][secondKey]:
        return f"   {syntax[key][secondKey]['command']} || {syntax[key][secondKey]['alias']}:\n        {syntax[key][secondKey]['description']}\n"
    elif "syntax" in syntax[key][secondKey]:
        return f"   {syntax[key][secondKey]['command']}:\n        {syntax[key][secondKey]['description']}\n        Syntax: {syntax['programName']} {syntax[key][secondKey]['syntax']}\n"
    else:
        return f"   {syntax[key][secondKey]['command']}:\n        {syntax[key][secondKey]['description']}\n"
 
main()
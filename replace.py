from sys import maxsize
maxsize = 100000000000

def static_replacor(code, attribute=[], ignore_suffixes=[]):
    attributes = ['src=', 'href='] 
    ignored_names = ["http", ".html", "#"]
    temporary = final = nal = ss = ""

    if attribute != []:
        attributes += attribute
    if ignore_suffixes != []:
        ignored_suffixes += ignore_suffixes
    
    inside = False

    for char in code:
        if not inside and final.split(" ")[-1] in attributes:
            # if the last word is in attributes to be replaced
            inside = True # we are inside the "" of the attribute
            final += '"' # it will finally be added to main string
            continue # pass the double qoutation and go on

        if inside and char == '"':
            # it means that we are at the end of attribute  
            inside = False  # the attribute has been finished and we are out of it

            ignored = False
            for name in ignored_names:
                if name in temporary:
                    ignored = True
                    break

                # some names like https and ... should not be replaced
                # because they are not one of static files
            if ignored:
                final += temporary
                final += '"'
                temporary = ""
                continue
            else:
                nal = f"{{% static '{temporary}' %}}"
                ss = f'{nal}"' # adding a double qoutation to the end of it
                final += ss
                temporary = ""
                continue

        if not inside:
            # they are other characters
            final += char

        elif inside:
            # add chars to temprorary to make decision for it later
            temporary += char
    
    return final


def manager(
            attributes=[], 
            ignore_suffixes=[], 
            file_address="input_file.txt", 
            destination="output.txt"
            ):
    code = None
    try:
        with open(file_address, "r") as input_file:
            code = input_file.read()
            print("I'm reading your file!")
    except:
        print("opening file was not done succesfully,check the file address and try again!")
        return
    
    if code == "" or code == None:
        print(f"the content of {file_address} is empty. check it.")
        return

    replaced_file = static_replacor(code, attributes, ignore_suffixes)

    try:
        with open(destination, "w+") as file:
            file.write(replaced_file)
            print("I did it successfully! open the file.")
    except:
        print("something with destination file went wrong, check it and try again...")
        return


if __name__ == "__main__":
    manager()
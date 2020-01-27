import re as regex

def case_filtering(x):

    if len (x) == 10:

        # rep3 = x.replace(".","-")

        return "%s-%s-%s" %(x[8::],x[5:7],x[0:4])

    if len(x) > 10:

        rep = regex.sub(r".\w$","",x)

        rep2 = rep.replace(".","-")

        return "%s-%s-%s" %(rep2[8::],rep2[5:7],rep2[0:4])


def m_correction(x):

    y = str(x)

    if y == "N":
        return "0"

    elif y == "Y":
        return "1" 


def extract_year(x):

    return x[-4::]


def find_word(x):

    y = x.lower()

    if "jaws" in y:
        return y

    if "shark" in y:
        return y


def genero_fixing(x):

    if x == True:

        return 1

    else:

        return 0


def int_converter(x):

    return str(x)

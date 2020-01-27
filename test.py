

# def find_word(x):

#         x.lower()

#         if "shark" in x:

#                 return x

#         # fd3[fd3['Título'].astype(str).str.contains("shark")]


# x= "baby shark tutririri"

# print(find_word(x))



# # fd3.Título = fd3["Título"].astype(str).apply(find_word)


# def extract_year(x):

#     return x[-4::]


# print(extract_year("15-12-1995"))


# def find_word(x):

#     x.lower()

#     if "jaws" in x:
    
#         return x


# print(find_word("Jaws"))


def extract_year(x):

    return int(x[-4::])


asd = extract_year("12-06-2017")

print(asd)

print(type(asd))

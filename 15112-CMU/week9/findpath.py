# this is the main function for findCategoryPath



def recurHelper(d, value, lst):
    for key in d:
        if (type(d[key])) != dict:
            if d[key] == value:
                lst.append(key)
                return lst
        else:
            if recurHelper(d[key], value, lst + [key]) == None:
                continue
            else:
                return recurHelper(d[key], value, lst + [key])


def findCategoryPath(d, value):
    lst = []
    return recurHelper(d, value, lst)





def testFindCategoryPath():
    print("Testing findCategoryPath...", end="")
    d = {"Sporting":
             {"Spaniel":
                  {"English Springer": "Betsy"},
              "Weimaraner": "Xeva",
              "Retriever":
                  {"Golden": "Sammo",
                   "Labrador": "Nya"}
              },
         "Working":
             {"Husky": "Stella",
              "Saint Bernard": "Rutherfurd",
              "Boxer": "Paximus"},
         "Herding":
             {"Corgi":
                  {"Welsh":
                       {"Cardigan": "Geb",
                        "Pembroke": "Niinja"}
                   },
              "Sheepdog":
                  {"Bergamasco": "Samur",
                   "Old English": "Duggy",
                   "Shetland": "Walker"}
              },
         "Other": "Kimchee"
         }
    value1 = "Samur"
    value2 = "Weimaraner"
    assert(findCategoryPath(d, value1) == ["Herding", "Sheepdog", "Bergamasco"])
    assert(findCategoryPath(d, value2) == None)
    print("Passed!")

# testFindCategoryPath()

d = {"Sporting":
             {"Spaniel":
                  {"English Springer": "Betsy"},
              "Weimaraner": "Xeva",
              "Retriever":
                  {"Golden": "Sammo",
                   "Labrador": "Nya"}
              },
         "Working":
             {"Husky": "Stella",
              "Saint Bernard": "Rutherfurd",
              "Boxer": "Paximus"},
         "Herding":
             {"Corgi":
                  {"Welsh":
                       {"Cardigan": "Geb",
                        "Pembroke": "Niinja"}
                   },
              "Sheepdog":
                  {"Bergamasco": "Samur",
                   "Old English": "Duggy",
                   "Shetland": "Walker"}
              },
         "Other": "Kimchee"
         }
print(findCategoryPath(d, "Samur"))
print(findCategoryPath(d, "Weimaraner"))
print(findCategoryPath(d, "Betsy"))
print(findCategoryPath(d, "Other"))

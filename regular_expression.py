import re
def find(A,B):

   searchmot = re.search(r'\b' + re.escape(B) + r'\b', A)
   if searchmot:
    return ("True ✅")
   else :
    return ("False ❌")


def Nbr(C):
  searchnmbr = re.search (r'\d',C)
  if searchnmbr :
    return "True ✅"
  else :
     return ("False ❌")


def Space (D):
  searchspace = re.sub(r'\s',"_",D)
  return searchspace

def Tele(T):
  searchtele = re.match(r'\b\d{2}-\d{3}-\d{5}\b',T)
  if searchtele :
    return " Phone number validate✅"
  else :
     return " Telephone number not validated ❌"


def Email(E):
  searchemail = re.search(r'[A-Za-z]+[a-z]+\.(com|ma)',E)
  if searchemail:
    return " Email validate ✅"
  else :
     return " Email not validated ❌"

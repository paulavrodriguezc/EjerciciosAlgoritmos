def validate_str():
    element=input("Please enter the letter you wish to search for in the list: ")
    while not element.isalpha or len(element)>1:
        element=input("Invalid input. Please enter the letter you wish to search for in the list: ")
    return element
def search(element: str, list_elements: list, index=0):
    if element==list_elements[index]:
        return element
    else:
        if index==len(list_elements)-1:
            if element==list_elements[index]:
                return element
            else: 
                return
        else:
            search(element, list_elements, index+1)
def main():
    list_elements=["a", "b", "c", "d", "e", "f", "g"]
    element=validate_str()
    result=search(element,list_elements)
    if result==None:
        print("The letter was not found.")
    else:
        print("The letter was found.")
main()
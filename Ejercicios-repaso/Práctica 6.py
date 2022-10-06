pathologies = {
    "Respiratory system": [
        {
            "id": 1,
            "name": "Cystic Fibrosis",
            "price": 300 	
        },
        {
            "id": 2,
            "name": "Emphysema",
            "price": 500
        },
        {
            "id": 3,
            "name": "Tuberculosis",
            "price": 450
        }
    ],
    "Nervous system": [
        {
            "id": 4,
            "name": "Parkinson",
            "price": 800 	
        },
        {
            "id": 5,
            "name": "Epilepsy",
            "price": 600
        }
    ],
    "Endocrine system": [
        {
            "id": 6,
            "name": "Diabetes",
            "price": 350 	
        },
        {
            "id": 7,
            "name": "Acromegaly",
            "price": 700
        },
        {
            "id": 8,
            "name": "Hashimoto's thyroiditis",
            "price": 900
        }
    ],   
}
number_client=0
patients={}
while True:
    option=int(input("Please select a valid option: \n1. Register and bill the patient \n2. See all patients registered. \n3. Exit \n--->"))
    if option==1:
        number_client+=1
        is_valid=False
        info_pathology=None
        while is_valid==False:
            id_pathology=int(input("Please enter the ID of the pathology: "))
            for system,sickness in pathologies.items():
                for pathology in sickness:
                    if pathology.get("id")==id_pathology:
                        is_valid=True
                        info_pathology=pathology
                        break
                    else:
                        is_valid=False
                if is_valid==True:
                    break
            if is_valid==False:
                print("Invalid ID.")
            else:
                break
        new_patient={"Name":"", "Last name":"", "Personal ID":0}
        for keys in new_patient.keys():
            new_patient[keys]=input(f"Please enter the patient's {keys}: ")
        patients[number_client]=new_patient
        new_patient["Pathology ID"]=id_pathology
        print("***RECEIPT***")
        print("Patient's information:")
        for key,value in patients.items():
                for key,value in new_patient.items():
                    print(f"*{key} - {value}")
        print("Pathology information:")
        for key,value in info_pathology.items():
                print(key,value)
    elif option==2:
        print(patients)
        selection=int(input("Please select the pathology that you would like to see the patients' list: \n1.Cystic Fibrosis \n2. Emphysema \n3. Tuberculosis \n4. Parkinson \n5. Epilepsy \n6. Diabetes \n7. Acromegaly \n.8 Hashimoto's thyroiditis \n--->"))
        to_print=[]
        for patient_number,patient_info in patients.items():
            check=patient_info["Pathology ID"]
            if check==selection:
                to_print.append(patient_number)
        for person in to_print:
            print("\n")
            for info,data in patients[person].items():
                if info!="Pathology ID":
                    print(f"* {info} - {data}")
    else:
        print("Thank you!")
        break
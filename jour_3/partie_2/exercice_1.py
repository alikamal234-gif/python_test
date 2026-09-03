def deviser(a,b):
    try :
        print(f"resultat est : {int(a) / int(b)}")
    except ValueError as v:
        print("valiable must be numbers")
    except ZeroDivisionError as z:
        print("can't deviser any number on ZERO")
    finally :
        print("Opération terminée.")



deviser(10,2)
deviser(10,0)
deviser(10,"a")
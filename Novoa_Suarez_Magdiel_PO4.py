#mb a bytes
try:
    def meg_a_bytes(mb):
         return mb * 1024 * 1024
#mb a kilo
    def meg_a_kilo(mb):
         return mb * 1024
#mb a giga
    def meg_a_giga(mb):
         return mb / 1024
#mb a tera
    def meg_a_tera(mb):
         return mb /(1024 * 1024)
    def main():
        print("ingrese que conversion quiere 1: mb a bytes, 2: mb a kilo, 3: mb a giga, 4: mb a tera: ")
        fu=input()
        mb=(input("ingrese la cantidad de mb a convertir: "))        
        if type(mb) != float or mb == 0:
            print("debe ingresar un numero y distnto de cero")
            return
        if fu== "1":
            print("haz escogido mb a bytes")
            print(mb,"mb son",meg_a_bytes(mb),"bytes")       

        if fu== "2":
            print("haz escogido mb a kilo")
            print(mb,"mb son",meg_a_kilo(mb),"kilo")
        if fu== "3":
            print("haz escogido mb a giga")
            print(mb,"mb son",meg_a_giga(mb),"giga")    
        if fu== "4":
            print("haz escogido mb a tera")
            print(mb,"mb son",meg_a_tera(mb),"tera")
        else:
            print("opcion no valida")
    
    if __name__ == "__main__":
        main()

    
except Exception as e:
    print("An error occurred:", e)

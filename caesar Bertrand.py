#Le programme qui suit permet de crypter un message, selon la methode cesar. Il permet aussi de décrypter un message, si l'on connait la clef de cryptage, ou non.
#Seul les lettres majuscules et minuscules sont coddés, les autres caracteres ne sont pas modifié.

#//////////variables//////////
    
clef = 0#entier qui prend la valeur de la clef
msg=""#liste des caracteres à crypter/décrypter
lsf=""#liste final   
rp="" #réponse utilisateur aux questions

#//////////fonctions//////////

#fonction appelée pour crypter, 
#arg: le message, la clef de cryptage
#return: le message crypter
def crypte(msg, clef) :
    ls = "" #variable , type: liste, portée: local
    for char in msg :
        #nombre "ASCII" correspondant au caractere, base 10
        nchar = ord(char)
        #on regarde si le caractere est une lettre miniscule :
        if(nchar >= ord('a') and nchar <= ord('z')) :      
            #nombre "ASCII" correspondant au caractere 'a'      
            na1 = ord('a')
            #numero du caractere, entre 0 et 25
            n = nchar - na1
            #numero du caractere codé, entre 0 et 25
            #utilisation du modulo : si (n + clef) > 26, alors (n + clef) % 26 = le reste de la division euclidienne (n + clef) / 26, tel que (n+clef) = (n+clef)%26 + k*26
            nc = (n + clef ) % 26
            #caractere codé
            charf = chr(nc+na1)
            #on ajoute cette lettre à notre liste
            ls = ls + charf
        #on regarde si le caractere est une majuscule : 
        elif(nchar >= ord('A') and nchar <= ord('Z') ):      
            #nombre "ASCII" correspondant au caractere 'A '      
            na1 = ord('A')
            #numero du caractere, entre 0 et 25
            n = nchar - na1
            #numero du caractere codé, entre 0 et 25
            nc = (n + clef ) % 26
            #caractere codé
            charf = chr(nc+na1)
            #on ajoute cette lettre à notre liste
            ls = ls + charf
        else :
             #si ce n'est pas une lettre, on ne modifie pas le caractere
            ls = ls + char
    return ls
    
#fonction appelée pour décrypter, 
#arg: le message, la clef de décryptage
#return: le message décrypter
def decrypte(msg, clef) :
    ls="" #variable , type: liste , portée: local
    for char in msg :
        #nombre "ASCII" correspondant au caractere, base 10
        nchar = ord(char)
        #on regarde si le caractere est une minuscule :
        if(nchar >= ord('a') and nchar <= ord('z')) :
            #nombre "ASCII" correspondant au caractere 'a '      
            na1 = ord('a')
            #numero du caractere, entre 0 et 25
            n = nchar - na1
            #numero du caractere décodé, entre 0 et 25
            nc = (n - clef + 26) % 26
            #caractere décodé
            charf = chr(nc+na1)
            #on ajoute cette lettre à notre liste
            ls = ls + charf
        #on regarde si le caractere est une majuscule : 
        elif(nchar >= ord('A') and nchar <= ord('Z') ):
            #nombre "ASCII" correspondant au caractere 'A'       
            na1 = ord('A')
            #numero du caractere, entre 0 et 25
            n = nchar - na1
            #numero du caractere décodé, entre 0 et 25
            nc = (n - clef + 26) % 26
            #caractere décodé
            charf = chr(nc+na1)
            #on ajoute cette lettre à notre liste
            ls = ls + charf
        else :
             #si ce n'est pas une lettre, on ne modifie pas le caractere
            ls = ls + char
    return ls

#fonction appelée pour tester si une liste est un nombre, 
#arg: la liste ( reponse )
#return: 1 si c'est un chiffre, 0 si s'en est pas un
def testRP(rp) :
#on definie une variable, puis pour chaque partie de rp, si le caractere correspondant est un chiffre, alors on incremente i.
#Si a la fin, i = taille de la reponse, alors c'est un chiffre
    i = 0
    for char in rp :
        if(ord(char) >= ord('0') and ord(char) <= ord('9')) :
            i = i + 1
    if(i == len(rp)) :
        return 1
    else :
        return 0 

#//////////code//////////

#on demande à l'utilisateur s'il veux décryter ou crypter :
flag = 1 # variable tampon, pour savoir si on reste dans la boucle
while flag:
    rp = input("Voulez vous cryter ou décrypter ? ( C pour crytage, DC pour décryptage ) : ")
	
#code de crytage
    #si reponse est 'C', alors on crypte (on est gentil, on accepte aussi les minuscules ^^)
    if(rp == 'C' or rp == 'c') :
        flag = 0 #réponse correct, on sort donc de la boucle
        print("bien, crytons alors :) ")
        #on demande la clef
        flag = 1
        while(flag) :
            rp = input("quelle est la clef de crytage ? : ")
            if(testRP(rp)) :
                clef = eval(rp)
                flag = 0
            else :
                print("clef non valide")
                print("")
                
        #on demande le message
        msg = input("message : ")
        #on execute la fonction pour crypter, la variable lsf prend le message crypté
        lsf = crypte(msg, clef)
        #on écrit le message crypter à l'écran
        print(lsf)  
#code de decryptage
    #si reponse est 'DC', alors on decrypte(ici on accepte les minuscules :p)
    elif(rp == 'DC' or rp == 'dc'):
        flag = 0 #réponse correct, on sort donc de la boucle
        print("bien, décrytons alors :) ")		

        flg = 1 # variable tampon, pour savoir si on reste dans la boucle
        #on demande si on connait la clef, le cas écheans, l'utilisateur la donne, sinon il tape 'N'
        while(flg) :
            rp = input("Connaissez vous la clef de coddage ? ( si oui, donnez la, si non tappez N ) : ")
            #on test si la réponse est un chiffre
            isKey = testRP(rp2)
            #si la reponse est un chiffre, on decrypte, avec comme clef ce chiffre
            if(isKey) :
                flg = 0 #on sort de la boucle
                #la clef prend la valeur de la réponse convertie en entier
                clef = eval(rp)
                #on demande le message à décrypter
                msg = input("message : ")
                #on execute la fonction pour décrypter, la variable lsf prend le message crypté
                lsf = decrypte(msg, clef)
                #on écrit le message décrypter à l'écran
                print(lsf)
            #si la réponse est non :
            elif (rp == 'N' or rp == 'n' ) :
                flg = 0 #on sort de la boucle
                print("")
                print("vous ne connaissez pas la clef, execution de l'algorithme de recherche")
                #message
                msg = input("message : ")                
                
                    #explication algorithme
                #Dans la langue francaise, la lettre la plus présente est le 'e',
                #l'algorithme va parcourir le message et noter le nombre de fois qu'une lettre est présente
                #Pour un grand message, le 'e' devrais donc etre majoritaire, et nous donner la clef :)

                #on converti les lettres majuscules en minuscules, et on supprime les autres caracteres:
                me = "" # le message en minuscule, sans ponctuation
                for char in msg :
                    if(ord(char) >= ord('a') and ord(char) <= ord('z')) :
                        me = me + char
                    elif(ord(char) >= ord('A') and ord(char) <= ord('Z')) :
                        me = me + chr(ord(char) + 32)
                #on creer une liste,
                #0 correspond au nombre de fois qu'il y a 'a', et 25 pour 'z'
                lt = []
                for i in range(26) :
                    lt.append(0)
                #on parcours le message, pour chaque lettre, on incremente le nombre correspondant :
                for char in me :
                    #numero du caractere, entre 0 et 25
                    n = ord(char) - ord('a')
                    lt[n] = lt[n] + 1                
                #boucle de recherche de clef, et de proposition de résultat
                pasTrouve = 1 
                nbe = 0 # on compte le nombre d'essaie de l'algorithme
                while(pasTrouve) :                   
                    #variable qui prend la position de la lettre la plus représenté
                    pg = 0
                    #on regarde la lettre la plus présente:
                    for i in range(26) :
                        if(lt[pg] < lt[i]) :
                           pg = i
                    #si la lettre la plus représenté l'est -1 fois, ca veux dire qu'on a tout essayé, on arrête l'algorithme
                    if(lt[pg] == -1) :
                        print("toutes les possibilités ont été testés !!!")
                        pasTrouve = 0
                        #on force la sortie de la boucle
                        break;
                    #position de e, entre 0 et 25
                    p = ord('e') - ord('a')
                    #la clef est égal au modulo de la somme de 26 et de la difference entre la position du 'e' potentiel et du 'e' reel :)
                    clef = (26 + pg - p) % 26
                    #si la clef = 0, on n'execute pas le code 
                    if(clef != 0) :
                        #on incremente le compteur d'essais
                        nbe = nbe + 1
                        print("")
                        print("clef potentiel : ", clef)
                        #on decrypte le resultat, selon la clef definie ci-dessus
                        lsf = decrypte(msg, clef)
                        
                        print("message decrypte potentiel : ")
                        print(lsf)
                        #on demande à l'utilisateur si c'est ca:
                        flag = 1
                        rp = ""
                        while flag :
                            rp = input("c'est ca ? ( O ou N ) : ")
                            if(rp == 'O' or rp == 'o') :
                                pasTrouve = 0
                                flag = 0
                                print("bien, la clef est donc ", clef, " et il a fallu ", nbe, " essaies ")
                            elif(rp == 'N' or rp == 'n'):
                                print("reeissayons alors :)" )
                                flag = 0
                            else :
                                print("je vais prendre ca pour un non :p")
                                flag = 0
                    else :
                        print("clef == 0")
                    #on fixe le plus grand nombre de fois qu'il y a une lettre à -1, comme ca on prendras le 2 eme plus grand( ou un egal)
                    lt[pg] = -1
                print("fin de l'algorithme") 
                                    
#autre
    #la réponse ne convient pas, on repose la question
    else :
        flag = 1
print("")
	



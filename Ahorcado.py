""" Ahorcado """
#-----Functions-----
def draw_man(man, word_list, letters_rem):
        print("-"*62 + f"\n\
   ______\n\
  |/    |\n\
  |     {man[5]}\n\
  |    {man[3]}{man[4]}{man[2]}\n\
  |   {man[1]} {man[0]}\n\
 _|_\n\
/___\\        ", end = "")
        #Correct letters
        for i in word_list:
            if i in letters_rem:
                print("_", end = " ")
            else:
                print(i, end = " ")
        print("\n")
        #Wrong letters
        for i in letters_no:
            print(i, end = " | ")
        print("\n" + "-"*62)

#-----Variables-----
not_number = False
lives = 6
man = ["\\_", "_/", "/", "\\", "|", "0"]
print_man = [" ", " ", " ", " ", "  ", "  "]
letters_no = []

#-------Print-------
print("*"*20 + " [ Ingresar palabra ] " + "*"*20)

#-------Input-------
word = input("Ingrese la palabra sin que los otros participantes la vean\n- ").lower()
print("*"*62)

#--Input-Correcton--
word_list = list(word)
for i in word:
    if i == " ":
        word_list.remove(i)
    try:
        int(i)
        word_list.remove(i)
    except:
        word_list = word_list
word = "".join(word_list)
letters_rem = word_list
word_list_2 = word_list
word_list_2.pop(0)
word_list = list(word)

#-------Game-------
if word_list == []:
    print("Palabra no válida")
else:
    print("\n"*32)
    print("*"*62 + "\n    _      _                                         _         \n\
   / \\    | |__     ___    _ __    ___    __ _    __| |   ___  \n\
  / Δ \\   | '_ \\   / _ \\  | '__|  / __|  / _` |  / _` |  / _ \\ \n\
 / ___ \\  | | | | | (_) | | |    | (__  | (_| | | (_| | | (_) |\n\
/_/   \\_\\ |_| |_|  \\___/  |_|     \\___|  \\__,_|  \\__,_|  \\___/ \n\n" + "*"*62)
    while True:
#------Output------
        draw_man(print_man, word_list, letters_rem)
#-----Game-End-----
        resp = input("\n- ")
        if resp in letters_rem:
            print("\ncorrecto!")
            for i in word_list:
                if resp == i:
                    letters_rem.remove(i)
            if letters_rem == []:
                draw_man(print_man, word_list, letters_rem)
                print("\n" + "*"*24 + " [ GANASTE ] " + "*"*24)
                break
        else:
            print("\nincorrecto :(")
            lives -= 1
            print_man[lives] = man[lives]
            letters_no.append(resp)
            if lives == 0:
                draw_man(print_man, word_list, letters_rem)
                print("\n" + "*"*21 + " [ FÍN DEL JUEGO ] " + "*"*21)
                break
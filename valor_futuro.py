import math


def menu():
    run_a = 1
    while run_a != 0:
        print('que valor desea conocer?')
        form = input("""Presione el numer indicado de acuerdo a lo que necesite
                    1 = Valor Futuro
                    2 = Valor presente
                    3 = interés del periodo
                    4 = Total de Periodos
                    0 = Detener programa
        : """)
        try:
            form = (int)(form)
            if form == 1:
                vf, vfi = future_val()
                print_result(vf, "Valor Futuro con tasa evectiva ")
                print_result(vfi, "Valor Futuro con tasa nominal ")
            elif form == 2:
                vp = present_val()
                print_result(vp, "Valor presente ")
            elif form == 3:
                i = interes()
                print_result((str)(i*100)+'%',"Interes ")
            elif form == 4:
                p = periodos()
                print_result(p,"Preriodo evaluado ")
            elif form == 0:
                run_a = 0
            elif form > 4 or form < 0:
                print_numerr()

        except Exception as e:
            print_numerr()
            menu()


def future_val() -> float:
    vp = input_float('Ingrese el Valor presente: ')
    i = input_float('Ingrese Interes del periodo: ') / 100
    n = input_float('Ingrese el total de periodos: ')
    # VF = VP*((1+i)^n)
    tn = tasa_nominal(i,n)
    fn = vp*((1+tn)**n)
    vf = vp*((1+i)**n)
    return vf, fn


def present_val() -> float:
    vf = input_float('Ingrese el Valor futuro: ')
    i = input_float('Ingrese Interes del periodo: ') / 100
    n = input_float('Ingrese el total de periodos: ')
    # VP = VF/(1+i)^n
    vp = vf/((1+i)**n)
    return vp


def interes() -> float:
    vf = input_float('Ingrese el Valor futuro: ')
    vp = input_float('Ingrese el valor presente: ')
    n = input_float('Ingrese el total de periodos: ')
    # VF/VP = (1 + i)^n 
    # (VF/VP)^(1/n) - 1 = i
    i = (vf/vp)**(1/n) - 1
    return i


def periodos() -> float:
    vf = input_float('Ingrese el Valor futuro: ')
    vp = input_float('Ingrese el valor presente: ')
    i = input_float('Ingrese el interes: ') / 100
    # VF/VP = (1 + i)^n 
    # (VF/VP)^(1/n) = 1 + i
    # (1/n)*ln*(VF/VP) = ln(1+i)
    # ln(VF/VP)=  n*ln(1+i)
    # ln(VF/VP)/ln(1+i) = n
    n = math.log(vf/vp) / math.log(1 + i)
    return n


def tasa_nominal(i,n) -> float:
    tn = n*(((1+i)**(1/n)-1))
    return tn


def print_numerr():
    print('\033[1m---------------------------------\033[0;0m')
    print('\033[1m| Ingrese un numero entre 0 y 4 |\033[0;0m')
    print('\033[1m---------------------------------\033[0;0m')


def input_float(message: str) -> float:
    try:
        num = (float)(input(message))
        return num
    except:
        print('\033[1m| DEBE INGRESAR SOLO NUMEROS |\033[0;0m')


def print_result(result: float, message: str) -> None:
    print('\033[1m----------------------------------------\033[0;0m')
    print('\033[1mEl '+ message + 'es: ' + (str)(result) + '\033[0;0m')
    print('\033[1m----------------------------------------\033[0;0m')
    print('\n')


if __name__ == '__main__':
    print('\033[1mBienvenido!!\033[0;0m')
    menu()

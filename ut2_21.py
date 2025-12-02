import subprocess
import platform
res=""
while res != 'salir': 
    res=input('desseas saber informacin del sistemas????????si/no/salir: ').lower()
    sis=platform.system()
    if res == 'si':
        print('su sistema operativo es',sis,
                        '\nsu version es',platform.version(),
                        '\n el nombre de su maquina es',platform.node(),
                        '\n su versin de python es',platform.python_version(),
                        '\n la arquitectura de su sistema es',platform.machine())
        if sis == 'Windows':
            print('su sistema Windows es malisimo')
        elif sis == 'Linux':
            print('su sistema Linux es muy bueno')
        elif sis == 'Darwin':
            print('su sistema MacOS no lo usa nadie')
        else:
            print('sistema operativo no reconocido')       
    elif res == 'no':
        print('okey, no se mostrara informacion del sistema')
    else:
        print('comando no reconocido, por favor ingrese si, no o salir')
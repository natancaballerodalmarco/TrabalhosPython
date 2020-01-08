from time import sleep

Terminal = ['Policial', 'Presidiário', 'Piloto', 'Oficial1', 'Oficial2', 'ChefeServico', 'Comissária1', 'Comissária2']
Aviao = []

def Movimento():
    print('Smart Fortwo saindo...')
    sleep(3.0)
    print('...\n...Smart Fortwo chegou.\n')
    sleep(3.0)

def ida(p1, p2, Terminal):
    print(f'Terminal:\n{Terminal}')
    print(f'Embarcando: \n{Terminal[p1]} e {Terminal[p2]}')
    Movimento()
    Aviao.append(Terminal[p1])
    Aviao.append(Terminal[p2])
    Terminal.remove(Terminal[p2])
    Terminal.remove(Terminal[p1])

def volta(p1, Aviao):
    print(f'Avião:\n{Aviao}')
    print(f'Embarcando: \n{Aviao[p1]}')
    Movimento()
    Terminal.append(Aviao[p1])
    Aviao.remove(Aviao[p1])

def volta_especial(p1, p2, Aviao):
    print(f'Avião:\n{Aviao}')
    print(f'Embarcando: \n{Aviao[p1]} e {Aviao[p2]}')
    Movimento()
    Terminal.append(Aviao[p1])
    Terminal.append(Aviao[p2])
    Aviao.remove(Aviao[p2])
    Aviao.remove(Aviao[p1])

ida(0, 1, Terminal)
volta(0, Aviao)
ida(0, 6, Terminal)
volta(1, Aviao)
ida(0, 5, Terminal)
volta(3, Aviao)
ida(0, 4, Terminal)
volta(4, Aviao)
ida(0, 3, Terminal)
volta(4, Aviao)
ida(0, 2, Terminal)
volta_especial(4, 6, Aviao)
ida(0, 2, Terminal)
volta(6, Aviao)
ida(0, 1, Terminal)
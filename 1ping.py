import socket
import time

def ping(host, port):

    rttMedio = 0
    tempos = []
    recebidos = 0
    enviar = 10

    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for i in range(enviar):
        try:
            mensagem = "teste"

            time.sleep(1.0)
            tempoInicial = time.time()

            cliente.sendto(mensagem.encode(), (host, port))

            cliente.settimeout(0.25)

            recebido = cliente.recv(1024)

            tempoFinal = time.time()
            tempos.append(tempoFinal - tempoInicial)

            recebidos += 1

            print("menssagem recebida:", recebido.decode())

        except socket.timeout:
            print("erro")

    cliente.settimeout(None)

    cliente.close()

    taxa = ((enviar - recebidos)/enviar)*100

    if len(tempos) > 1:
        rttMedio = sum(tempos) / len(tempos)

    print("\n --- sd.dcc.ufla.br ping estatisticas ---")
    print('enviados: {}, recebidos: {}, taxa de perda: {}%'.format(enviar, recebidos, taxa))
    print('rtt medio = {}ms'.format(rttMedio*100))

host = "sd.dcc.ufla.br"
port = 6000

ping(host, port)
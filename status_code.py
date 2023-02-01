import requests
from notifypy import Notify


def notificar_resultado(mensagem):
    notification = Notify()
    notification.title = "Verificação dos sites"
    notification.message = mensagem
    notification.send()


def verificar_sites():
    hosts = [
        "https://hhseletrica.com.br",
        "https://projetoniara.com.br",
        "https://pontedeconcreto.com.br",
        "https://portalapi.unifeijr.com.br",
        "https://compjunior.com.br",
        "https://athena.compjunior.com.br",
        "https://sistema.compjunior.com.br",
        "https://compweek.com.br",
    ]

    cairam = []

    print("teste")

    for url in hosts:
        try:
            site = requests.get(url, timeout=1)
            print(site.status_code)
        except requests.Timeout:
            cairam.append(url)

    if len(cairam) == len(hosts):
        notificar_resultado("Todos os sites estão fora do ar, o servidor deve ter caido")
    elif len(cairam) == 0:
        notificar_resultado("Todos os sites estão funcionando!")
    else:
        nl = "\n"
        notificar_resultado(f"Cairam:{nl}{nl.join(cairam)}")


if __name__ == "__main__":
    verificar_sites()

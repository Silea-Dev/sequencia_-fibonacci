import os


class Fibonacci:
    def __init__(self):
        self._lista = [1, 2]

    def gerar_sequencia(self, distancia):
        if distancia <= 2:
            self._lista = self._lista[:distancia]
            return

        for _ in range(distancia - 2):
            conta = self._lista[-1] + self._lista[-2]
            self._lista.append(conta)

    def get_sequencia(self):
        return self._lista


def executar_programa():
    while True:
        limite_str = input(
            "Digite um inteiro positivo 'n' para gerar da sequência de tamanho 'n' | sair[ex]\n:"
        )
        if limite_str.lower() == "ex":
            print("Bye!")
            os.system("cls")
            break

        try:
            limite_int = int(limite_str)
            if limite_int < 0:
                print("[ERROR] Digite um inteiro POSITIVO, por favor!")
                continue
            if len(limite_str) > 4:
                print("[ALERT] POR SEGURANÇA LIMITEI O NÚMERO DE TERMOS POR SEQUÊNCIA!")
                continue

            gerador = Fibonacci()
            gerador.gerar_sequencia(limite_int)
            print(gerador.get_sequencia())
        except ValueError as v:
            print(f"[ERROR] Digite um INTEIRO positivo, por favor: {v}")


if __name__ == "__main__":
    executar_programa()

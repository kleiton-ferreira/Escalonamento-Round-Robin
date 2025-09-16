from process import Process
from scheduler import RoundRobinScheduler


def main():
    """
    Função principal que configura e executa a simulação
    """
    # Cria o escalonador com quantum = 2
    scheduler = RoundRobinScheduler(quantum=2)

    # Cria os processos conforme o cenário proposto
    processes = [
        Process(1, 10),  # Processo 1: 10 unidades
        Process(2, 5),  # Processo 2: 5 unidades
        Process(3, 8)  # Processo 3: 8 unidades
    ]

    # Adiciona os processos ao escalonador
    scheduler.add_processes(processes)

    # Exibe configuração inicial
    print("CONFIGURAÇÃO INICIAL:")
    print("Processos criados:")
    for process in scheduler.processes:
        print(f"  {process}")
    print()

    # Executa a simulação
    scheduler.run_simulation()


if __name__ == "__main__":
    main()
class Process:
    """
    Classe que representa um processo no sistema de escalonamento
    """

    def __init__(self, pid, total_time):
        """
        Inicializa um processo com ID e tempo total necessário
        :param pid: Identificador do processo
        :param total_time: Tempo total necessário para execução
        """
        self.pid = pid
        self.total_time = total_time
        self.remaining_time = total_time
        self.execution_blocks = []  # Lista de blocos de execução alocados

    def execute(self, quantum, time_slot):
        """
        Executa o processo por um quantum de tempo
        :param quantum: Quantum de tempo alocado
        :param time_slot: Tempo atual do sistema
        :return: Tempo realmente executado
        """
        # Verifica quanto tempo pode ser executado (mínimo entre quantum e tempo restante)
        time_executed = min(quantum, self.remaining_time)
        self.remaining_time -= time_executed

        # Registra o bloco de execução
        block_info = {
            'start_time': time_slot,
            'duration': time_executed,
            'end_time': time_slot + time_executed
        }
        self.execution_blocks.append(block_info)

        return time_executed

    def is_completed(self):
        """
        Verifica se o processo foi concluído
        :return: True se o processo foi concluído, False caso contrário
        """
        return self.remaining_time <= 0

    def __str__(self):
        """
        Representação em string do processo
        :return: String formatada com informações do processo
        """
        status = "Concluído" if self.is_completed() else f"Restante: {self.remaining_time}"
        return f"Processo P{self.pid} (Total: {self.total_time}, {status})"
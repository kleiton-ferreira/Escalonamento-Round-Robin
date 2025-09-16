from process import Process


class RoundRobinScheduler:
    """
    Classe que implementa o algoritmo de escalonamento Round Robin
    """

    def __init__(self, quantum=2):
        """
        Inicializa o escalonador com o quantum especificado
        :param quantum: Quantum de tempo para cada processo
        """
        self.quantum = quantum
        self.processes = []
        self.time_elapsed = 0
        self.execution_history = []

    def add_process(self, process):
        """
        Adiciona um processo à lista de processos
        :param process: Processo a ser adicionado
        """
        self.processes.append(process)

    def add_processes(self, processes_list):
        """
        Adiciona múltiplos processos de uma vez
        :param processes_list: Lista de processos
        """
        self.processes.extend(processes_list)

    def run_simulation(self):
        """
        Executa a simulação do escalonamento Round Robin
        """
        print("=" * 60)
        print("INICIANDO SIMULAÇÃO ROUND ROBIN")
        print("=" * 60)
        print(f"Quantum definido: {self.quantum} unidades de tempo")
        print("-" * 60)

        # Cria uma fila circular com todos os processos
        process_queue = self.processes.copy()
        current_index = 0
        block_counter = 1  # Contador de blocos de execução

        # Continua executando enquanto houver processos na fila
        while process_queue:
            # Obtém o próximo processo da fila
            current_process = process_queue[current_index]

            # Executa o processo pelo quantum
            time_executed = current_process.execute(self.quantum, self.time_elapsed)

            # Registra a execução no histórico
            execution_info = {
                'time_slot': self.time_elapsed,
                'process': current_process.pid,
                'time_executed': time_executed,
                'block_id': block_counter,
                'remaining_time': current_process.remaining_time
            }
            self.execution_history.append(execution_info)

            # Exibe informações da execução atual
            self._display_execution_step(execution_info, block_counter)

            # Atualiza o tempo decorrido
            self.time_elapsed += time_executed
            block_counter += 1

            # Verifica se o processo foi concluído
            if current_process.is_completed():
                # Remove o processo da fila
                process_queue.pop(current_index)
                # Se removemos um processo, ajustamos o índice se necessário
                if current_index >= len(process_queue):
                    current_index = 0
                continue

            # Move para o próximo processo na fila circular
            current_index = (current_index + 1) % len(process_queue)

        # Exibe o resumo final da simulação
        self._display_final_summary()

    def _display_execution_step(self, execution_info, block_id):
        """
        Exibe informações detalhadas de cada passo de execução
        :param execution_info: Dicionário com informações da execução
        :param block_id: ID do bloco de execução
        """
        print(
            f"Bloco {block_id}: Tempo {execution_info['time_slot']}-{execution_info['time_slot'] + execution_info['time_executed']}")
        print(f"  Processo P{execution_info['process']} executado por {execution_info['time_executed']} unidades")
        print(f"  Tempo restante de P{execution_info['process']}: {execution_info['remaining_time']}")
        print(f"  Próximo processo na fila...")
        print("-" * 40)

    def _display_final_summary(self):
        """
        Exibe um resumo detalhado da simulação
        """
        print("=" * 60)
        print("SIMULAÇÃO CONCLUÍDA!")
        print("=" * 60)
        print(f"Tempo total de execução: {self.time_elapsed} unidades")
        print("-" * 60)

        # Exibe detalhes de cada processo
        print("DETALHES DOS PROCESSOS:")
        for process in self.processes:
            print(f"\nProcesso P{process.pid}:")
            print(f"  Tempo total necessário: {process.total_time}")
            print(f"  Blocos de execução alocados: {len(process.execution_blocks)}")

            for i, block in enumerate(process.execution_blocks, 1):
                print(f"    Bloco {i}: Tempo {block['start_time']}-{block['end_time']} "
                      f"(Duração: {block['duration']})")

        # Exibe histórico completo de execução
        print("\n" + "=" * 60)
        print("HISTÓRICO COMPLETO DE EXECUÇÃO:")
        print("=" * 60)
        print("Bloco | Processo | Início-Fim | Duração | Restante")
        print("-" * 60)

        for i, exec_info in enumerate(self.execution_history, 1):
            end_time = exec_info['time_slot'] + exec_info['time_executed']
            print(f"{i:5d} | P{exec_info['process']:7d} | "
                  f"{exec_info['time_slot']:3d}-{end_time:3d} | "
                  f"{exec_info['time_executed']:7d} | "
                  f"{exec_info['remaining_time']:8d}")
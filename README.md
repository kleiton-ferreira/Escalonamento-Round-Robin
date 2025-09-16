# Simulador de Escalonamento Round Robin
Este projeto implementa um simulador do algoritmo de escalonamento Round Robin em Python, permitindo visualizar a execução de processos com um quantum fixo de tempo. O simulador mostra a sequência de execução dos processos, o tempo restante de cada um após cada quantum e fornece um relatório detalhado ao final da simulação.

## 🎯 Objetivo
O objetivo deste projeto é demonstrar o funcionamento do algoritmo de escalonamento Round Robin, que é amplamente utilizado em sistemas operacionais para gerenciamento de processos em ambientes de tempo compartilhado.

## ⚙️ Funcionalidades
- Simulação de Processos: Criação de processos com tempos de execução específicos
- Algoritmo Round Robin: Implementação do algoritmo com quantum configurável
- Visualização Detalhada: Exibição passo a passo da execução dos processos
- Relatório Completo: Histórico de execução com índices de blocos e tempos
- Modularidade: Código organizado em classes para fácil manutenção e extensão

## 🛠️ Tecnologias utilizadas
- Python 3.x → Linguagem principal do projeto
- Classes e POO → Para organização modular do código
- Módulos padrão Python → Não requer dependências externas

## 📂 Estrutura do projeto

📦 round-robin-simulator

 ┣ 📜 process.py         # Classe Process: gerencia os processos e seu estado
 
 ┣ 📜 scheduler.py       # Classe RoundRobinScheduler: implementa o algoritmo
 
 ┣ 📜 main.py            # Script principal para executar a simulação
 
 ┗ 📜 README.md          # Documentação do projeto

## 📋 Cenário de Simulação
O simulador é configurado com o seguinte cenário:
- Processo 1: Tempo total necessário = 10 unidades de tempo
- Processo 2: Tempo total necessário = 5 unidades de tempo
- Processo 3: Tempo total necessário = 8 unidades de tempo
- Quantum: 2 unidades de tempo

## ▶️ Como executar o projeto
Pré-requisitos
- Python 3.x instalado
- PyCharm ou outra IDE/editor de código

Execução
- Clone o repositório ou baixe os arquivos do projeto
- Abra o projeto no PyCharm
- Execute o arquivo main.py


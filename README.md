# SprintDP_IV

## Explicação das Estruturas e Algoritmos Utilizados

- **Programação Dinâmica (PD):**
  - Utilizada para modelar o consumo e reposição diária de insumos, buscando minimizar a quantidade de produto faltante ao longo de vários dias.
  - Cada estado da PD é definido pelo dia atual e pelo estoque do insumo disponível naquele dia.  
  - As decisões consistem em escolher quanto repor de insumo a cada dia, considerando os limites do estoque.
  - A função de transição determina o estoque do próximo dia com base na reposição e no consumo realizado.
  - A função objetivo acumula as faltas de insumo em cada dia, buscando uma estratégia ótima para reposição.

- **Versão Recursiva com Memorização:**
  - Implementada por meio de uma função recursiva que calcula a falta mínima para cada estado, guardando os resultados já obtidos em um dicionário para evitar cálculos repetidos.
  - Garante eficiência e evita recomputação, principalmente em cenários com muitos dias e possibilidades de reposição.

- **Versão Iterativa (Bottom-Up):**
  - Implementada por meio de uma tabela que armazena os resultados para todos estados possíveis, resolvendo o problema de trás para frente (último para o primeiro dia).
  - Essa abordagem também evita recomputações e garante que cada subproblema seja resolvido uma única vez.

- **Assert para Equivalência dos Resultados:**
  - Após a execução das duas versões, um comando `assert` compara os resultados finais, garantindo que ambas as implementações produzem o mesmo valor ótimo de falta, conforme exigido no problema.

Essas estruturas asseguram que o controle de estoque simulado seja eficiente, flexível para ajustes de parâmetros e adequado para analisar diferentes cenários de demanda e reposição de insumos.

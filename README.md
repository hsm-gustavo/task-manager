# Gerenciador de Tarefas

Um gerenciador de tarefas diárias para manter a monitoração de suas tarefas.

## Uso

Para usar o gerenciador de tarefas, basta executar o arquivo `main.py`:

```bash
$ python3 main.py
```

O programa iniciará mostrando o menu principal, onde você pode escolher entre as opções:

1. Adicionar tarefa
2. Procurar tarefa (requer nome)
3. Remover tarefa (requer índice)
4. Quantidade de tarefas
5. Listar tarefas
6. Editar tarefa (requer índice)
7. Sair do programa

### Adicionar tarefa

Ao escolher a opção 1, você será solicitado a digitar o nome da tarefa, a descrição, o prazo e a prioridade da mesma. O prazo deve ser digitado de uma das seguinte maneiras: `dd/mm/aaaa` ou `dd/mm/aa`.

### Procurar tarefa

Ao escolher a opção 2, você será solicitado a digitar o nome da tarefa que deseja procurar. O programa irá procurar pelo nome digitado na lista de tarefas e retornará a primeira tarefa que encontrar com o nome. Caso a lista esteja vazia, o índice esteja fora do alcance ou não encontre nenhuma tarefa com o nome digitado, o programa retornará uma mensagem de erro.

### Remover tarefa

Ao escolher a opção 3, você será solicitado a digitar o índice da tarefa que deseja remover. O programa irá procurar pelo índice digitado na lista de tarefas e removerá a tarefa que encontrar com o índice. O primeiro elemento da lista tem índice 0, o segundo tem índice 1 e assim por diante. Caso a lista esteja vazia, o índice esteja fora do alcance ou não encontre nenhuma tarefa com o índice digitado, o programa retornará uma mensagem de erro.

### Quantidade de tarefas

Ao escolher a opção 4, o programa irá retornar a quantidade de tarefas que estão na lista.

### Listar tarefas

Ao escolher a opção 5, o programa irá listar todas as tarefas que estão na lista.

### Editar tarefa

Ao escolher a opção 6, você será solicitado a digitar o índice da tarefa que deseja editar. O programa irá procurar pelo índice digitado na lista de tarefas e então vai perguntar quais são as novas informações da tarefa (nome, descrição, prazo e prioridade). Qualquer campo vazio será ignorado, mantendo as mesmas informações antes da edição. Caso a lista esteja vazia, o índice esteja fora do alcance ou não encontre nenhuma tarefa com o índice digitado, o programa retornará uma mensagem de erro.

### Sair do programa

Ao escolher a opção 7, o programa irá encerrar.
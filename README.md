
# TesteCodigo  
## Verificador de Fibonacci  
Neste programa a solução utilizada foi um loop While True tendo as quebras de loop dentro de condicionais pois existem 3 cenários possíveis:  
1. Caso o número fornecido pelo usuário seja igual o número da sequência de fibonacci calculado no loop atual eu desejo que o loop se quebre e retorne uma mensagem informando que o número inserido pertence a sequência.  
2. Caso o número fornecido seja maior que o número da sequência calculado atualmente eu desejo que o loop continue pois ainda não sabemos se o número do usuário pertence ou não a sequência de fibonacci.  
3. Caso o número fornecido seja menor que o número atual da sequência de fibonacci eu desejo que o loop se quebre com a mensagem informando que o número do usuário não pertence a sequência de fibonacci.  
  
E você pode estar se perguntando: mas por que não checar a terceira condição antes da execução do loop while?  
A resposta é: nesse caso o programa não funcionaria caso o usuário fosse inserir um número negativo, sendo assim, eu teria que adicionar mais uma condicional ao programa além da condicional presente no início de cada loop while.  
  
## Verificador de letra A  
Neste programa a solução encontrada foi: pegar a string fornecida pelo usuário e transformar todas as letras em minúsculas para que seja necessário apenas uma checagem. Após isso eu transformo a string do usuário em uma lista sendo que cada caractere da string se torna um item da lista. E por fim eu apenas precisei utilizar o médodo count() do python para contar quantos itens "a" existem nesta lista para posteriormente mostrar o resultado ao usuário.
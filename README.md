#TCCEEAPUNIRIO---ROTEIRIZACAO
Esse é o meu TCC onde eu uso o algoritmo de Clarke & Wright para encontrar a melhor a melhor rota que possa levar e trazer os servidores da UNIRIO.

A trilha que pretendo seguir é a seguinte:

- Descobrir as distâncias entre os municípios do estado do Rio de Janeiro e montar um arquivo csv com elas.
- Aplicar o algoritmo de Clarke&Wright nesta pequena base de dados.
- Analisar resultados e propor cenários.
- Comparar cenários.


DIA 2 - Finalmente acertando no Clark&Wright

Reestruturei a minha implementação do algoritmo de Clarke&Wright, agora o algoritmo se comporta bem melhor. Porém, ainda vejo que ele se comporta melhor quando temos pontos mais próximos do nó central.

Consegui algumas rotas interessantes. Utilizando apenas pontos que estão a menos de 1:30 hora do nó de origem, consegui formar uma rota que GASTA R$130,00 reais de combustível e tem um capital para investimento de R$516,00. Na avaliação mais pessimista, economizo R$ 5200,00 por mês e R$6402,00 reais. Essa rota passa pelos seguintes municipios. 

- DUQUE DE CAXIAS
- SAO JOAO DE MERITI
- BELFORD ROXO
- MESQUITA
- NILOPOLIS
- NOVA IGUACU

Outra rota que aparece frequêntemente é mandar um ônibus apenas para Niterói, isso geraria uma receita de R$ 11264,00 na estimativa pessimista e R$12474,00.

Admitindo que possamos ter passageiros em pé, a melhor rota seria a que passa por Niterói e São Gonçalo, que transportaria 53 pessoas ( 5 pessoas em pé ) e teria um capital para investir de quase 1000 reais diários. 





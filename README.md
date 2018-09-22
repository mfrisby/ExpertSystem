# ExpertSystem

Truth table query solver

https://en.wikipedia.org/wiki/Truth_table

![alt text](https://introcs.cs.princeton.edu/java/71boolean/images/truth-table.png)

## Chainage avant

### Algorithme

- BF, une base de faits;
- BR, une base de règles (conclusion positives);
- Fait, le fait que l'on cherche à établir,
- Recherche de la déduction possible de Fait

TANT QUE (F ∉ BF) ET (∃ R ∈ BR, applicable(R)) FAIRE
 
 choisir une règle applicable R (par metarègles, heuristiques, ...)

BR = BR - R (désactivation de R)

BF = BF union concl(R) (déclenchement de la règle R, ajout de sa conclusion)

FIN TANT QUE

SI F ∈ BF ALORS F est établi
SINON F n'est pas établi FIN

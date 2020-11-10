
## Ant Colony Algorithm

- pheromones:     when ants travel they will leave some pheromones behind, the strenght of their pheromones will be calculated.
- vaporisation:   the pheromones will evaporate at a constant rate over time
- multiple ants do the this.
    - the pheromones increase the probability of the ants following that path.
- then the final ant takes the one with the highest pheromones.

Solution:
- How it decides on which square to go is by:
    - score of going to the square: pheremone** alpha(weight on pheremone) * (1/distance) ** beta ()
    - probability of going to that square is = theCity'sScore/sumOfAllAVAILABLECitiesscores
    - then move to that square
    - do until there is a successful ant.
    - multiply the pheremone matrix by decay rate when entering the next generation


- maybe start the first one pseudo random:
    - only go right and down
    - or just make it very random
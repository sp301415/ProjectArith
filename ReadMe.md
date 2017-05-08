# Solving Modified Blotto Game with Genetic Algorithm

This is a document with python-style pseudocode to explain our algorithm.

## Notation
- Total battlefield number: `BATTLEFIELD_TOTAL`
- Total troop number: `TROOP_TOTAL`
- Gene pool size: `GENE_POOL_SIZE`
- Gene pool: `gene_pool`, 2D array with size `GENE_POOL_SIZE`*`BATTLEFIELD_TOTAL`
- Troop profile: `troop_profile`,  2D array with size 2*`BATTLEFIELD_TOTAL`
- Value profile: `value_profile`,  2D array with size 2*`BATTLEFIELD_TOTAL`
- Player: `player`, either `0` or `1`
- Opponent: `opponent`, equals to `player ^ 1`



      while not end_condition :
        for i from 0 to int(GENE_POOL_SIZE * percentage):
          set gene_pool[i] = reduce_improve(troop_profile, player)
        for i from int(GENE_POOL_SIZE * percentage) to GENE_POOL_SIZE:
          set gene_pool[i] = randomly partition TROOP_TOTAL to BATTLEFIELD_TOTAL
        gene_selection(troop_profile, gene_pool, value_profile, player)
        change player

      return troopProfile


## Reduce_Improve

This step makes new genes from existing troop profile. 
 

    def reduce_improve(troop_profile, player)
    
      initalize leftover = 0
      
      for i from 0 to BATTLEFIELD_TOTAL:
        if troop_profile[player][i] > troop_profile[opponent][i] + 1 then:
          add troop_profile[player][i] - troop_profile[opponent][i] -1 to leftover
          set troop_profile[player][i] = troop_pr
## Main

    def main():ofile[opponent][i] + 1
      
      for i from 0 to leftover:
        add 1 to troop_profile[player][random int from 0 to BATTLEFIELD_TOTAL]
        
      return troop_profile


## Greedy_Mode

This step scores the difference of score between gene and initial troop profile.


    def greedy_mode(troop_profile_init, troop_profile, value_profile, player):
      
      initalize troop_profile_temp[player] = troop_profile[player]
      initalize troop_profile_temp[opponent] = troop_profile_init[opponent]
      set score = game(troop_profile_temp, valueProfile) - game(troop_profile_init, valueProfile) + 0.25
    
      return score

  

## Generous_Mode

This step exists to find PNE more easily; it is a special case. If there are indifferent values among player’s battlefield, to deploy troops more on battlefields that opponent’s value are low gets more score.


    def generous_mode(troop_profile_player, value_profile):
     
      for same value i in value_profile[player]:
        for j as index of i in value_profile[player]:
          append (troop_profile_player[j] / troop_profile_same_total)
            + (valueProfile[opponent][j] / value_profile_same_total) to gene_score
        add pow(10, stdev(gene_score)) to score
        clear gene_score
        
      return score      


## Gene_Selection

This selects gene based on generous and greedy mode.


    def gene_selection(troop_profile, gene_pool, value_profile, player):
      
      for i from 0 to GENE_POOL_SIZE
        append (greedy_mode(troop_profile, gene_pool[i], value_profile, player) /
          generous_mode(gene_pool[i]], value_profile) to score
          
      troop_profile[player] = randomly choose gene_pool with weight = score
      
      return troopProfile  



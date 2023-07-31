def outgoing_dmg(cr = 5, cd = 50, skill_multiplier=0, extra_multiplier=0, scaling_attribute=0, extra_dmg=0,
                 dmg_multiplier=0, def_ignore=0, res_multiplier=100,
                 dmg_taken_multiplier=100, universal_dmg_reduction_multiplier=90,
                 weaken_multiplier=100):
    final_dmg = (skill_multiplier / 100 + extra_multiplier) * scaling_attribute + extra_dmg
    final_dmg *= 1 + dmg_multiplier / 100    
    defense = 1000 * (1 - def_ignore / 100)
    final_dmg *= 1 - (defense / (defense + 200 + 10 * 80))   
    final_dmg *= res_multiplier / 100    
    final_dmg *= dmg_taken_multiplier / 100
    final_dmg *= universal_dmg_reduction_multiplier / 100 
    final_dmg *= weaken_multiplier / 100
    final_dmg *= (1 + (min(cr, 100) / 100) * (cd / 100))
    return final_dmg

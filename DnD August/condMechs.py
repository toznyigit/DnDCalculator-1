def checkCondition(target):
    for condition in target.condition:
        if condition == "RC":
            for condition in target.condition:
                if "curse" in target.condition[condition]:  target.condition.pop(condition)
        if condition == "Heal":
            if target.condition["Heal"][0] > 0:
                target.condition["Heal"][0]-=1
                target.currentHealth = min(target.maxHealth,target.currentHealth+target.condition["Heal"][1])
        if condition == "Damage":
            if target.condition["Damage"][0] > 0:
                target.condition["Damage"][0]-=1
                target.currentHealth -= target.condition["Damage"][1]

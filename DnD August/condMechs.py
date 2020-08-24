def checkCondition(target):
    for condition in target.condition:
        if condition == "Heal":
            if target.condition["Heal"][0] > 0:
                target.condition["Heal"][0]-=1
                target.currentHealth = min(target.maxHealth,target.currentHealth+target.condition["Heal"][1])

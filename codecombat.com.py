def seekAndDestroy():
    target = hero.findNearestEnemy()
    if target:
        if hero.distanceTo(target)>10 and hero.isReady("jump"):
            hero.jumpTo(target)
        if hero.isReady("cleave") and goodCleave():
            hero.cleave(target)
        else:
            hero.attack(target)

def goodCleave():
    goodTime = 3
    cleaveRange = 10
    countEnemyNear = 0
    targets = hero.findEnemies()
    
    for i in targets:
        if hero.distanceTo(i) <= cleaveRange:
            countEnemyNear +=1
    if countEnemyNear > goodTime:
        return True
    return False
    

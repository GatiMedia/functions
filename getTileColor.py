def getTileColor(nodes):
    nodes = nuke.selectedNodes()
    if nodes:
        nodeNames = []
        nodeColors = []
        nodeInfo = []
        for n in nodes:
            nClass = n.Class()
            tileColorNew = n['tile_color'].value()
            if tileColorNew == 0:
                tileColorNew = None
                ### cache ###
                classCache = [i.capitalize() for i in nuke.toNode('preferences')['NodeColourClassCache'].value().split()]
                for c in classCache:
                    if c in nClass:
                        tileColorNew = nuke.toNode('preferences')['NodeColourCacheColor'].value()
                ### deep ###
                classDeep = [i.capitalize() for i in nuke.toNode('preferences')['NodeColourClassDeep'].value().split()]
                for c in classDeep:
                    if c in nClass:
                        tileColorNew = nuke.toNode('preferences')['NodeColourDeepColor'].value()
                ### 01-14 ###
                for num in range(14):
                    className = 'NodeColourClass'+str(num+1).zfill(2)
                    classColor = 'NodeColour'+str(num+1).zfill(2)+'Color'
                    for c in [i.capitalize() for i in nuke.toNode('preferences')[className].value().split()]:
                        if c in nClass:
                            tileColorNew = nuke.toNode('preferences')[classColor].value()
                    for c in [i for i in nuke.toNode('preferences')[className].value().split()]:
                        if c in nClass:
                            tileColorNew = nuke.toNode('preferences')[classColor].value()
                if tileColorNew == None:
                    tileColorNew = nuke.toNode('preferences')['NodeColour14Color'].value()
            nodeNames.append(n.name())
            nodeColors.append(tileColorNew)
        for name, color in zip(nodeNames, nodeColors):
            nodeInfo.append(str(name)+" : "+str(color))
    else:
        nuke.message('<font color=orange><b>\n\nSelect some nodes first!\n\n')
    return(nodeInfo)

print(getTileColor(nuke.selectedNodes()))

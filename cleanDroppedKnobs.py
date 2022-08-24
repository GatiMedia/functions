def cleanDroppedKnobs():
    for node in nuke.allNodes():
        for knob in node.knobs():
            if 'panelDropped' in knob:
                try:
                    node.removeKnob(node[knob])
                except:
                    pass
                    
utilitiesMenu.addCommand('Clean Dropped Knobs', 'cleanDroppedKnobs()', index=5)

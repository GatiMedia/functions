def cleanDroppedKnobs():
    for node in nuke.allNodes(recurseGroups=True):
        for knob in node.knobs():
            if 'panelDropped' in knob:
                try:
                    node.removeKnob(node[knob])
                except:
                    pass

# Add to custom menu
utilitiesMenu.addCommand('Clean Dropped Knobs', 'cleanDroppedKnobs()', index=5)

# Apply on Script Load
nuke.addOnScriptLoad(cleanDroppedKnobs)

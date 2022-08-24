def closePanels():
    for node in nuke.allNodes():
        node.hideControlPanel()

nuke.menu('Nodes').addCommand('close', 'closePanels()' , 'shift+d')

def closePanels():
    for node in nuke.allNodes(recurseGroups=True):
        node.hideControlPanel()

utilitiesMenu.addCommand('Close Panels', 'closePanels()' , 'shift+d', index=1 )

def closePanels():
    for node in nuke.allNodes():
        node.hideControlPanel()

utilitiesMenu.addCommand('Close Panels', 'closePanels()' , 'shift+d', index=1 )

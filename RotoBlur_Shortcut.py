import nuke

def RotoBlur_Shortcut():
    y_offset = 60
    r = nuke.createNode('Roto', 'output alpha')
    y = int(r.ypos() + y_offset)
    b = nuke.nodes.Blur()
    b['size'].setValue(2)
    b['label'].setValue('Size: [value size]')
    b['xpos'].setValue(r.xpos())
    b['ypos'].setValue(y)
    b.setInput(0,r)
    b.hideControlPanel()
    
nuke.menu('Nodes').addMenu('Draw').addCommand('Create Roto and Blur node', 'RotoBlur_Shortcut()', shortcut='o', icon='Roto.png')

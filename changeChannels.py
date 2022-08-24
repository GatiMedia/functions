def changeChannels():
    sel_nodes = nuke.selectedNodes()
    if len(sel_nodes) > 0:
        ok_channels = ['all', 'none', 'rgba', 'rgb', 'alpha']

        for sel_node in sel_nodes:
            
            # setting up for channels knob
            if sel_node.knob('channels'):
                if not sel_node['channels'].value() == "alpha" and sel_node.knob('channels').value() in ok_channels:
                    channel_index = ok_channels.index(sel_node['channels'].value())
                    sel_node['channels'].setValue(ok_channels[channel_index + 1])
                else:
                    sel_node['channels'].setValue('all')

            # setting up for output knob
            if sel_node.knob('output'):
                try:
                    if not sel_node['output'].value() == "alpha" and sel_node.knob('output').value() in ok_channels:
                        channel_index = ok_channels.index(sel_node['output'].value())
                        sel_node['output'].setValue(ok_channels[channel_index + 1])
                    else:
                        sel_node['output'].setValue('all')
                except:
                    pass

            # setting up for retimedChannels knob
            if sel_node.knob('retimedChannels'):
                if not sel_node['retimedChannels'].value() == "alpha" and sel_node.knob('retimedChannels').value() in ok_channels:
                    channel_index = ok_channels.index(sel_node['retimedChannels'].value())
                    sel_node['retimedChannels'].setValue(ok_channels[channel_index + 1])
                else:
                    sel_node['retimedChannels'].setValue('all')
    else:
        nuke.message('<center><b>Select a node/nodes first.\nThis shortcut iterates through the following channels:</b>\n<i>all, none, rgba, rgb, alpha</i></center>')

utilitiesMenu.addCommand('Change Channels', 'changeChannels()' , 'shift+a')

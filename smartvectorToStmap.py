def smartvectorToStmap():

    selCheck = nuke.selectedNodes('Read')

    if selCheck:
        selSV = nuke.selectedNode()
        # Getting the n-th value from the user
        frameNumber = nuke.getInput(
            """<center><b><font color=orange>\nEvery n-th frame to create\n STMap & Write node from</b>\n\n(10 is a recommanded value,\nchange only if necessary)\n""",
            '10')

        # Checking if the value is integer
        if frameNumber.isdigit():

            # Getting the values from the selected Read node
            sv_x = selSV['xpos'].value()
            sv_y = selSV['ypos'].value()
            sv_first = selSV['first'].value()
            sv_last = selSV['last'].value()
            sv_range = range(selSV['last'].value() - sv_first)
            selSV.setSelected(False)

            # Creating the first setup
            dot = nuke.nodes.Dot()
            dot.setInput(0, selSV)
            dot['xpos'].setValue(sv_x + 35)
            dotx = dot['xpos'].value()
            dot['ypos'].setValue(sv_y + 200)
            doty = dot['ypos'].value()
            dot.setSelected(True)

            # Creating the first VectorDistort using the first frame as a reference
            vecDist1 = nuke.createNode('VectorDistort')
            vecDist1.setInput(0, dot)
            vecDist1['reference_frame'].setValue(sv_first)
            vecDist1['output_mode'].setValue('st-map')
            vecDist1['label'].setValue("""Ref fr.: [value reference_frame]\nOutput: [value output_mode]""")
            vecDist1['xpos'].setValue(sv_x)
            vecDist1['ypos'].setValue(doty + 200)
            vecDistY = vecDist1['ypos'].value()
            dot.setSelected(False)
            vecDist1.setSelected(True)

            # Create GBKWrite

            writeNode['channel'].setValue("rgb")
            writeNode['fecompname'].setValue("stmap_fr" + str(sv_first))
            
            dot.setSelected(True)
            for i in sv_range[0::int(frameNumber)]:
                if i > 2:
                    try:
                        vecDist2 = nuke.createNode('VectorDistort')
                        vecDist2.setInput(0, dot)
                        vecDist2['reference_frame'].setValue(sv_first + i)
                        vecDist2['output_mode'].setValue('st-map')
                        vecDist1['label'].setValue("""Ref fr.: [value reference_frame]\nOutput: [value output_mode]""")
                        vecDist2['ypos'].setValue(vecDistY)
                        vecDist2_x = sv_x
                        vecDist2['xpos'].setValue(vecDist2_x + (i * 33))
                        vecDist2_x = vecDist2['xpos'].value()
                        vecDist2.setSelected(True)

                        # Create GBKWrite #

                        writeNode['channel'].setValue("rgb")
                        writeNode['fecompname'].setValue("stmap_fr" + str(sv_first))

                    except Exception:
                        pass
        else:
            nuke.message("""<center><b><font color=orange>Given value need to be an integer!""")
    else:
        nuke.message("""<center><b><font color=orange>Select a single node first\ncontaining a smartvector layer!""")

        
bopMenu.addCommand('SmartVector to STMap', 'smartvectorToStmap()', index=0 )

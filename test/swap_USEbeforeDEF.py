from x3dkw import *
import copy

USEdict = {}
DEFdict = {}
USEbeforeDEFdict = {}

#shapeclass = globals()['Shape']
#print (shapeclass())

def swap_USEbeforeDEF(node=None, parent=None):
    USE = getattr(node,'USE', None)
    if USE:
        if USE not in USEdict:
            USEdict[USE] = [{'node': node, 'parent': parent}]
        else:
            USEdict[USE].append({'node': node, 'parent': parent})
        print(node.NAME(), 'USE: ' + USE + str(len(USEdict[USE])))
        if USE not in DEFdict:
            print ("USE " + USE + " occurred before DEF")
            USEbeforeDEFdict[USE] = USEdict[USE] # record in dict
    DEF = getattr(node,'DEF', None)
    if DEF:
        if DEF not in DEFdict: DEFdict[DEF] = [node]
        else:
            DEFdict[DEF].append(node)
            print ("DEF " + DEF + " already defined")
            if DEF not in USEbeforeDEFdict:
                print ("creating a new USE node of the same type")
                insertDEFIndex = parent.children.index(node)
                nodeClass = node.NAME()
                node = globals()[nodeClass](USE=DEF) # a bit hackish
                parent.children[insertDEFIndex] = node
                # use node.FIELD_DEFINITIONS to reset all fields to defaults
        print(node.NAME(),'DEF: ' + DEF + str(len(DEFdict[DEF])))
        if DEF in USEbeforeDEFdict:
            USEnode = USEbeforeDEFdict[DEF][0] # replace first USE node only
            USEcopy = copy.deepcopy(USEnode['node'])
            if len(DEFdict[DEF]) == 1: # only for first DEF node
                print("replacing earlier USE with this DEF")
                insertUSEIndex = USEnode['parent'].children.index(USEnode['node'])
                USEnode['parent'].children[insertUSEIndex] = node
            # DEF to USE
            print("replacing DEF with copy of earlier USE")
            insertDEFIndex = parent.children.index(node)
            parent.children[insertDEFIndex] = USEcopy
    for each in node.children:
        swap_USEbeforeDEF(node=each, parent=node)

x3d = X3D()
scene = Scene()
x3d.Scene = scene
grpa = Group(DEF='A')
grpb = Group(DEF='B')
scene.children.append(grpa)
scene.children.append(grpb)
trans = Transform(DEF='C')
trans2 = Transform(USE='C')
grpb.children.append(trans)
grpa.children.append(trans2)
grpb.children.append(trans)
print (x3d.XML())
swap_USEbeforeDEF(node=scene)
print (x3d.XML())

USEdict = {}
DEFdict = {}
USEbeforeDEFdict = {}

x3d = X3D()
scene = Scene()
x3d.Scene = scene
grpa = Group(DEF='A')
grpb = Group(DEF='B')
scene.children.append(grpa)
scene.children.append(grpb)
trans = Transform(DEF='C')
grpd = Group(DEF='D')
trans.children.append(grpd)
grpb.children.append(trans)
grpa.children.append(trans)

print (x3d.XML())
swap_USEbeforeDEF(node=scene)
print (x3d.XML())


#blob = x3d.XML()
#fp = open("dump_case2.x3d","w+")
#fp.write(blob)
#fp.close()

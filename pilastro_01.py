"""
    file: pilastro_01.py
    
    Descrizione:    Pilastro in ca
                     - 4 barre diritte
                     - staffe ogni 25 cm 
    
"""


import FreeCAD, Draft, Arch
from ColumnReinforcement import SingleTie

FreeCAD.ActiveDocument.Label='pilastro_01'

App.setLogLevel('pilastro_01', 'Trace')
#App.setLogLevel('pilastro_01', 'Log')
#App.setLogLevel('pilastro_01', 'Message')
log=App.Logger('pilastro_01')


objects=App.ActiveDocument.Objects
for object in objects:
    App.ActiveDocument.removeObject(object.Name)


App.closeDocument("pilastro_01")
App.setActiveDocument("")
App.ActiveDocument=None
Gui.ActiveDocument=None


App.newDocument("pilastro_01")
App.setActiveDocument("pilastro_01")


# It doesn't work if the structure is not based on a face
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

Rect = Draft.makeRectangle(400, 400)
Structure = Arch.makeStructure(Rect, height=4000)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

## For Straight Rebars
#RebarGroup = SingleTie.makeSingleTieFourRebars(
#    l_cover_of_tie=40,        
#    r_cover_of_tie=40,
#    t_cover_of_tie=40,
#    b_cover_of_tie=40,
#    offset_of_tie=100,
#    bent_angle=135,
#    extension_factor=2,
#    dia_of_tie=8,
#    number_spacing_check=True,
#    number_spacing_value=10,
#    dia_of_rebars=16,
#    t_offset_of_rebars=40,
#    b_offset_of_rebars=40,
#    rebar_type="StraightRebar",
#    hook_orientation="Top Inside",
#    hook_extend_along="x-axis",
#    l_rebar_rounding=None,
#    hook_extension=None,
#    structure=Structure,
#    facename="Face6",
#).rebar_group


Gui.SendMsgToActiveView("ViewFit")                  # visualizza l'intero elemento
Gui.activeDocument().activeView().viewIsometric()   # visualizazione isometrica


from FreeCAD import Console

import FreeCAD as App
import Arch
import ArchPrecast

#App.closeDocument("pilastro")
App.setActiveDocument("")
App.ActiveDocument=None
Gui.ActiveDocument=None


App.newDocument("pilastro")
App.setActiveDocument("pilastro")

Console.PrintLog('pilastro.py')

# pilastro
lunghezza=400.0     # lunghezza pilastro
larghezza=400.0     # larghezza pilastro
altezza=5000.0      # altezza pilastro


def makePilastro():
    """ Crea pilastro """
    pilastro = ArchPrecast.makePrecast(slabtype="Champagne",
                                       chamfer=0.0,
                                       dentlength=4e+16,
                                       dentwidth=0.0,
                                       dentheight=4e+16,
                                       base=0.0,
                                       holenumber=0,
                                       holemajor=0.0,
                                       holeminor=0.0,
                                       holespacing=0.0,
                                       groovenumber=0,
                                       groovedepth=50.0,
                                       grooveheight=50.0,
                                       groovespacing=50.0,
                                       risernumber=0,
                                       downlength=0.0,
                                       riser=0.0,
                                       tread=0.0,
                                       dents=[],
                                       precasttype="Pillar",
                                       length=500.0,
                                       width=500.0,
                                       height=5000.0,)
    pilastro.Placement.Base = FreeCAD.Vector(0, 0, 0)
    pilastro.Placement.Rotation = pilastro.Placement.Rotation.multiply(FreeCAD.DraftWorkingPlane.getRotation().Rotation)
    Draft.autogroup(pilastro)    
    return pilastro

    
pilastro=makePilastro()
# visualizzazione
Gui.SendMsgToActiveView("ViewFit")                  # visualizza l'intero pilastro
Gui.activeDocument().activeView().viewIsometric()   # visualizazione isometrica
    


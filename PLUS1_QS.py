# -*- coding: utf-8 -*-
"""
*******************************************************************************
                                    FMS 1
    
    PYTHON SCRIPT TO COMPUTE CURRENT LOADS ON SUBMERGED HORIZONTAL CYLINDER

        FILL THE MISSING SCRIPT BY REPLACING #_______________________

*******************************************************************************
                                  DESCRIPTION

Which Python Concepts are used?
    -> Reading Input from Console
    -> Import and use the module "Math"
    -> Perform Simple Mathematical operations
    -> Print The output to a file

Why is this Script usefull ?
    -> To compute Hydrodynamic Current Loads on a Submerged Horizontal Cylinder

What are the assummptions ?
    -> Clinder is ...   
                > Slender 
                > Completely Submerged 
                > Horizontally Positioned
                > Fixed at a depth

    -> Current is ...
                > Steady Uniform    

What are we actually going to calculate ?
    -> Drag Force Per unit legth of cylinder
    -> Drag Load on Cylinder 

How is this Script going to compute Forces?
    -> By Application of Morrision's Equations
        
    Expression for Drag Load :
        
        FdL = (1/2)*(RHO)*(Cd)*(D)*Vc*Vc 
        
            FdL = Drag force per unit length
            RHO = Desnity of water
            Cd  = Drag Coefficient 
            D   = Diameter of Cylinder
            Vc  = Current Speed
        
        Fd = FdL * L
            
            Fd = Total Drag Force on the cylinder
            L  = Length of Cylinder
            
*******************************************************************************
                            THE SCRIPT STARTS HERE

           FILL THE MISSING SCRIPT BY REPLACING #_______________________

*******************************************************************************
"""

''' ---------------------------------------------------------------------------
Import Required Modules 
----------------------------------------------------------------------------'''
import math


''' ---------------------------------------------------------------------------
Read the Required Inputs 
--------------------------------------------------------------------------- '''

print("Enter the Following Inputs")

''' Fluid Properties '''
# Read Density of water
INP=input('Density   =')
RHO=float(INP)

''' Cylinder Geometry & Position '''
# Diameter of Cylinder
#_______________________________________________    Fill at this Line ***
#_______________________________________________    Fill at this Line ***
# Length of Cylinder
#_______________________________________________    Fill at this Line ***
#_______________________________________________    Fill at this Line ***

''' Cylinder Hydrodynamic Coefficients '''
# Drag Coefficient 
#_______________________________________________    Fill at this Line ***
#_______________________________________________    Fill at this Line ***

''' Current Data '''
# Current Speed
#_______________________________________________    Fill at this Line ***
#_______________________________________________    Fill at this Line ***


''' ---------------------------------------------------------------------------
 Compute Drag Force
 
Hint : Implement Morrision Equaiton for Drag Load
        FdL = (1/2)*(RHO)*(Cd)*(D)*Vc*Vc  
        Fd  = FdL * L
----------------------------------------------------------------------------'''

# Drag Load per unit length
#_______________________________________________    Fill at this Line ***


# Total Drag Load
#_______________________________________________    Fill at this Line ***


''' ---------------------------------------------------------------------------
Printing the Given Data and Computed Data


----------------------------------------------------------------------------'''

print()
print("Given Input Data:\n")
print("Density     =%10.5E"%(RHO))
print("Diameter    =%10.5E"%(#_________))           Fill at this Line ***
print("Length      =%10.5E"%(#_________))           Fill at this Line ***
print("Cd          =%10.5E"%(#_________))           Fill at this Line ***
print("Vc          =%10.5E"%(#_________))           Fill at this Line ***
print("\n\nComputed Values:\n")
print("Drag force per unit length       = %10.5E"%(#_________))     Fill at this Line ***
print("Total Drag Force on the Cylinder = %10.5E"%(#_________))     Fill at this Line ***
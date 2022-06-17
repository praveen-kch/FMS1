# -*- coding: utf-8 -*-
"""
*******************************************************************************
                                    FMS 1
    
    PYTHON SCRIPT TO COMPUTE CURRENT LOADS ON SUBMERGED HORIZONTAL CYLINDER

        Replaced #_______________________ with Appropriate Script
        
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
    -> Its a Slender Cylinder 
    -> Completely Submerged 
    -> Horizontally Positioned
    -> Fixed at a depth
    -> Steady Uniform Current    

What are we actually going to calculate ?
    -> Drag Force Per unit legth
    -> Drag Load on Cylinder 

How is this Script going to compute Forces?
    -> By Application of Morrision's Equations - Drag Componet only
        
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

            Replaced #_______________________ with Appropriate Script

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
INP=input('Diameter  =')
D=float(INP)
# Length of Cylinder
INP=input('Length    =')
L=float(INP)


''' Cylinder Hydrodynamic Coefficients '''
# Drag Coefficient 
INP=input('Cd        =')
Cd=float(INP)

''' Current Data '''
# Current Speed
INP=input('Vc        =')
Vc=float(INP)

''' ---------------------------------------------------------------------------
 Compute Drag Force
 
Hint : Implement Morrision Equaiton for Drag Load
        FdL = (1/2)*(RHO)*(Cd)*(D)*Vc*Vc  
        Fd  = FdL * L
----------------------------------------------------------------------------'''

# Drag Load per unit length
FdL=0.5*RHO*Cd*D*Vc**2


# Total Drag Load
Fd = FdL*L


''' ---------------------------------------------------------------------------
Printing the Given Data and Computed Data 
----------------------------------------------------------------------------'''

print()
print("Given Input Data:\n")
print("Density     =%10.5E"%(RHO))
print("Diameter    =%10.5E"%(D))
print("Length      =%10.5E"%(L))
print("Cd          =%10.5E"%(Cd))
print("Vc          =%10.5E"%(Vc))
print("\n\nComputed Values:\n")
print("Drag force per unit length       = %10.5E"%(FdL))
print("Total Drag Force on the Cylinder = %10.5E"%(Fd))
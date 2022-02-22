# Calculate d-band center & width

A python script to calculate the d-band center and width from Densities of States (DOS).

## Table of Contents
* [Introduction](#introduction)
* [General Info](#general-info)
* [Technologies](#technologies)
* [Launch](#launch)
* [Example of Use](#example-of-use)

### Introduction

Densities of States plots offer valuable electronic information about materials. Often for transition metal-based systems, the agglomeration of d-orbitals or states (or collectively called the d-band) can be evaluated to provide insights into reactivity and structure - property relationships as suggested by Norskov et al:

* Nørskov, J. K.; Abild-Pedersen, F.; Studt, F.; Bligaard, T. Density Functional Theory in Surface Chemistry and Catalysis. Proceedings of the National Academy of Sciences of the United States of America. National Academy of Sciences 2011, 937–943.

With the Fermi energy, certain metrics can be calculated such as the d-band centroid, d-band center, and d-band width as described and demonstrated here:

* Holme, T.; Zhou, Y.; Pasquarelli, R.; O'Hayre, R. First principles study of doped carbon
supports for enhanced platinum catalysts. Physical Chemistry Chemical Physics 2010,
12, 9461-9468.
* Vojvodic, A.; Nørskov, J. K.; Abild-Pedersen, F. Electronic structure effects in
transition metal surface chemistry. Topics in Catalysis 2014, 57, 25-32.
* Inoglu, N.; Kitchin, J. R. Simple model explaining and predicting coverage-dependent
atomic adsorption energies on transition metal surfaces. Physical Review B - Condensed
Matter and Materials Physics 2010, 82, 045414.

### General Info

The script takes a provided DOS file (consisting of energy states against densities of states with dos.dat provided as an example file) and an inputted Fermi energy to calculate the coresspnding d-band centroid, d-band center, and d-band width.  

### Technologies
* Python 3

### Launch

```
$ python d_band.py
```

### Example of Use
The script will first ask for a Fermi energy input:
```
Fermi energy (units are defined by input file):
```
The script will then ask for a file input:
```
File of DOS:
```
The script will then out the values as follows:
```
e_f:
E_d: 
e_d: 
e_w: 
```
Where e_f is the Fermi energy, E_d is the d-band centroid, e_d is the d-band center, and e_w is the d-band width.



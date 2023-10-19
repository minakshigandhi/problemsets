#!/usr/bin/env python3

taxa = ('sapiens, erectus, neanderthalensis')

print(taxa)

print(type(taxa))

print(taxa[1])

taxa.split(',')

species = taxa.split(',')

print(species) #prints the string split as list

print(species[1]) #prints index posiiton 1 = erectus

print(type(species)) #prints type list

print(sorted(species, key=None, reverse=False)) #sorts the list alphabetically

sorted(species)
print(species)


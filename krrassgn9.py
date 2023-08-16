#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:





# In[ ]:





# In[7]:


def getKB(filename):
    # A KB is a set of ABox, TBox, RBox, Objects
    
    import xml.etree.ElementTree as ET
    # import TaxonomyBuilder as Builder
    tree=ET.parse(filename)
    root = tree.getroot()
    
    KB = Builder.build(root)
    return KB
    


# In[ ]:


def getinstance(KB, C):
    
    
    # KB is Knowledge Base and C is a concept description.
    # A new fact in KB using C and named individual obj and be generated as InstanceOf(C, obj) or NotInstanceOf(C, obj)
    
    # Implicit assumption: importing NotInstanceOf and Tableu from Assignment 8 and 7 respectively.
    # from util import NotInstanceOf
    # import Tableu
    cobj = []
    for obj in KB.Objects:
        if Tableu.unsat(KB, NotInstanceOf(C, obj)):##
            cobj.append(obj)
    return cobj
        
    
if __name__ == '__main__':
    concept_name = input('Enter concept name:')
    
    
    KB = getKB('hierarchy.xml')
    concept = None
    for c in KB.ABox:
        if c.name == concept_name:
            concept = c
            break
    if(concept_name == 'Nothing'):
        print('No instance found')
        with open(f'{concept_name}>.individuals.txt', 'w') as f:
            pass
    elif(concept_name == 'Thing'):
        print('Following instances were found:')
        for inst in KB.Objects:
            print(inst)
        with open(f'{concept_name}>.individuals.txt', 'w') as f:
            for inst in KB.Objects:
                f.write(inst)
                f.write('\n')
    elif(concept is None):
        print('Concept not found')
        exit()
        
    
    instances = getinstance(KB, concept)
    if(len(instances) == 0):
        print('No instances found')
        with open(f'{concept_name}>.individuals.txt', 'w') as f:
            pass
    else:
        print('Following instances were found:')
        for inst in instances:
            print(inst)
            
        with open(f'{concept_name}>.individuals.txt', 'w') as f:
            for inst in instances:
                f.write(inst)
                f.write('\n')



# In[5]:





# In[ ]:





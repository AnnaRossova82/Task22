#!/usr/bin/env python
# coding: utf-8

# In[42]:


#Згідно математичній формулі, має бути: 15math+16physics+19chemistry-(6physics_chemistry+9 math_chemistry+7 Math_physics)+4 All subjects = 32
AtLeastOneGoodMark = 15+16+19-(6+9+7)+4
print(AtLeastOneGoodMark)
Math = {'John', 'Mike', 'July', 'Alex', 'Ann', 'Peter', 'Joseph', 'George', 'Amily', 'Jane', 'Mary', 'Stephan', 'M1', 'M2', 'M3'}
Physics = {'John', 'Mike', 'July', 'Alex', 'Mark', 'Kate', 'Ann', 'Peter', 'Joseph', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7'}
Chemistry = {'John', 'Mike', 'July', 'Alex', 'Mark', 'Kate', 'George', 'Amily', 'Jane', 'Mary', 'Stephan', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8'}
PhysicsChemistry={'John', 'Mike', 'July', 'Alex', 'Mark', 'Kate'}
MathChemistry = {'John', 'Mike', 'July', 'Alex', 'George', 'Amily', 'Jane', 'Mary', 'Stephan'}
MathPhysics = {'John', 'Mike', 'July', 'Alex', 'Ann', 'Peter', 'Joseph'}
MathPhysicsChemistry = {'John', 'Mike', 'July', 'Alex'}

#The best way - to use len of each set and calculate by formula:
print("Studens have at least one good mark:",(len(Math)+len(Physics)+len(Chemistry)-(len(PhysicsChemistry)+len(MathChemistry)+len(MathPhysics))+len(MathPhysicsChemistry)))

#Add 'John', 'Mike', 'July', 'Alex' to all categories as they have success for all subjects
#Name PhysicsChemistry two left students 'Mark', 'Kate', add them to Physics and to Chemistry also
#Math Physics and accordingly solo math and physics - name 'Ann', 'Peter', 'Joseph'
#MathChemistry name 'George', 'Amily', 'Jane', 'Mary', 'Stephan'
#Left - name somehow differenf for each subject, lazy to remember more names...

#Just to check if all is written fine - find total matching
res = MathPhysicsChemistry&MathPhysics&MathChemistry&PhysicsChemistry&Chemistry&Physics&Math

#Now update all sets, matching pairs will join and we get list of unique studends with names
Math.update(Physics,Chemistry,PhysicsChemistry,MathChemistry,MathPhysics,MathPhysicsChemistry)
print(Math)
print(len(Math))

#both variants get 32 students fortunately






# In[49]:


#Згідно математичній формулі, має бути: 12rain+8wind+4cold-(2WindCold+5RainWind+3RainCold)+1RainWindCold = 15, тому гарної погоди буде 30 - 15 = 15 днів
BadWeather = 12+8+4-(2+5+3)+1
print(BadWeather)
Rain = {'bzz1', 'bzz3', 'bzz4', 'bzz5', 'bzz6', 'bzz7', 'bzz8', 'r1', 'r2', 'r3', 'r4', 'r5'}
Wind = {'bzz1', 'bzz2', 'bzz5', 'bzz6', 'bzz7', 'bzz8', 'w1', 'w2'}
Cold = {'bzz1', 'bzz2', 'bzz3', 'bzz4'}
RainWind = {'bzz1', 'bzz5', 'bzz6', 'bzz7', 'bzz8'}
RainCold = {'bzz1', 'bzz3', 'bzz4'}
WindCold = {'bzz1', 'bzz2'}
RainWindCold = {'bzz1'}
#Add days to list the same method as with students from task before
print("Unlucky weather in Sept:",(len(Rain)+len(Wind)+len(Cold)-(len(RainWind)+len(RainCold)+len(WindCold))+len(RainWindCold)))

Rain.update(Wind, Cold, RainWind, RainCold, WindCold, RainWindCold)
print(Rain)
print(len(Rain))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





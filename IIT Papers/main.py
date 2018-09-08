# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 20:34:35 2018

@author: Nikhil Anand
"""

#Reading the python files

import PyPDF2
pdf_file_obj=open('2018/Paper1.pdf','rb')
content=" "
pdf_reader=PyPDF2.PdfFileReader(pdf_file_obj)
for i in range(0,pdf_reader.numPages):
    content=content+pdf_reader.getPage(i).extractText()
    
content = " ".join(content.replace(u"\xa0", " ").strip().split())

for x in content:
    x.replace(' \n ','')


content.lower()    



#tokenizing words

import nltk
words=nltk.tokenize.word_tokenize(content)


#Removing stop words
from nltk.corpus import stopwords
stopword_list=set(stopwords.words('english'))
list_stop_char=['(',')',':','.',',','/','-','=','?',';'
                 ,'A','B','C','D'
                 ,'1','2','3','4','12','8','10','11'
                 ,'option','options'
                 ,'question','questions'
                 ,'The','If'
                 ,'Paper','Marks','marks'
                 ,'given','following'
                 ,'JEE','Advanced'
                 ,'PARAGRAPH'
                 ,'correct'
                 ,'answer'
                 ,'chosen'
                 ,'There'
                 ,'first','second','one','two','three','four','five'
                 ,'respectively'
                 ,'2018','2017','2016','2015','2014','2013','2012','2011','2010','2009','2008'
                 ,'value'
                 ,'Let'
                 ,'This'
                 ,'result'
                 ,'constant'
                 ,'section','SECTION'
                 ,'contains'
                 ,'Answer'
                 ,'For'
                 ,'In'
                 ,'ONLY','let'
                 ,'marking','scheme'
                 ,'selecting','Selecting'
                 ,'according'
                 ,'Full'
                 ,'without'
                 ,'evaluated'
                 ,'figure'
                 ,'Then','Each','also'
                 ,'choose','Therefore','Based','defined','Ignore'
                 ,'none'
                 ,'e.g','i.e'
                 ,'based'
                 ,'undergoes'
                 ,'incorrect']
stopword_list.update(list_stop_char)


new_content=[]

for x in words:
    if x not in stopword_list:
        new_content.append(x) 

    
len(new_content)


#check frequency distribution
fdis=nltk.FreqDist(new_content)
fdis.most_common(139)


print(new_content)


""""Analyze and find pattern on which subjects, which topics, which sub-topics are asked most in previous year 
and create a trend analysis"""" 


# step1 : create a list of words belonging to particular topic
# step2 : check whether the words belong to the subject or not using for loops, take the count and plot the graph


#Terms related to mechanics(Physics)

mechanics=set()

mechanics_words = ["hooke's law",
 "newton's first law",
 "newton's second law",
 "newton's third law",
 'acceleration',
 'action',
 'axle',
 'center of gravity',
 'centripetal force',
 'collision',
 'compression',
 'conservation',
 'conservation of momentum',
 'deceleration',
 'direction',
 'displacement',
 'distance',
 'drag',
 'dynamics',
 'efficiency',
 'elastic potential energy',
 'elasticity',
 'energy',
 'equilibrium',
 'force',
 'free fall',
 'friction',
 'fulcrum',
 'gear',
 'gradient',
 'gravitational force',
 'gravity',
 'impact',
 'impulse',
 'inclined plane',
 'inertia',
 'joule',
 'kinematics',
 'kinetic energy',
 'lever',
 'lift',
 'load',
 'machine',
 'magnitude',
 'mass',
 'mechanical advantage',
 'mechanical energy',
 'moment',
 'momentum',
 'motion',
 'newton',
 'pendulum',
 'periodic motion',
 'perpetual motion machine',
 'pivot',
 'potential energy',
 'power',
 'projectile',
 'pulley',
 'reaction',
 'resistance',
 'scalar',
 'screw',
 'simple machine',
 'slope',
 'speed',
 'strain',
 'stress',
 'tensile strength',
 'tension',
 'terminal velocity',
 'thrust',
 'time',
 'torque',
 'vector',
 'velocity',
 'wedge',
 'weight',
 'wheel',
 'wheel and axle',
 'work']

mechanics.update(mechanics_words)


#Terms realted to Fulid dynamics(Physics)
    
fluid=set()

fluid_words=['euler equations',
 "laplace equation",
 'mach number',
 'density',
 'acoustic theory',
 'vorticity',
 'darcy-weisbach equation',
 'supersonic flow',
 'hydrodynamics',
 'strouhal number',
 'compressible flow',
 'streamline - stream function',
 'aerodynamics',
 'reynolds number',
 'ideal Gas',
 'sound barrier',
 'conservation laws',
 'flow Coefficient',
 'pressure',
 'flow measurement',
 'vapor pressure',
 'aeronautics',
 'reynolds number',
 'coanda effect',
 'knudsen number',
 'turbulent flow',
 'turbulence',
 'boundary layer',
 'laminar Flow',
 'surface tension',
 'fluids',
 'liquids',
 'euler number',
 'weber number',
 'non-newtonian fluid',
 'lift',
 'newtonian fluid',
 'hydraulics',
 'transonic',
 'cavitation',
 'velocity',
 'prandtl number',
 "bernoulli's equation",
 'froude number',
 'wave drag',
 'viscosity',
 'richardson number',
 'venturi',
 'navier-Stokes Equations',
 'gas']


fluid.update(fluid_words)


#words realted to Magnetism and Electricity

magnetism=set()

magentism_words=['charles augustin de coulomb',
 'charles proteus steinmetz',
 'james clerk maxwell',
 'michael faraday',
 'nikola tesla',
 'thomas edison',
 'alternating current',
 'ampere',
 'atom',
 'attract',
 'attraction',
 'bar magnet',
 'battery',
 'bioelectricity',
 'capacitor',
 'charge',
 'circuit',
 'closed circuit',
 'compass',
 'conduct',
 'conductivity',
 'conductor',
 'current',
 'cycle',
 'direct current',
 'electric field',
 'electrical energy',
 'electricity',
 'electromagnet',
 'electromagnetic',
 'electromagnetic wave',
 'electromotive force',
 'electron',
 'electrostatic',
 'electrostatic field',
 'electrostatics',
 'ferromagnetism',
 'field',
 'force',
 'frequency',
 'friction',
 'generator',
 'gravitational field',
 'hertz',
 'hysteresis',
 'induction',
 'inductor',
 'insulator',
 'ion',
 'magnet',
 'magnetic',
 'magnetic field',
 'magnetic flux',
 'magnetic force',
 'magnetic moment',
 'magnetic pole',
 'magnetism',
 'metal',
 'negative charge',
 'neutral',
 'nucleus',
 'ohm',
 'open circuit',
 'parallel circuit',
 'permanent magnet',
 'positive charge',
 'potential difference',
 'proton',
 'repel',
 'resistance',
 'resistivity',
 'resistor',
 'semiconductor',
 'series circuit',
 'solution',
 'static electricity',
 'switch',
 'terminal',
 'vector',
 'volt',
 'voltage']

magnetism.update(magentism_words)


#waves related terms

waves=set()

waves_words=['doppler effect',
 'amplitude',
 'angle of reflection',
 'compression',
 'crest',
 'diffraction',
 'electric',
 'electromagnetic',
 'electromagnetic spectrum',
 'electromagnetic wave',
 'emission',
 'energy',
 'frequency',
 'hertz',
 'intensity',
 'light',
 'loudness',
 'magnetic',
 'medium',
 'overtone',
 'peak',
 'period',
 'periodic motion',
 'photon',
 'pitch',
 'radiation',
 'radio wave',
 'rarefaction',
 'reflection',
 'refraction',
 'sound',
 'sound wave',
 'standing wave',
 'superposition',
 'transverse',
 'vacuum',
 'vibration',
 'wave',
 'wavelength']


waves.update(waves_words)




#words related to thermodynamics
thermo=set()

thermo_words=['automobile',
 'automobile engine',
 'change',
 'connection',
 'conversion',
 'cooling',
 'device',
 'devices',
 'energy',
 'engine',
 'equivalent',
 'explain',
 'heat',
 'heat energy',
 'important',
 'law',
 'law of thermodynamics',
 'machine',
 'mechanical',
 'mechanical energy',
 'refrigerator',
 'study',
 'thermodynamic',
 'thermodynamics',
 'work']




thermo.update(thermo_words)


#words related to atomic physics

atomic=set()

atomic_words=['enrico fermi',
 'ernest rutherford',
 'lise meitner',
 'marie curie',
 'absorber',
 'absorption',
 'alpha decay',
 'alpha particle',
 'atom',
 'atomic bomb',
 'atomic mass',
 'atomic number',
 'atomic weight',
 'background radiation',
 'beta decay',
 'beta particle',
 'binding energy',
 'breeder reactor',
 'chain reaction',
 'curie',
 'decay',
 'electromagnetic radiation',
 'electron',
 'electron volt',
 'excited',
 'gamma radiation',
 'gamma ray',
 'half-life',
 'hydrogen bomb',
 'ion',
 'ionizing radiation',
 'irradiate',
 'isomer',
 'isotope',
 'mass defect',
 'neutron',
 'nuclear',
 'nuclear fission',
 'nuclear fusion',
 'nuclear reaction',
 'nuclear reactor',
 'nucleon',
 'nucleonics',
 'nucleus',
 'positron',
 'proton',
 'rad',
 'radioactive',
 'radioactive decay',
 'radioisotope',
 'scintillation counter',
 'stability',
 'tracer',
 'transmutation']

atomic.update(atomic_words)



#Analyzing the percentage of sub topics

#mechanics

count_mechanics=0

for words in new_content:
    if words in mechanics:
        count_mechanics=count_mechanics+1
        
# 77 words out of 1957  (3.93%)      

#fluid dynamics

count_fluid=0

for words in new_content:
    if words in fluid:
        count_fluid=count_fluid+1
        
# 1 words out of 1957  (0.05%)      

#magnetism

count_magnetism=0

for words in new_content:
    if words in magnetism:
        count_magnetism=count_magnetism+1
        
# 47 words out of 1957  (2.4%)      


#waves and oscillations

count_waves=0

for words in new_content:
    if words in waves:
        count_waves=count_waves+1
        
# 29 words out of 1957  (1.4%)      


#thermodynamics

count_thermo=0

for words in new_content:
    if words in thermo:
        count_thermo=count_thermo+1
        
# 11 words out of 1957  (0.56%)      


#atomic physics

count_atomic=0

for words in atomic:
    if words in atomic:
        count_atomic=count_atomic+1
        
# 54 words out of 1957  (2.7%)      


#total words 219 (physics) out of 1957
#constitute 11.19%        
        
import matplotlib.pyplot as plt
labels='Mechanics','Fluid Dynamics','Magnetism and Electricity','Waves and Oscillations','Thermodynamics','Atomic Physics' 
size=[77,1,47,29,11,54]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1) 
fig1, ax1 = plt.subplots()
ax1.pie(sizes,labels=labels,explode=explode,autopct='%1.1f%%',shadow=False,startangle=90)
ax1.axis('equal')  
plt.show()



#chemistry analysis

#atomic structure

atomic_str=set()

atomic_str_words=['atom',
 'atomic mass',
 'atomic mass unit',
 'atomic number',
 'atomic theory',
 'cathode ray',
 'electron',
 'group',
 'isotope',
 'mass number',
 'neutron',
 'nucleus',
 'period',
 'periodic table',
 'proton']


atomic_str.update(atomic_str_words)


#Electrochemistry


electrochem=set()

electro_chem_words =['adding cell potentials,
 'electrochemistry',
 'electrolysis',
 'electrorefining',
 "hess's law",
 'line notation',
 'nernst equation',
 'redox',
 'work',
 'anode',
 'cathode',
 'Cell potential',
 'current',
 'electrode',
 'electrolytic Cell',
 'electroplating',
 'galvanic cell',
 'half-cell',
 'half-reaction',
 'oxidation',
 'oxidation oumber',
 'oxidation potential',
 'oxidizing agent',
 'potentiometer',
 'reaction quotient',
 'reducing agent',
 'reduction',
 'reduction potential',
 'standard state',
 'emf'
]















""" """

from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()

url = "http://www.sparknotes.com/chemistry/electrochemistry/electrolytic/terms/"
response = http.request('GET', url)
soup = BeautifulSoup(response.data)

electro=set()
#scrapping the mechanics keywords
#all_links = soup.find_all("a",class_="word dynamictext")
all_links = soup.find_all("b")
for link in all_links:
    electro.add(link.next) #contents can also be used

"""

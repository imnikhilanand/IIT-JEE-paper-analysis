from IIT_analysis.Paper import Paper


class Chemistry(Paper):
    
    def __init__(self,pdf):
        Paper.__init__(self,pdf)
        
    def get_chapters(self):
        self.electrochemistry = {'adding cell potentials',
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
                                 'cell',
                                 'cell potential',
                                 'potential',
                                 'current',
                                 'electrode',
                                 'electrolytic Cell',
                                 'electroplating',
                                 'galvanic',
                                 'galvanic cell',
                                 'half-cell',
                                 'half-reaction',
                                 'oxidation',
                                 'oxidation oumber',
                                 'oxidation potential',
                                 'oxidizing agent',
                                 'potentiometer',
                                 'quotient',
                                 'emf'
                                 }
        
        self.atomic_structure = {'atom',
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
                                 'proton'
                                 }
        
        self.chemical_bonding = { 'chemical bond',
                                 'ionic bond',
                                 'covalent bond',
                                 'bond',
                                 'bonding'}
        
        self.organic_chemistry = {'addition reaction',
                                  'addition',
                                  'alcohol',
                                  'aldehyde',
                                  'alkane',
                                  'alkene',
                                  'alkyne',
                                  'amide',
                                  'amine',
                                  'amino acid',
                                  'aromatic',
                                  'aromatic hydrocarbon',
                                  'asymmetrical',
                                  'benzene',
                                  'butane',
                                  'combustion',
                                  'covalent bond',
                                  'cracking',
                                  'distillation',
                                  'double bond',
                                  'element',
                                  'ester',
                                  'ethane',
                                  'ether',
                                  'fermentation',
                                  'fractional distillation',
                                  'group',
                                  'halide',
                                  'hydrocarbon',
                                  'inorganic',
                                  'inorganic compound',
                                  'ion',
                                  'ionic bond',
                                  'isomer',
                                  'ketone',
                                  'methane',
                                  'molecular formula',
                                  'molecule',
                                  'monomer',
                                  'nonpolar',
                                  'organic',
                                  'organic compound',
                                  'phenol',
                                  'polar',
                                  'polymer',
                                  'polymerization',
                                  'propane',
                                  'saponification',
                                  'saturated',
                                  'structural formula',
                                  'symmetrical',
                                  'tetrahedron',
                                  'toluene',
                                  'valence electron'}
            
        self.bio_chemistry = {'atp',
                              'dna',
                              'krebs cycle',
                              'rna',
                              'acid',
                              'adhesion',
                              'aerobic',
                              'amino acid',
                              'anaerobic',
                              'base',
                              'biochemistry',
                              'carbohydrate',
                              'carbon',
                              'carbonic acid',
                              'cell',
                              'cell membrane',
                              'cell wall',
                              'cellular respiration',
                              'cellulose',
                              'chitin',
                              'citric acid cycle',
                              'cohesion',
                              'denature',
                              'disaccharide',
                              'enzyme',
                              'fatty acid',
                              'fermentation',
                              'glucose',
                              'glycerol',
                              'glycogen',
                              'glycolysis',
                              'homeostasis',
                              'hydrolysis',
                              'hydrophilic',
                              'hydrophobic',
                              'insulation',
                              'lipid',
                              'macromolecule',
                              'metabolism',
                              'monomer',
                              'monosaccharide',
                              'nucleic acid',
                              'nucleotide',
                              'peptide bond',
                              'phospholipid',
                              'phosphorus',
                              'photosynthesis',
                              'polar',
                              'polarity',
                              'polymer',
                              'polymerization',
                              'polypeptide',
                              'polysaccharide',
                              'protein',
                              'pyruvic acid',
                              'starch',
                              'substrate',
                              'triglyceride'}
            
        self.thermodynamics = {'automobile',
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
                             'work'}
        
        self.atomic_chemistry = {'enrico fermi',
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
                               'transmutation'}
        
        self.chemical_equilibrium = {'chemical equilibrium',
                                     'equilibrium',
                                     'cation',
                                     'anion',
                                     'ion',
                                     'common ion',
                                     "Le Chatelier's Principle",
                                     'solubility',
                                     'reversible',
                                     'reverse',
                                     'rate of reaction',
                                     'equilibrium constant',
                                     'common ion effect',
                                     'heterogeneous equilibrium',
                                     'homogeneous equilibrium',
                                     'concentration',
                                     'coefficient',
                                     'dissociation equation',
                                     'dissociation',
                                     'arrow',
                                     'haber',
                                     'K',
                                     'ksp',
                                     'precipitate',
                                     'mass action',
                                     'rate',
                                     'shift',
                                     'solubility',
                                     'solubility product'
                                     }
        
        self.chemical_kinetics = {'catalyst',
                                  'activation',
                                  'activated',
                                  'collision',
                                  'inhibitor',
                                  'intermediate',
                                  'order',
                                  'rate-determining step'
                                  }
            
        self.polymers = {'polymerization',
                         'condensation',
                         'thermoplastic ',
                         'thermosetting',
                         'LDPE',
                         'HDPE',
                         'polyethylene',
                         'terephthalate',
                         'polyviny',
                         'polyethylene',
                         'polypropylene',
                         'polystyrene'
                         }
        
        self.data_dic = {'electrochemistry':0,
                         'chemical_bonding':0,
                         'organic_chemistry':0,
                         'bio_chemistry':0,
                         'thermodynamics':0,
                         'atomic_chemistry':0,
                         'atomic_structure':0,
                         'equilibrium':0,
                         'chemical_kinetics':0,
                         'polymers':0}
        
        
        for y in self.trimmed_content:
            if y in self.electrochemistry:
                self.data_dic['electrochemistry']=self.data_dic['electrochemistry']+1
                    
        for y in self.trimmed_content:
            if y in self.atomic_structure:
                self.data_dic['atomic_structure']=self.data_dic['atomic_structure']+1
        
        for y in self.trimmed_content:
            if y in self.chemical_bonding:
                self.data_dic['chemical_bonding']=self.data_dic['chemical_bonding']+1
        
        for y in self.trimmed_content:
            if y in self.organic_chemistry:
                self.data_dic['organic_chemistry']=self.data_dic['organic_chemistry']+1
        
        for y in self.trimmed_content:
            if y in self.bio_chemistry:
                self.data_dic['bio_chemistry']=self.data_dic['bio_chemistry']+1
                
        for y in self.trimmed_content:
            if y in self.thermodynamics:
                self.data_dic['thermodynamics']=self.data_dic['thermodynamics']+1
        
        for y in self.trimmed_content:
            if y in self.atomic_chemistry:
                self.data_dic['atomic_chemistry']=self.data_dic['atomic_chemistry']+1
                
        for y in self.trimmed_content:
            if y in self.chemical_equilibrium:
                self.data_dic['equilibrium']=self.data_dic['equilibrium']+1
                
        for y in self.trimmed_content:
            if y in self.polymers:
                self.data_dic['polymers']=self.data_dic['polymers']+1
                
        for y in self.trimmed_content:
            if y in self.chemical_kinetics:
                self.data_dic['chemical_kinetics']=self.data_dic['chemical_kinetics']+1
                
                
        return(self.data_dic)   
        
        




# module used

import pickle

''' word dictionary generator '''

# hard_list

words_h={"azure":["Bright blue in colour like acloudless sky","Microsoft's Cloud Computing platform"],   
   "exodus":["is the title given to an Old English alliterative poem in the Junius manuscript","A movie was released with same name,starring Christian Bale and Aaron Paul."],
   "foxglove":["A plant","Also known as Digitalis"],
   "galvanize":["Shock or Excite (someone) into taking action","protects iron from rusting"],
   "gazebo":["is a pavilion building structure, sometimes octagonal or turret-shaped.","often built in a park, garden or spacious public area."],
   "haiku":["is a very short poem in the English language.","is a three-line observation about a fleeting moment involving nature."],
   "hyphen":["is a punctuation mark","used to join words"],
   "ivory":["is a hard, white material from the tusks ","word derives from the ancient Egyptian, through the Latin ebor- or ebur."],
   "jaywalk":["an urban traffic safety problem.","to cross a street without taking advantage of provided means of safe crossing"],
   "jigsaw":["a machine saw with a fine blade enabling it to cut curved lines in a sheet of wood, metal, or plastic.","a puzzle"],
   "jovial":["sociable and genial","cheerful and friendly"],
   "larynx":["internal part of human body","the hollow muscular organ forming an air passage to the lungs"],
   "marques":["is a nobleman of hereditary rank in various European peerages"," The term is also used to translate equivalent Asian styles, as in imperial China and Japan."],
   "pneumonia":["presumed to be bacterial is treated with antibiotics.","inflammatory condition of the lung affecting alveoli"],
   "quartz":["Second most abundant minerals in Earth's continental crust","Used in Wristwatch"],
   "schizophrenia":["a mental disorder","disorder characterized by abnormal social behavior and failure to recognize what is real"],
   "sphinx":["In Arabic, means Father of Dread"," is a mythical creature with, as a minimum, the head of a human and the body of a lion."],
   "swivel":["A coupling between two parts enabling one to revolve without turning the other.","turn around a point or axis"],
   "topaz":["A gem stone","a silicate mineral of aluminium and fluorine"],
   "waltz":["a form of dance","a smooth, progressive ballroom and folk dance, normally in triple time, performed primarily in closed position."],
   "xylophone":[" a musical instrument in the percussion family that consists of wooden bars struck by mallets.","refers specifically to a chromatic instrument of somewhat higher pitch range"],
   "zephyr":["A soft gentle breeze","A fine cotton gingham"],
   "zilch":["means 'nothing'(pronoun)","not any, no (determiner)"]}
   
# easy_list

words_e={"axiom":["From Greek origin that means,'what is thought fitting'","In Mathematics, a statement or proposition on which an abstractly defined structure is based."],
    "askew":["Crooked; Awry","With disapproval, scorn, contempt, etc."],
    "abruptly":["Terminating or changing suddenly","Suddenly, Unexpectedly"],
    "banjo":["Six-stringed instrument with a thin membrane stretched over a frame or cavity as a resonator","In Brazil, derived from the cavaco, and is especially associated with Samba and its variants."],
    "gizmo":["Key on certain flute","s an effects device for the electric guitar and bass guitar"],
    "haphazard":["lacking any obvious principle of organization","random, unplanned, chaotic etc."],
    "kiosk":["a public booth","a small open-fronted hut or cubicle from newspaper, refreshments, tickets etc are sold."],
    "microwave":["used in navigation, radars, Spectroscopy etc.","form of electro-magnetic radiation"],
    "wimpy":["A timid or unadventurous person","weak and ineffectual"],
    "squawk":["four-digit octal numbers; the dials on a transponder read from zero to seven, inclusive.","A discrete transponder code assigned by air traffic controllers to uniquely identify an aircraft."],
    "vortex":["a major component of turbulent flow","a region in a fluid in which the flow is rotating around an axis line, which may be straight or curved."],
    "zodiac":["In historical astronomy, circle of twelve 30degree divisions of celestial longitude that are centered upon the ecliptic, the apparent path of the Sun across the celestial sphere over the course of the year.","12 sign corresponding to 12 longitudinal divivsion"],
    "zombie":["Most commonly found in horror and fantasy genre works.","Their earliest depictions in the comics medium was made DC Comic character Solomon Grundy in 1944 Green Lantern story"],
    "croquet":["A sport involving hitting plastic or wooden balls with a mallet through hoops embedded in a grass playging court","The first set of rules for this sport was registered by Isaac Spratt in November 1856 with the Stationers' Company in London."],
    "mystify":["make obscure or mysterious.","utterly bewilder or perplex (someone)"],
    "bagpipes":["a class of musical instrument, aerophones, using enclosed reeds fed from a constant reservoir of air in the form of a bag.","have been played for centuries (and continue to be played) throughout large parts of Europe, Turkey, the Caucasus, around the Persian Gulf, Northern Africa and North America."]}

# word file creation

l1=[words_e,words_h]
ifile=open("words.dat","wb")
pickle.dump(l1,ifile)
ifile.close()

''' initial userbase creation '''

# initial userbase

d1={"root":["pass",20,11,9,5,6],
    "RAJ":["pass",10,9,1,9,0],
    "MOHAN":["pass",17,9,8,9,0],
    "SOHAM":["pass",11,9,2,9,0],
    "SONU":["pass",15,15,0,9,6]}

# word file creation

ifile=open("user.dat","wb")
pickle.dump(d1,ifile)
ifile.close()

# ---- end of program ----


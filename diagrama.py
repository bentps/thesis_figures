# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np

#define speeds and directions that atoms can go
def middle(x):
    y=0*x
    return y

def base(x):
    y=x
    return y

def four(x):
    y=4*x
    return y

def negbase(x):
    y=-x
    return y

def negfour(x):
    y=-4*x
    return y

#define the time-spans of the various stages of atom-activities
stem=-.0250
warmup1=.500 + .065
warmup2=.500 + .130 + .065
speedy=.065 + .130 + 1.000  + .065
less1=.065 + .130 + .065
less2=.065 + .065
turn1=.065 + .065
turn2=.065 + .130 + .065
brakes=.065 + .130 + 1.000 + .065
warmdown1=.065 + .130 + .500
warmdown2=.065 + .500

#how long are the atoms going for? how many points to plot lines along?
z=np.linspace(stem-.3,5.100,3000)


#define the times at which atom-speeds change
a=stem+warmup1
b=a+speedy
c=b+less1
d=c+turn1
e=d+brakes
f=e+warmdown1

g=stem+warmup2
h=g+speedy
i=h+less2
j=i+turn2
k=j+brakes
l=k+warmdown2

#define where the atoms are when they change speed corresponding to each change-time
chng=stem
chnga=base(a)-chng
chngb=four(b)-(four(a)-chnga)
chngc=base(c)-(base(b)-chngb)
chngd=negbase(d)-(negbase(c)-chngc)
chnge=negfour(e)-(negfour(d)-chngd)

chngg=negbase(g)+chng
chngh=negfour(h)-(negfour(g)-chngg)
chngi=negbase(i)-(negbase(h)-chngh)
chngj=base(j)-(base(i)-chngi)
chngk=four(k)-(four(j)-chngj)


#lay out each path of atoms by which direction they start going at the first pulse
def top(x):
    y=np.piecewise(
        x, [(x>=stem) & (x<a),(x>=a) & (x<b),(x>=b) & (x<c),
        (x>=c) & (x<d),(x>=d) & (x<e),x>=e],
        [lambda x: base(x)-chng, 
        lambda x: four(x)-(four(a)-chnga), 
        lambda x: base(x)-(base(b)-chngb),
        lambda x: negbase(x)-(negbase(c)-chngc), 
        lambda x: negfour(x)-(negfour(d)-chngd),
        lambda x: negbase(x)-(negbase(e)-chnge)]
    )
    return y

def bottom(x):
    y=np.piecewise(
        x, [(x>=stem) & (x<g),(x>=g) & (x<h),(x>h) & (x<i),
        (x>=i) & (x<j),(x>=j) & (x<k),x>=k],
        [lambda x: negbase(x)+chng, 
        lambda x: negfour(x)-(negfour(g)-chngg), 
        lambda x: negbase(x)-(negbase(h)-chngh),
        lambda x: base(x)-(base(i)-chngi), 
        lambda x: four(x)-(four(j)-chngj),
        lambda x: base(x)-(base(k)-chngk)]
    )
    return y
    

# the x,y values of the change-points just in case
points = np.array([
    [stem,middle(stem)],
    [a,chnga],
    [b,chngb],
    [c,chngc],
    [d,chngd],
    [e,chnge],
    [f,middle(f)],
    [g,chngg],
    [h,chngh],
    [i,chngi],
    [j,chngj],
    [k,chngk],
    [l,middle(l)]
])
x, y = points.T

#define the pulses as functions
def pulse(x, phase, amp, period):
    y=amp*(np.cos(2*np.pi*x/period+phase)+1)
    return y  
 
def phase(x, period):
    phase=-2*np.pi*x/period-np.pi
    return phase

def null(x):
    pass
    

#define pulse-set lengths and start times
initial=.050
onepulse=.130
twopulses=.260
ropulse=.500

s1=stem + .500
s2=s1 + twopulses + 1.000
mid=s2 + twopulses
s3=mid + onepulse
s4=s3 + twopulses + 1.000

#piecewise functions for the pulses at their times
def toppulses(x):
    y=np.piecewise(
        x, [x<s1, (x>=s1) & (x<=s1+onepulse), (x>s1+onepulse) & (x<s2), (x>=s2) & (x<=s2+onepulse),
            (x>s2+onepulse) & (x<s3), (x>=s3) & (x<=s3+onepulse), (x>s3+onepulse) & (x<s4),
            (x>=s4) & (x<=s4+onepulse), x>s4+onepulse],
        [lambda x: null(x),
        lambda x: pulse(x, phase(s1, onepulse),1, onepulse),
        lambda x: null(x), 
        lambda x: pulse(x, phase(s2, onepulse),1, onepulse),
        lambda x: null(x),
        lambda x: pulse(x, phase(s3, onepulse),1, onepulse),
        lambda x: null(x),
        lambda x: pulse(x, phase(s4, onepulse),1, onepulse),
        lambda x: null(x)]
    )
    return y

def bottompulses(x):
    y=np.piecewise(
        x, [x<s1+onepulse, (x>=s1+onepulse) & (x<=s1+twopulses), (x>s1+twopulses) & (x<s2+onepulse),
            (x>=s2+onepulse) & (x<=s2+twopulses), (x>s2+twopulses) & (x<s3+onepulse),
            (x>=s3+onepulse) & (x<=s3+twopulses), (x>s3+twopulses) & (x<s4+onepulse),
            (x>=s4+onepulse) & (x<=s4+twopulses), x>s4+twopulses],
        [lambda x: null(x),
        lambda x: pulse(x, phase(s1, onepulse),1, onepulse),
        lambda x: null(x), 
        lambda x: pulse(x, phase(s2, onepulse),1, onepulse),
        lambda x: null(x),
        lambda x: pulse(x, phase(s3, onepulse),1, onepulse),
        lambda x: null(x),
        lambda x: pulse(x, phase(s4, onepulse),1, onepulse),
        lambda x: null(x)]
    )
    return y

def midpulse(x):
    y=np.piecewise(
        x, [x<mid, (x>=mid) & (x<=mid+onepulse), x>mid+onepulse],
        [lambda x: null(x),
        lambda x: pulse(x, phase(mid, onepulse), 0.5, onepulse),
        lambda x: null(x)]
    )
    return y

def initialpulse(x):
    y=np.piecewise(
        x, [x<stem, (x>=stem) & (x<=stem+initial), x>stem+initial],
        [lambda x: null(x),
        lambda x: pulse(x, phase(stem-initial, initial), 0.5, initial),
        lambda x: null(x)]
    )
    return y

def readout(x):
    y=np.piecewise(
        x, [x<f-ropulse/2, (x>f-ropulse/2) & (x<f+ropulse/2), x>f+ropulse/2],
        [lambda x: null(x),
        lambda x: 1,
        lambda x: null(x)]
    )
    return y

#plt.plot(z,toppulses(z))
#plt.plot(z,bottompulses(z))
#plt.plot(z,midpulse(z))
#plt.plot(z,initialpulse(z))

######################
#plot everything!!
######################
#tweakable feats
atomlines = 2.5
pulselines = 1

# set up the subplots and their areas on the grid
atoms = plt.subplot2grid((13, 8), (0, 0), colspan=8, rowspan=10)
puls = plt.subplot2grid((13, 8), (10, 0), colspan=8, rowspan=3)

#'#f87217'
#'steelblue'

#plot the atoms' paths
atoms.plot(z,top(z),linewidth=atomlines, color='steelblue')
atoms.plot(z,bottom(z),linewidth=atomlines, color='#f87217')
atoms.plot(z,middle(z),linewidth=atomlines, color='black')

#plot the pulses
puls.plot(z,toppulses(z),linewidth=pulselines, color='green')
puls.plot(z,bottompulses(z),linewidth=pulselines, color='green')
puls.plot(z,midpulse(z),linewidth=pulselines, color='green')
puls.plot(z,initialpulse(z),linewidth=pulselines, color='green')
puls.plot(z,readout(z),linewidth=pulselines,color='purple')

#specify axis and tick visibility, label axes, control gap between plot
#puls.spines['top'].set_visible(False)
atoms.tick_params(bottom='off')
atoms.axes.get_xaxis().set_ticks([])
puls.set_xlabel('Time (ms)',fontsize=14)
atoms.set_ylabel('Distance',fontsize=14)
puls.set_ylabel('Intensity',fontsize=14)
puls.yaxis.labelpad = 12
plt.subplots_adjust(hspace=-0.1)



#extremely hacky arrow situation
hl=0.09
hw=0.6
w=0.015
yval=-6.37
puls.arrow(a+1.5*onepulse,3,speedy-twopulses-hl,0,
            width=w, color='k', overhang=0.5, head_width=hw, head_length=hl)
puls.arrow(b-onepulse/2,3,-speedy+twopulses+hl,0,
            width=w, color='k', overhang=0.5, head_width=hw, head_length=hl)
atoms.arrow(a+1.5*onepulse,yval,speedy-twopulses-hl,0,
            width=w, color='k', overhang=0.5, head_width=hw, head_length=hl)
atoms.arrow(b-onepulse/2,yval,-speedy+twopulses+hl,0,
            width=w, color='k', overhang=0.5, head_width=hw, head_length=hl)
puls.arrow(d+1.5*onepulse,3,speedy-twopulses-hl,0,
            width=w, color='k', overhang=0.5, head_width=hw, head_length=hl)
puls.arrow(e-onepulse/2,3,-speedy+twopulses+hl,0,
            width=w, color='k', overhang=0.5, head_width=hw, head_length=hl)
atoms.arrow(d+1.5*onepulse,yval,speedy-twopulses-hl,0,
            width=w, color='k', overhang=0.5, head_width=hw, head_length=hl)
atoms.arrow(e-onepulse/2,yval,-speedy+twopulses+hl,0,
            width=w, color='k', overhang=0.5, head_width=hw, head_length=hl)




#force x axes to be equal
puls.axis([stem-0.3,5.100+stem-.3,-0,3])
atoms.axis([stem-0.3,5.100+stem-.3,-6.500,6.500])


#add anotations, and remove tick labels:
puls.yaxis.set_ticklabels([])

atoms.text(1.18, -6, 'T')
atoms.text(2.83, -6, 'T')
atoms.text(1.1, -2, '3',color='#f87217')
atoms.text(1.1, .4, '2')
atoms.text(1.1, 3.5, '1',color='steelblue')
atoms.yaxis.set_ticklabels([])


#add vertical colored background areas and dotted lines to visually connect pulses w atoms
figures=[atoms,puls]
for s in [s1,s2,s3,s4]:
    currentrange=np.linspace(s,s+onepulse,500)
    atoms.fill_between(currentrange, -6.500,top(currentrange), facecolor='#e2eef9')
    puls.fill_between(currentrange, 0,3, facecolor='#e2eef9')
    currentrange=np.linspace(s+onepulse,s+twopulses,500)
    atoms.fill_between(currentrange, -6.500,bottom(currentrange), facecolor='#ffa07a', alpha=0.4)
    puls.fill_between(currentrange, 0,3, facecolor='#ffa07a', alpha=0.4)

for fi in figures:
    fi.axvspan(stem, stem+initial, facecolor='black', alpha=0.2)
    fi.axvspan(mid, mid+onepulse, facecolor='black', alpha=0.2)
    fi.axvspan(f-ropulse/2, f+ropulse/2, facecolor='purple', alpha=0.15)         

#add vertical lines up to readoutpulse
for xvalue in [f-ropulse/2, f+ropulse/2]:
    puls.vlines(x=xvalue, ymin=0, ymax=1, linewidth=1, color='purple')

#plt.savefig('./fig1a_17-07-20.pdf')

#'#e2eef9'
#'#ffa07a'





#ticks_atoms = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(y/10))
#atoms.yaxis.set_major_formatter(ticks_atoms)


#for s in [s1,s2,s3,s4]:
#    for fi in figures:
#        fi.axvspan(s, s+onepulse, facecolor='#e2eef9')
#        fi.axvspan(s+onepulse, s+twopulses, facecolor='#ffa07a', alpha=0.25)

#f, (a, p) = plt.subplots(1,2)
#plt.figure(1, figsize=(8,8))
#plt.subplot(211)
#plt.scatter(x,y,s=1)
#atoms.spines['bottom'].set_visible(False)
#atoms.tick_params(bottom='off')
#plt.savefig('../Documents/bendata/test3.pdf')
#plt.axis([19,21,55,58])
#plt.figure(2,figsize=(8,2))
#p=plt.subplot(212)
#puls.spines['right'].set_visible(False)
#puls.yaxis.set_ticks_position('left')
#puls.xaxis.set_ticks_position('bottom')
#plt.axis([0,40,0,5])

#for xvalue in [stem, mid+onepulse/2]:
#    for fi in figures:
#        fi.axvline(x=xvalue, linewidth=0.5, color='black', linestyle='dashed')

#atoms.axvspan(s1, s1+onepulse, facecolor='steelblue', alpha=0.2)
#puls.axvspan(s1, s1+onepulse, facecolor='steelblue', alpha=0.2)
#atoms.axvspan(s1, s1+twopulses, facecolor='#f87217', alpha=0.2)
#puls.axvspan(s1, s1+twopulses, facecolor='#f87217', alpha=0.2)
#
#atoms.axvspan(s2, s2+onepulse, facecolor='steelblue', alpha=0.2)
#puls.axvspan(s2, s2+onepulse, facecolor='steelblue', alpha=0.2)
#atoms.axvspan(s2, s2+twopulses, facecolor='#f87217', alpha=0.2)
#puls.axvspan(s2, s2+twopulses, facecolor='#f87217', alpha=0.2)

#atoms.axvspan(s3, s3+onepulse, facecolor='steelblue', alpha=0.2)
#puls.axvspan(s3, s3+onepulse, facecolor='steelblue', alpha=0.2)
#atoms.axvspan(s3, s3+twopulses, facecolor='#f87217', alpha=0.2)
#puls.axvspan(s3, s3+twopulses, facecolor='#f87217', alpha=0.2)
#
#atoms.axvspan(s4, s4+onepulse, facecolor='steelblue', alpha=0.2)
#puls.axvspan(s4, s4+onepulse, facecolor='steelblue', alpha=0.2)
#atoms.axvspan(s4, s4+twopulses, facecolor='#f87217', alpha=0.2)
#puls.axvspan(s4, s4+twopulses, facecolor='#f87217', alpha=0.2)

#f.tight_layout()

#
#
#def toppulses(x):
#    y=np.piecewise(
#        x, [(x>=s1) & (x<=s1+onepulse), (x>=s2) & (x<=s2+onepulse),
#            (x>=s4) & (x<=s4+onepulse), (x>=s5) & (x<=s5+onepulse)],
#        [lambda x: pulse(x, phase(s1),1), 
#        lambda x: pulse(x, phase(s2),1), 
#        lambda x: pulse(x, phase(s4),1), 
#        lambda x: pulse(x, phase(s5),1)]
#    )
#    return y
#
#def bottompulses(x):
#    y=np.piecewise(
#        x, [(x>=s1+onepulse) & (x<=s1+twopulses), (x>=s2+onepulse) & (x<=s2+twopulses),
#            (x>=s4+onepulse) & (x<=s4+twopulses), (x>=s5+onepulse) & (x<=s5+twopulses)],
#        [lambda x: pulse(x, phase(s1),1), 
#        lambda x: pulse(x, phase(s2),1), 
#        lambda x: pulse(x, phase(s4),1), 
#        lambda x: pulse(x, phase(s5),1)]
#    )
#    return y
#
#def mid(x):
#    y=np.piecewise(
#        x, [(x>=s3) & (x<=s3+onepulse)],
#        [lambda x: pulse(x, phase(s3),0.5)]
#    )
#    return y
#def t1(x):
#     y=np.piecewise(x,[(x>=s1) & (x<=s1+onepulse)],[lambda x: pulse(x, phase(s1),1)])
#     return y
#t1r=np.linspace(s1,s1+onepulse,100)
#plt.plot(t1r,t1(t1r))
#plt.plot(z,top(z))
#
#def t2(x):
#     y=np.piecewise(x,[(x>=s2) & (x<=s2+onepulse)],[lambda x: pulse(x, phase(s2),1)])
#     return y
# 
#def t3(x):
#     y=np.piecewise(x,[(x>=s3) & (x<=s3+onepulse)],[lambda x: pulse(x, phase(s3),1)])
#     return y
#
#def t4(x):
#     y=np.piecewise(x,[(x>=s4) & (x<=s4+onepulse)],[lambda x: pulse(x, phase(s4),1)])
#     return y
#
#def b1(x):
#     y=np.piecewise(x,[(x>=s1+onepulse) & (x<=s1+twopulses)],[lambda x: pulse(x, phase(s1),1)])
#     return y
# 
#def b2(x):
#     y=np.piecewise(x,[(x>=s2+onepulse) & (x<=s2+twopulses)],[lambda x: pulse(x, phase(s2),1)])
#     return y
# 
#def b3(x):
#     y=np.piecewise(x,[(x>=s3+onepulse) & (x<=s3+twopulses)],[lambda x: pulse(x, phase(s3),1)])
#     return y
#
#def b4(x):
#     y=np.piecewise(x,[(x>=s4+onepulse) & (x<=s4+twopulses)],[lambda x: pulse(x, phase(s4),1)])
#     return y    
    

# Preliminary Report


### Introduction to the SIR Model and Notation

The SIR model is built based on the first-order derivative to model the spread of infectious disease, where the time dependent variables $S$, $I$, $R$ each represent the following populations: 

$S$(susceptible): number of individuals who are not infected but could become infected

$I$(infected): number of individuals who are already infected and can spread disease
    
$R$(removed): number of individuals who are either recovered and immune or have died
    
And $s$, $i$, $r$ are used to represent the proportion of susceptible, infected and removed individuals among the population. 

There are two parameters $b$ and $k$ in the model, where $b$ indicates the number of interactions each day that could spread the disease (per individual) and $k$ indicates the fraction of the infectious population which recovers each day. 

In the ODE-based model, we can get the following system of differential equations:

$\frac{ds}{dt} = -b * s(t) * i(t)$

$\frac{dr}{dt} = k * i(t)$

$\frac{di}{dt} = b * s(t) * i(t) - k * i(t)$






### Python Package 'sir'




### Discrete Agent-Based Model




### Continuous/ODE-Based Model




### Variations and Improvements






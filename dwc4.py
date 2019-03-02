# BusBar500kV, 09-Feb-2019
# D-Wave Challenge 4

import dwavebinarycsp
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import dimod

shots=100
# Solving as a QUBO Problem method 1 using converting to BQM
j01=1
h0=-0.2
h1=-0.2
linear = {1: h0, 2: h1}
quadratic = {(1, 2): j01}
bqm = dimod.BinaryQuadraticModel(linear, quadratic, 0.0, dimod.BINARY)

sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample(bqm, num_reads=shots)

print('\n************ QUBO - Results - Method 1 using converting to BQM **************')
for res in response.data(['sample', 'energy', 'num_occurrences']):
    print('|s1 = %s |s2 = %s | Energy = %f | Probability  = %f %% ' % (res.sample[1],res.sample[2],
          res.energy, res.num_occurrences*100/shots))



# Solving as a QUBO Problem - Method 2 using automatic embedding
j01=1
h0=-0.2
h1=-0.2
linear = {('s0','s0'): h0, ('s1','s1'): h1}
quadratic = {('s0','s1'): j01}
Q=dict(linear)
Q.update(quadratic)

response = EmbeddingComposite(DWaveSampler()).sample_qubo(Q,num_reads=shots)

print('\n************ QUBO - Results - Method 2 using automatic embedding ************** \n')
for res in response.data(['sample', 'energy', 'num_occurrences']):
    print('|s1 = %s |s2 = %s | Energy = %f | Probability  = %f %% ' % (res.sample['s0'],res.sample['s1'],
          res.energy, res.num_occurrences*100/shots))

# Solving as a QUBO Problem - Method 3 using manual embedding
j01=1
h0=-0.2
h1=-0.2
q1=0
q2=1
biases = {(q1,q1): h0, (q2,q2): h1}
coupler_strengths = {(q1,q2): j01}
Q=dict(biases)
Q.update(coupler_strengths)

response = EmbeddingComposite(DWaveSampler()).sample_qubo(Q,num_reads=shots)
# response = sampler.sample(bqm, num_reads=shots)

print('\n************ QUBO - Results - Method 3 using manual embedding ************** \n')
print('Unit cell status :',DWaveSampler().nodelist[0:8])
for res in response.data(['sample', 'energy', 'num_occurrences']):
    print('|s1 = %s |s2 = %s | Energy = %f | Probability  = %f %% ' % (res.sample[q1],res.sample[q2],
          res.energy, res.num_occurrences*100/shots))
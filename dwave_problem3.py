# BusBar500kV, 03-Feb-2019
# D-Wave Challenge 3

import dwavebinarycsp
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import dimod

gcost=1


def min_cost(s0,s1):
    global gcost
    j01 = -1
    h0 = -0.5
    h1 = 0

    c=h0*s0+h1*s1+j01*s0*s1
    if c<gcost:
        gcost=c
        return True
    else:
        return False


# Method 1 - Solving as a Constraint Satisfaction Problem
csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.SPIN)
shots=100
csp.add_constraint(min_cost,['s1','s2'])
bqm1 = dwavebinarycsp.stitch(csp, max_graph_size=2)
sampler1 = EmbeddingComposite(DWaveSampler())
response1 = sampler1.sample(bqm1, num_reads=shots)
print('************ Method 1 - Constaint Satisfaction Problem - Results ************** \n')
for res in response1.data(['sample', 'energy', 'num_occurrences']):
    print('|s1 = %s |s2 = %s | Energy = %f | Probability  = %f %% ' % (res.sample['s1'],res.sample['s2'],
          res.energy, res.num_occurrences*100/shots))

exit(0)

# Method 2 - Solving as a Binary Quadratic Model Problem
j01=-1
h0=-0.5
h1=0
linear = {1: h0, 2: h1}
quadratic = {(1, 2): j01}
bqm2 = dimod.BinaryQuadraticModel(linear, quadratic, 0.0, dimod.BINARY)

sampler2 = EmbeddingComposite(DWaveSampler())
response2 = sampler2.sample(bqm2, num_reads=shots)

print('************ Method 2 - Binary Quadratic Model - Results ************** \n')
for res in response2.data(['sample', 'energy', 'num_occurrences']):
    print('|s1 = %s |s2 = %s | Energy = %f | Probability  = %f %% ' % (res.sample[1],res.sample[2],
          res.energy, res.num_occurrences*100/shots))
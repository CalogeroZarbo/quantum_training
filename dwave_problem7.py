# Calogero Zarbo, Docebo, 2-Mar-2019
# D-Wave Challenge 7

#   NAE3SAT Truth Table
# Q-1    Q-2    Q-3    R
#  0      0      0     1
#  0      0      1     0
#  0      1      0     0
#  0      1      1     0
#  1      0      0     0
#  1      0      1     0
#  1      1      0     0
#  1      1      1     1

from dwave.system.composites import EmbeddingComposite
from dwave.system.samplers import DWaveSampler
import dwavebinarycsp
import dimod
import operator

def not_all_equal(q1, q2, q3): 
    return not ((q1 == q2) and (q2 == q3))


csp = dwavebinarycsp.ConstraintSatisfactionProblem(vartype=dimod.Vartype.SPIN) 
csp.add_constraint(not_all_equal, ['q1', 'q2', 'q3'])

my_bqm = dwavebinarycsp.stitch(csp)

print(my_bqm)

exit(0)

sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample(my_bqm, num_reads = 5000)
for sample, energy, occurences in response.data(['sample', 'energy', 'num_occurrences']):
    print(list(sample.values()), 'Occurrences:', occurences, 'Energy:', energy)
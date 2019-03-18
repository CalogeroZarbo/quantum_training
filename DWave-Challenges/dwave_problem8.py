# Calogero Zarbo, Docebo, 17-Mar-2019
# D-Wave Challenge 8

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
from dimod import ExactSolver
import dwavebinarycsp
import dimod
import operator


def not_all_equal(q1, q2, q3): 
    return not ((q1 == q2) and (q2 == q3))

csp = dwavebinarycsp.ConstraintSatisfactionProblem(vartype=dimod.Vartype.SPIN) 
csp.add_constraint(not_all_equal, ['a', 'b', 'c'])
csp.add_constraint(not_all_equal, ['c', 'd', 'e'])

my_bqm = dwavebinarycsp.stitch(csp)

print(my_bqm)


print('Classical Solver')
sampler = ExactSolver()
response = sampler.sample(my_bqm)
for sample, energy, occurrences in response.data(['sample', 'energy', 'num_occurrences']):
    print(list(sample.values()),'Occurrences :',occurrences,'Energy :',energy)

print('DWave Solver')
sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample(my_bqm, num_reads = 5000)
for sample, energy, occurences in response.data(['sample', 'energy', 'num_occurrences']):
    print(list(sample.values()), 'Occurrences:', occurences, 'Energy:', energy)

print('The correct answer is 18, while I said 10.')
print('I got busted by the stochastic nature of the Quantum Solver, which does not give all the results, and not always the same ones.')
print('Credit to Yasas for the explanation: https://github.com/yasasp/Dwave-Challenges/blob/master/dwc8.py')
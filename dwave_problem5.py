# Calogero Zarbo, Docebo, 16-Feb-2019
# D-Wave Challenge 5
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import dimod


shots = 100
# Converting the Model and Checking the formulation
bqm = dimod.BinaryQuadraticModel({0: -1, 1: -1}, {(0, 1): 2}, 0.0, dimod.BINARY)
bqm_ising = bqm.change_vartype(dimod.SPIN, inplace=False)

print('Giving QUBO: E(x0,x1) = -x0 -x1 +2*x0*x1 ')
print('The Ising formulation is:')
print('h0:',bqm_ising.linear[0], '|', 'h1:',bqm_ising.linear[1], '|', 'j01:', bqm_ising.quadratic[(0,1)])
print('With an offset of:', bqm_ising.offset)

# Check the consistency of the results
sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample(bqm_ising, num_reads=shots)

print('\n************ Check Results using EmbeddingComposite **************')
for sample, energy, num_occurrences in response.data(['sample', 'energy', 'num_occurrences']):
    print(sample,energy, num_occurrences*100/shots)


print('\n************ Check Results using dmod.ExactSolver **************')
response_2 = dimod.ExactSolver().sample(bqm_ising)
for sample, energy in response.data(['sample', 'energy']): print(sample, energy)

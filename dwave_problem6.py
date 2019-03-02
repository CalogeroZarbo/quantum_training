# BusBar500kV, 24-Feb-2019
# D-Wave Challenge 6

from dwave.system.composites import FixedEmbeddingComposite
from dwave.system.samplers import DWaveSampler

# Part 1: Largest Largest complete graph Kn'' that can be a sub-graph of bipartite graph K4,4
embedding = {'q1': {0}, 'q2': {4}, 'q3': {2, 6}, 'q4': {3, 5}, 'q5': {7, 1}}
sampler = DWaveSampler()
sampler_embedded = FixedEmbeddingComposite(sampler, embedding)
print('\n**********  Part 1: Largest complete graph Kn'' that can be a sub-graph of bipartite graph K4,4 ***********  \n')
print('Assignment : \n',embedding)
print('Neighbourhood check : \n',sampler_embedded.adjacency)

# Part 2: Solving Problem 4 using manual embedding as a QUBO
shots=100
h0=-0.2
h1=-0.2
j01=1
j10=0
sampler = DWaveSampler()
embedding_1 = {'h0': {5}, 'h1': {13}}
Q_not={('h0','h0'):h0,('h0','h1'):j01,('h1','h0'):j10, ('h1','h1'):h1}
sampler_embedded = FixedEmbeddingComposite(sampler, embedding_1)
response = sampler_embedded.sample_qubo(Q_not, num_reads=shots)
print('\n**********  Part 2: Problem 4 using manual embedding to qubit 5 and 13 (in two different unit cells)\n')
for res in response.data(['sample', 'energy', 'num_occurrences']):
    print('|h0 = %s |h1 = %s | Energy = %f | Probability  = %f %% ' % (res.sample['h0'],res.sample['h1'],
          res.energy, res.num_occurrences*100/shots))
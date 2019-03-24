# Calogero Zarbo, Docebo, 24-Mar-2019
# D-Wave Challenge 9

import dwavebinarycsp
import dimod
import minorminer
from dwave.system.composites import FixedEmbeddingComposite, TilingComposite
from dwave.system.samplers import DWaveSampler

def not_all_equal(q1, q2, q3): 
    return not ((q1 == q2) and (q2 == q3))

csp = dwavebinarycsp.ConstraintSatisfactionProblem(vartype=dimod.Vartype.SPIN) 
csp.add_constraint(not_all_equal, ['a', 'b', 'c'])
csp.add_constraint(not_all_equal, ['c', 'd', 'e'])

bqm = dwavebinarycsp.stitch(csp)

chimera_cell = [(i, j + 4) for j in range(4) for i in range(4)]

embeddings = [minorminer.find_embedding(bqm.to_qubo()[0].keys(), chimera_cell) for i in range(100)]
min_emb = min(embeddings, key=lambda x: len(sum(x.values(), [])))
print("Minimum embedding configuration:", min_emb)
print("Minimum embedding length:", len(sum(min_emb.values(), [])))

# Verification of the found embedding
print("Verification of the found embedding")
sampler = FixedEmbeddingComposite(DWaveSampler(), min_emb)
response = sampler.sample(bqm, num_reads = 5000)
for sample, energy, occurences in response.data(['sample', 'energy', 'num_occurrences']):
    print(list(sample.values()), 'Occurrences:', occurences, 'Energy:', energy)

# Bonus question: running in parallel
print("Bonus question: running in parallel")
sampler2 = FixedEmbeddingComposite(TilingComposite(DWaveSampler(), 1, 1, 4), min_emb)
response = sampler.sample(bqm, num_reads = 5000)
for sample, energy, occurences in response.data(['sample', 'energy', 'num_occurrences']):
    print(list(sample.values()), 'Occurrences:', occurences, 'Energy:', energy)

print("Adjacency:", sampler2.adjacency)


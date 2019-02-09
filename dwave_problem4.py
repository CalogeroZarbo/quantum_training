# Calogero Zarbo, Docebo, 09-Feb-2019
# D-Wave Challenge 4

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import dimod

q01=1
q0=-0.2
q1=-0.2
shots = 1000
linear = {1: q0, 2: q1}
quadratic = {(1, 2): q01}
bqm = dimod.BinaryQuadraticModel(linear, quadratic, 0.0, dimod.BINARY)

sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample(bqm, num_reads=shots)

for res in response.data(['sample', 'energy', 'num_occurrences']):
    print('|x0 = %s |x1 = %s | Energy = %f | Probability  = %f %% ' % (res.sample[1],res.sample[2],
          res.energy, res.num_occurrences*100/shots))
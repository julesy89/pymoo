import numpy as np

from pymoo.algorithms.genetic_algorithm import GeneticAlgorithm
from pymoo.operators.crossover.real_simulated_binary_crossover import SimulatedBinaryCrossover
from pymoo.operators.mutation.real_polynomial_mutation import PolynomialMutation
from pymoo.operators.sampling.real_random_sampling import RealRandomSampling
from pymoo.operators.selection.tournament_selection import TournamentSelection
from pymoo.operators.survival.reference_line_survival import ReferenceLineSurvival


class NSGAIII(GeneticAlgorithm):
    def __init__(self, pop_size=100, verbose=1):

        self.ref_lines = self.create_ref_lines()
        super().__init__(
            pop_size=pop_size,
            sampling=RealRandomSampling(),
            selection=TournamentSelection(),
            crossover=SimulatedBinaryCrossover(),
            mutation=PolynomialMutation(),
            survival=ReferenceLineSurvival(self.ref_lines),
            verbose=verbose)

    def create_ref_lines(self):
        n_refs = 30
        ref_lines = np.array([np.linspace(0, 1, n_refs), np.linspace(1, 0, n_refs).T]).T
        ref_lines -= 1e-50
        ref_lines = ref_lines / np.array([np.linalg.norm(ref_lines, axis=1)]).T
        return ref_lines
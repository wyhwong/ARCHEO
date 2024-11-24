import pandas as pd

from archeo.utils.file import check_and_create_dir
from archeo.visualization.distribution import distribution_summary, kick_against_spin_cmap, kick_distribution_on_spin
from archeo.visualization.estimation import (
    corner_estimates,
    effective_spin_estimates,
    mass_estimates,
    precession_spin_estimates,
    second_generation_probability_curve,
    table_estimates,
)


def visualize_prior_distribution(prior: pd.DataFrame, output_dir: str) -> None:
    """Visualize the prior distribution of the mass, spin, and precession of the black holes.

    Args:
        prior (pd.DataFrame): The prior samples.
        output_dir (str): The directory where the visualizations will be saved.
    """

    check_and_create_dir(output_dir)

    distribution_summary(prior, output_dir=output_dir)
    kick_against_spin_cmap(prior, output_dir=output_dir)
    kick_distribution_on_spin(prior, output_dir=output_dir)


def visualize_posterior_estimation(dfs: dict[str, pd.DataFrame], output_dir: str) -> None:
    """Visualize the posterior estimation of the mass, spin, and precession of the black holes.

    Args:
        dfs (dict[str, pd.DataFrame]): A dictionary of dataframes with the posterior samples.
        output_dir (str): The directory where the visualizations will be saved.
    """

    check_and_create_dir(output_dir)

    for label, df in dfs.items():
        _output_dir = f"{output_dir}/{label}"
        check_and_create_dir(_output_dir)
        mass_estimates(df, label, output_dir=_output_dir)
        corner_estimates({label: df}, output_dir=_output_dir)
        second_generation_probability_curve({label: df}, output_dir=_output_dir)
        effective_spin_estimates({label: df}, output_dir=_output_dir)
        precession_spin_estimates({label: df}, output_dir=_output_dir)

    corner_estimates(dfs, output_dir=output_dir)
    second_generation_probability_curve(dfs, output_dir=output_dir)
    effective_spin_estimates(dfs, output_dir=output_dir)
    precession_spin_estimates(dfs, output_dir=output_dir)
    table_estimates(dfs, output_dir=output_dir)
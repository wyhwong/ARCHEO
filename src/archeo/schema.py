from dataclasses import dataclass

import numpy as np

from archeo.constants import Fits


@dataclass(frozen=True)
class Domain:
    """Domain of a parameter.

    Attributes:
        low (float): Lower bound of the domain
        high (float): Upper bound of the domain
    """

    low: float = float("-inf")
    high: float = float("inf")

    def contain(self, value: float) -> bool:
        """Check if the input value is within the domain."""

        return self.low <= value <= self.high

    def draw(self) -> float:
        """Draw a random value from the domain."""

        return np.random.uniform(low=self.low, high=self.high)


@dataclass(frozen=True)
class Binary:
    """Binary parameters.

    Attributes:
        m_1 (float): Mass of the primary black hole (in solar mass)
        m_2 (float): Mass of the secondary black hole (in solar mass)
        chi_1 (tuple[float, float, float]): Spin of the primary black hole (dimensionless), [0, 1]
        chi_2 (tuple[float, float, float]): Spin of the secondary black hole (dimensionless), [0, 1]
    """

    m_1: float
    m_2: float
    chi_1: tuple[float, float, float]
    chi_2: tuple[float, float, float]


@dataclass(frozen=True)
class Event:
    """Event (Binary Black Hole Merger) parameters."""

    m_1: float
    m_2: float
    m_ret: float
    m_ret_err: float
    v_f: tuple[float, float, float]
    v_f_err: tuple[float, float, float]
    chi_1: tuple[float, float, float]
    chi_2: tuple[float, float, float]
    chi_f: tuple[float, float, float]
    chi_f_err: tuple[float, float, float]


@dataclass(frozen=True)
class PriorConfig:
    """Configuration of the prior.

    Attributes:
        n_samples (int): Number of samples to generate.
        fits (Fits): Surrogate model to use.
        is_spin_aligned (bool): Whether the spins are aligned or not.
        is_only_up_aligned_spin (bool): Whether the spins are only in the positive z-direction.
        spin (Domain): Domain of the spin parameter.
        phi (Domain): Domain of the azimuthal angle of the spin.
        theta (Domain): Domain of the polar angle of the spin.
        mass_ratio (Domain): Domain of the mass ratio.
        mass (Domain): Domain of the mass.
        is_mahapatra (bool): Whether the Mahapatra mass function is used.
    """

    n_samples: int
    fits: Fits
    is_spin_aligned: bool
    is_only_up_aligned_spin: bool
    spin: Domain  # unit: dimensionless
    phi: Domain  # unit: pi
    theta: Domain  # unit: pi
    mass_ratio: Domain  # unit: dimensionless
    mass: Domain  # unit: solar mass
    is_mahapatra: bool

    def __post_init__(self) -> None:
        """Post initialization."""

        if self.fits not in Fits:
            raise ValueError(f"Invalid fits: {self.fits}")

        if self.is_only_up_aligned_spin and not self.is_spin_aligned:
            raise ValueError("Only up-aligned spin is only valid when spins are aligned.")


@dataclass(frozen=True)
class Padding:
    """
    Padding for plot.

    Attributes:
        tpad: float, the top padding of the plot.
        lpad: float, the left padding of the plot.
        bpad: float, the bottom padding of the plot.
    """

    tpad: float = 2.5
    lpad: float = 0.1
    bpad: float = 0.12


@dataclass(frozen=True)
class Labels:
    """
    Labels for plot.

    Attributes:
        title: str, the title of the plot.
        xlabel: str, the x-axis label of the plot.
        ylabel: str, the y-axis label of the plot.
    """

    title: str = ""
    xlabel: str = ""
    ylabel: str = ""

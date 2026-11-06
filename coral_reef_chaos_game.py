"""Coral Reef - Chaos Game using the affine rules from the provided slide.

Requirements:
    Python 3
    matplotlib  (install with: python -m pip install matplotlib)

Run:
    python coral_reef_chaos_game.py

Optional examples:
    python coral_reef_chaos_game.py --iterations 200000
    python coral_reef_chaos_game.py --iterations 200000 --seed 42 --save coral_reef.png
"""

import argparse
import random

import matplotlib.pyplot as plt


# Number of iterations used when no command-line value is provided.
DEFAULT_ITERATIONS = 100_000

# Starting point. The slide does not specify an initial point, so (0, 0)
# is used; the pattern quickly converges to the same attractor.
START_X = 0.0
START_Y = 0.0

# Discard a few initial points so the plotted pattern does not depend on
# the arbitrary starting point.
BURN_IN = 20


def coral_reef_points(iterations, seed=None):
    """Generate x/y coordinates using the three probabilistic rules.

    Probabilities and equations are copied from the provided slide:

      40%: new_x =  0.31*x - 0.53*y + 0.89
           new_y = -0.46*x - 0.29*y + 1.04

      15%: new_x =  0.31*x - 0.08*y + 0.22
           new_y =  0.15*x - 0.45*y + 0.34

      45%: new_x =  0.55*y + 0.01
           new_y =  0.69*x - 0.20*y + 0.38
    """
    if iterations <= 0:
        raise ValueError("iterations must be a positive integer")

    rng = random.Random(seed)
    x, y = START_X, START_Y
    x_points = []
    y_points = []

    for step in range(iterations + BURN_IN):
        choice = rng.random()

        if choice < 0.40:
            # Rule 1 — probability 40%
            new_x = 0.31 * x - 0.53 * y + 0.89
            new_y = -0.46 * x - 0.29 * y + 1.04

        elif choice < 0.55:
            # Rule 2 — probability 15% (0.40 + 0.15)
            new_x = 0.31 * x - 0.08 * y + 0.22
            new_y = 0.15 * x - 0.45 * y + 0.34

        else:
            # Rule 3 — probability 45%
            new_x = 0.55 * y + 0.01
            new_y = 0.69 * x - 0.20 * y + 0.38

        x, y = new_x, new_y

        if step >= BURN_IN:
            x_points.append(x)
            y_points.append(y)

    return x_points, y_points


def main():
    parser = argparse.ArgumentParser(
        description="Draw the Coral Reef chaos game from the three slide equations."
    )
    parser.add_argument(
        "--iterations",
        type=int,
        default=DEFAULT_ITERATIONS,
        help=f"number of plotted points (default: {DEFAULT_ITERATIONS})",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="optional random seed; use the same seed to reproduce the same pattern",
    )
    parser.add_argument(
        "--save",
        type=str,
        default=None,
        help="optional filename for saving the image, e.g. coral_reef.png",
    )
    args = parser.parse_args()

    try:
        x_points, y_points = coral_reef_points(args.iterations, args.seed)
    except ValueError as error:
        parser.error(str(error))

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.scatter(x_points, y_points, s=0.2, color="coral", marker=".", linewidths=0)
    ax.set_title("Coral Reef — Chaos Game", fontsize=14)
    ax.set_aspect("equal", adjustable="datalim")
    ax.axis("off")
    fig.tight_layout()

    if args.save:
        fig.savefig(args.save, dpi=300, bbox_inches="tight")
        print(f"Image saved to: {args.save}")

    plt.show()


if __name__ == "__main__":
    main()

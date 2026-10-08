"""Helpers for sketching the vector function

    v = r_hat / r**2

the inverse-square radial field (Griffiths, Introduction to Electrodynamics,
Sec. 1.2).  This is the prototype for the electric field of a point charge and
the gravitational field of a point mass.

    v(x, y, z) = (x x_hat + y y_hat + z z_hat) / (x**2 + y**2 + z**2)**(3/2)

Its magnitude is |v| = 1 / r**2 and it points radially outward everywhere
(undefined at the origin, where it blows up).

Also provides a retro-neon ("synthwave") plotting theme: a dark palette, a
purple -> magenta -> pink -> orange -> yellow colormap, and a glow helper.
"""

from __future__ import annotations

import numpy as np
from matplotlib import patheffects
from matplotlib.colors import LinearSegmentedColormap


def radial_field(x, y, z, eps: float = 1e-12):
    """Return the components (vx, vy, vz) of v = r_hat / r**2.

    Parameters
    ----------
    x, y, z : array_like
        Cartesian coordinates (any broadcastable shapes).
    eps : float
        Small softening added to r to avoid division by zero at the origin.

    Returns
    -------
    vx, vy, vz : ndarray
        Cartesian components of the field.
    """
    x, y, z = np.asarray(x), np.asarray(y), np.asarray(z)
    r = np.sqrt(x**2 + y**2 + z**2)
    r_safe = r + eps
    # r_hat / r**2 = (x, y, z) / r**3
    inv_r3 = 1.0 / r_safe**3
    return x * inv_r3, y * inv_r3, z * inv_r3


def normalize(vx, vy, vz, eps: float = 1e-12):
    """Return unit vectors and the magnitude, for arrow-direction plotting.

    Because |v| = 1/r**2 spans many orders of magnitude, quiver plots look
    terrible if arrows are drawn to scale.  It is standard (Griffiths does this)
    to draw all arrows the same length and let the *density* / a colormap carry
    the magnitude information.
    """
    vx, vy, vz = np.asarray(vx), np.asarray(vy), np.asarray(vz)
    mag = np.sqrt(vx**2 + vy**2 + vz**2)
    mag_safe = mag + eps
    return vx / mag_safe, vy / mag_safe, vz / mag_safe, mag


# --------------------------------------------------------------------------- #
#  Retro-neon ("synthwave") styling
# --------------------------------------------------------------------------- #

# A nostalgic 1980s neon palette.
NEON = {
    "bg":      "#0d0221",   # near-black deep indigo (figure background)
    "panel":   "#181135",   # slightly lighter panel (axes background)
    "fg":      "#f5e6ff",   # soft off-white foreground text
    "cyan":    "#05d9e8",   # neon cyan
    "pink":    "#ff2a6d",   # hot neon pink
    "magenta": "#d300c5",   # neon magenta
    "purple":  "#7b2ff7",   # electric purple
    "orange":  "#ff9e00",   # sunset orange
    "yellow":  "#f9f871",   # pale neon yellow
    "green":   "#39ff14",   # laser green
}


def neon_cmap():
    """A synthwave-sunset colormap: purple -> magenta -> pink -> neon orange.

    Ends at a saturated orange (not pale yellow) so every value stays clearly
    visible against a *white* background.
    """
    return LinearSegmentedColormap.from_list(
        "synthwave",
        [NEON["purple"], NEON["magenta"], NEON["pink"], NEON["orange"]],
    )


def neon_rcparams():
    """rcParams dict that turns matplotlib into a dark neon theme.

    Use as ``plt.rcParams.update(neon_rcparams())``.  Kept separate from the
    LaTeX-font settings so the two can be combined.
    """
    return {
        "figure.facecolor":  NEON["bg"],
        "savefig.facecolor":  NEON["bg"],
        "axes.facecolor":    NEON["panel"],
        "axes.edgecolor":    NEON["magenta"],
        "axes.labelcolor":   NEON["cyan"],
        "axes.titlecolor":   NEON["pink"],
        "text.color":        NEON["fg"],
        "xtick.color":       NEON["cyan"],
        "ytick.color":       NEON["cyan"],
        "grid.color":        NEON["purple"],
        "grid.alpha":        0.35,
        "axes.grid":         False,
    }


def glow(color, n_layers: int = 6, linewidth: float = 2.2, alpha: float = 0.18):
    """Path-effects list that gives a line/marker a soft neon glow.

    Draws several progressively wider, semi-transparent strokes of ``color``
    underneath the object, then the object itself on top.  Pass to the
    ``path_effects=`` keyword of most matplotlib artists.
    """
    effects = [
        patheffects.Stroke(linewidth=linewidth + i * 2.4, foreground=color, alpha=alpha)
        for i in range(n_layers, 0, -1)
    ]
    effects.append(patheffects.Normal())
    return effects


def style_neon_3d(ax):
    """Apply the dark neon theme to a 3D (mplot3d) axes' panes and grid lines."""
    bg = (0.05, 0.0, 0.13, 1.0)  # NEON['bg'] as RGBA
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.set_pane_color(bg)
        axis.pane.set_edgecolor(NEON["purple"])
        axis.pane.set_alpha(0.9)
        axis._axinfo["grid"]["color"] = NEON["purple"]
        axis._axinfo["grid"]["linewidth"] = 0.6
    ax.set_facecolor(NEON["bg"])

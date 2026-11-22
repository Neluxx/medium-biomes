from beet import Context
from beet.contrib.worldgen import WorldgenNoise

from beet_datapack_utils import resolve_key, targets

# Map of noise name -> first/base octave override.
# The value is written to `firstOctave` (<= 26.2) or `base_octave` (>= 26.3).
NOISE_PATCHES: dict[str, int] = {
    "minecraft:temperature":     -11,  # default -10 / large -12
    "minecraft:erosion":         -10,  # default  -9 / large -11
    "minecraft:vegetation":       -9,  # default  -8 / large -10
    "minecraft:continentalness": -10,  # default  -9 / large -11
}


def beet_default(ctx: Context):
    for target in targets(ctx):
        for name, value in NOISE_PATCHES.items():
            with target.patch(WorldgenNoise, name) as noise:
                noise[resolve_key(noise, "base_octave", "firstOctave")] = value
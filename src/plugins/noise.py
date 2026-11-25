from beet import Context
from beet.contrib.worldgen import WorldgenNoise

from beet_datapack_utils import first_existing_key, versioned_packs

# Map of noise name -> first octave override.
# The value is written to `firstOctave` (before 26.3) or `base_octave` (from 26.3 on).
NOISE_FIRST_OCTAVES: dict[str, int] = {
    "minecraft:temperature":     -11,  # default -10 / large -12
    "minecraft:erosion":         -10,  # default  -9 / large -11
    "minecraft:vegetation":       -9,  # default  -8 / large -10
    "minecraft:continentalness": -10,  # default  -9 / large -11
}


def beet_default(ctx: Context):
    for pack in versioned_packs(ctx):
        for name, first_octave in NOISE_FIRST_OCTAVES.items():
            with pack.edit(WorldgenNoise, name) as noise:
                noise[first_existing_key(noise, "base_octave", "firstOctave")] = first_octave
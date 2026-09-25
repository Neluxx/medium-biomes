from beet import Context, DataPack
from beet.contrib.vanilla import Vanilla
from beet.contrib.worldgen import WorldgenNoise

from src.plugins.utils import iterate_versions, octave_key

# Map of noise name -> firstOctave override.
NOISE_PATCHES: dict[str, int] = {
    "minecraft:temperature":     -11,  # default -10 / large -12
    "minecraft:erosion":         -10,  # default  -9 / large -11
    "minecraft:vegetation":       -9,  # default  -8 / large -10
    "minecraft:continentalness": -10,  # default  -9 / large -11
}


def beet_default(ctx: Context):
    vanilla = ctx.inject(Vanilla)
 
    for pack, version in iterate_versions(ctx):
        source = vanilla.releases[version].mount("data").data[WorldgenNoise]
 
        for name, value in NOISE_PATCHES.items():
            patched = source[name].copy()
            patched.data[octave_key(patched.data)] = value
            pack[WorldgenNoise][name] = patched


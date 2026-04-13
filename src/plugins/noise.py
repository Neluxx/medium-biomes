from beet import Context, DataPack
from beet.contrib.vanilla import Vanilla
from beet.contrib.worldgen import WorldgenNoise

from src.plugins.utils import iterate_versions

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
        for name, value in NOISE_PATCHES.items():
            source = vanilla.releases[version].mount("data").data[WorldgenNoise]
            patched = source[name].copy()
            patched.data["firstOctave"] = value
            pack[WorldgenNoise][name] = patched

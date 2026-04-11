from beet import Context, DataPack
from beet.contrib.vanilla import Vanilla
from beet.contrib.worldgen import WorldgenNoise

# Map of noise name -> firstOctave override.
NOISE_PATCHES: dict[str, int] = {
    "minecraft:temperature":     -11,  # default -10 / large -12
    "minecraft:erosion":         -10,  # default  -9 / large -11
    "minecraft:vegetation":       -9,  # default  -8 / large -10
    "minecraft:continentalness": -10,  # default  -9 / large -11
}


def beet_default(ctx: Context):
    source = get_source(ctx.inject(Vanilla), ctx.meta["base_version"])
    apply_patch(ctx.data, source)


def get_source(vanilla: Vanilla, version: str):
    return vanilla.releases[version].mount("data").data[WorldgenNoise]


def apply_patch(pack: DataPack, source):
    for name, first_octave in NOISE_PATCHES.items():
        patched = source[name].copy()
        patched.data["firstOctave"] = first_octave
        pack[WorldgenNoise][name] = patched

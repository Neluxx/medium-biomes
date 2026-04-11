from beet import Context, DataPack
from beet.contrib.vanilla import Vanilla
from beet.contrib.worldgen import WorldgenNoise

TEMPERATURE = "minecraft:temperature"
TEMPERATURE_FIRST_OCTAVE = -11  # defaults to -10 or -12 for large biomes
EROSION = "minecraft:erosion"
EROSION_FIRST_OCTAVE = -10  # defaults to -9 or -11 for large biomes
VEGETATION = "minecraft:vegetation"
VEGETATION_FIRST_OCTAVE = -9  # defaults to -8 or -10 for large biomes
CONTINENTALNESS = "minecraft:continentalness"
CONTINENTALNESS_FIRST_OCTAVE = -10  # defaults to -9 or -11 for large biomes


def beet_default(ctx: Context):
    source = get_source(ctx.inject(Vanilla), ctx.meta["base_version"])
    apply_patch(ctx.data, source)


def get_source(vanilla: Vanilla, version: str):
    return vanilla.releases[version].mount("data").data[WorldgenNoise]


def apply_patch(pack: DataPack, source):
    patched = source[TEMPERATURE].copy()
    patched.data["firstOctave"] = TEMPERATURE_FIRST_OCTAVE
    pack[WorldgenNoise][TEMPERATURE] = patched

    patched = source[EROSION].copy()
    patched.data["firstOctave"] = EROSION_FIRST_OCTAVE
    pack[WorldgenNoise][EROSION] = patched

    patched = source[VEGETATION].copy()
    patched.data["firstOctave"] = VEGETATION_FIRST_OCTAVE
    pack[WorldgenNoise][VEGETATION] = patched

    patched = source[CONTINENTALNESS].copy()
    patched.data["firstOctave"] = CONTINENTALNESS_FIRST_OCTAVE
    pack[WorldgenNoise][CONTINENTALNESS] = patched

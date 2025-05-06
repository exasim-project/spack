# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Neofoam(CMakePackage):
    """NeoFOAM is a WIP prototype of a modern CFD core."""

    license("GPL-3.0-or-later")

    homepage = "https://github.com/exasim-project/NeoFOAM"
    git = "https://github.com/exasim-project/FoamAdapter.git"

    maintainers("greole", "HenningScheufler")

    version("main", branch="main")

    variant("test", default=False, description="")
    variant("examples", default=True, description="")
    variant("benchmarks", default=False, description="")
    variant("cuda", default=False, description="Compile with CUDA support")
    variant("hip", default=False, description="Compile with HIP support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("neon")
    depends_on("openfoam")

    def cmake_args(self):
        return [
            self.define_from_variant("FOAMADAPTER_BUILD_TESTS", "test"),
            self.define_from_variant("FOAMADAPTER_BUILD_EXAMPLES", "examples"),
            self.define_from_variant("FOAMADAPTER_BUILD_BENCHMARKS", "benchmarks"),
            self.define_from_variant("Kokkos_ENABLE_CUDA", "cuda"),
            self.define_from_variant("Kokkos_ENABLE_HIP", "hip"),
        ]

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

    variant("cuda", default=False, description="Compile with CUDA support")
    variant("hip", default=False, description="Compile with HIP support")
    variant("test", default=False, description="")
    variant("examples", default=False, description="")
    variant("benchmarks", default=False, description="")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("neon")
    depends_on("openfoam")

    def cmake_args(self):
        return [
            '-DFOAMADAPTER_BUILD_TESTS=%s' % ('+test' in self.spec),
            '-DFOAMADAPTER_BUILD_EXAMPLES=%s' % ('+examples' in self.spec),
            '-DFOAMADAPTER_BUILD_BENCHMARKS=%s' % ('+benchmarks' in self.spec),
            '-DKokkos_ENABLE_CUDA=%s' % ('+cuda' in self.spec),
            '-DKokkos_ENABLE_HIP=%s' % ('+hip' in self.spec),
        ]

from conan import ConanFile


class xepocsRecipe(ConanFile):
    name = "xepocs"
    version = "0.1.0"  # version file (source of truth)
    python_requires = "xenoide-base/0.1.1"
    python_requires_extend = "xenoide-base.XenoideCMake"
    package_type = "application"
    build_info_prefix = "XE"

    license = "MIT"
    author = "Felipe Apablaza <felipe.apablaza@protonmail.com>"
    url = "https://github.com/XenoideSoftware/xenoide-pocs"
    description = "Proof of concepts for the Xenoide project"
    topics = ("ide", "game-engine", "graphics")

    options = {
        "with_poc_clang": [True, False],
        "with_poc_lsp": [True, False],
        "with_poc_protobuf": [True, False],
        "with_poc_wxwidgets": [True, False],
        "with_poc_zeromq": [True, False],
    }

    default_options = {
        # LLVM Debug builds are ~4400 steps and tens of GB; keep the POC off
        # unless explicitly requested (build LLVM in Release first).
        "with_poc_clang": False,
        "with_poc_lsp": True,
        "with_poc_protobuf": True,
        "with_poc_wxwidgets": False,
        "with_poc_zeromq": True,
    }

    def configure(self):
        # lsp-framework uses C++20 concepts; the POC project follows it.
        self.settings.compiler.cppstd = "20"

    def init(self):
        super().init()
        self.options.with_tests = False

    exports_sources = "CMakeLists.txt", "src/*"

    def requirements(self):
        if self.options.get_safe("with_poc_clang"):
            self.requires("llvm/18.1.8")

        if self.options.get_safe("with_poc_lsp"):
            self.requires("lsp-framework/1.3.1")

        if self.options.get_safe("with_poc_protobuf"):
            self.requires("protobuf/3.9.1")

        if self.options.get_safe("with_poc_zeromq"):
            # cppzmq is the maintained C++ binding; zmqpp has no recipe and
            # was only ever installed out-of-band.
            self.requires("cppzmq/4.11.0")

    def xenoide_toolchain(self, tc):
        for option, variable in (
            ("with_poc_clang", "XE_ENABLE_POC_CLANG"),
            ("with_poc_lsp", "XE_ENABLE_POC_LSP"),
            ("with_poc_protobuf", "XE_ENABLE_POC_PROTOBUF"),
            ("with_poc_wxwidgets", "XE_ENABLE_POC_WXWIDGETS"),
            ("with_poc_zeromq", "XE_ENABLE_POC_ZEROMQ"),
        ):
            tc.variables[variable] = "ON" if self.options.get_safe(option) else "OFF"

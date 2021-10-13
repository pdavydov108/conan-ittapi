from conans import ConanFile, tools, AutoToolsBuildEnvironment, CMake


class Libittapi(ConanFile):
    name = "ittapi"
    version = "3.21.2"
    license = "https://github.com/intel/ittapi/tree/master/LICENSES"
    author = "Pavel Davydov pdavydov108@gmail.com"
    url = "https://github.com/intel/ittapi"
    description = "Conan package for ittapi."
    settings = "os", "compiler", "arch"
    generators = "cmake"

    def source(self):
        git = tools.Git()
        git.clone(self.url, 'master')

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h")
        self.copy("*.a", src="bin", dst='lib')

    def package_info(self):
        self.cpp_info.libs = ["ittnotify"]

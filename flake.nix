{
  description = "flake gitomezashi";

  outputs = { self, nixpkgs }:
    let pkgs = import nixpkgs { system = "x86_64-linux"; };
    in {
      packages.x86_64-linux.gitomezashi = with pkgs;
        python38Packages.buildPythonPackage rec {
          name = "gitomezashi";
          version = "0.1";
          src = ./.;
          propagatedBuildInputs = with python38Packages;
            [
              # requests
              GitPython
              svgwrite
              cairosvg
            ];
          doCheck = false;
        };

      defaultPackage.x86_64-linux = self.packages.x86_64-linux.gitomezashi;
    };
}

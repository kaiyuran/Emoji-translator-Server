with import <nixpkgs> {};

mkShell {
  buildInputs = [
    python3
    python3Packages.flask
    python3Packages.flask-cors
    python3Packages.gunicorn
  ];

  shellHook = ''
    export LANG=C.UTF-8
    export LC_ALL=C.UTF-8
  '';
}
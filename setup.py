import cx_Freeze

executables = [cx_Freeze.Executable(
    script="jogo.py",
    icon="assets/sonicIcon.ico"
)]
cx_Freeze.setup(
    name="Sonic",
    options={
        "build_exe":{"packages":["pygame"],
        "include_files":["assets"]
        }}
    ,executables = executables
)
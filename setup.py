from cx_Freeze import setup, Executable

setup(name = "Jogo Sonic" ,
	version = "1.0" ,
    icon="assets/sonicIcon.ico",
	options={
        "build_exe":{"packages":["pygame"],
        "include_files":["assets"]
        }},
	description = "Esse foi um projeto criado pelos alunos Henrique Tres Terra e Vinicius Artuso da instituição ATITUS, Passo Fundo" ,
	executables = [Executable("jogo.py")])
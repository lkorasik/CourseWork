(* ::Package:: *)

BeginPackage["ExternalLanguages`"];

	LoadFunction::usage = "Load function from julia or python code"
	LoadFile::usage = "Load file"
	GetPythonDirectory::usage = "Get directory where Python code placed"
	GetJuliaDirectory::usage = "Get directory where Julia code placed"
	StartPython::usage = "Start python session"
	StartJulia::usage = "Start julia session"

	$GetCodeDirectory::usage = "Get directory where code placed"

Begin["Public`"];
	LoadFunction[session_, name_] := (Return[ExternalFunction[session, name]];);

	LoadFile[folder_, filename_, session_] := (
        path = folder <> "\\" <> filename;
        evaluator = ExternalEvaluate[session, File[path]];
        Return[evaluator];
    );

	$GetCodeDirectory[language_] := (
        directory = NotebookDirectory[];
        directory = ParentDirectory[directory];
        directory = directory <> "\\" <> language;
        Return[directory];
    );

	GetPythonDirectory[] := Return[$GetCodeDirectory["python"]];
	GetJuliaDirectory[] := Return[$GetCodeDirectory["julia"]];

	StartPython[] := Return[StartExternalSession["Python"]];

	StartJulia[] := Return[StartExternalSession["Julia"]];
End[];

EndPackage[];

(*
(*\:041e\:0447\:0438\:0441\:0442\:043a\:0430 \:0438\:043c\:0435\:043d*)
Clear["Global`*"];
<< "C:\\Files\\Study\\CourseWork\\code\\mathematica\\Utils.wl"
*)

(*
(*Python example*)
python = StartPython[];
LoadFile[GetPythonDirectory[], "functions.py", python];

f = LoadFunction[python, "f"];
f[3]

g = LoadFunction[python, "g"];
g[3]

DeleteObject[python];
*)

(*
(*Julia example*)
julia = StartJulia[];
LoadFile[GetPythonDirectory[], "functions.jl", julia];

f = LoadFunction[julia, "f"];
f[3]

g = LoadFunction[julia, "g"];
g[3]

DeleteObject[julia];
*)

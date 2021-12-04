(* ::Package:: *)

BeginPackage["Utils`"];
SaveGraphic::usage = "Plot graphic and save it"
Begin["Public`"];
	SaveGraphic[f_, g_, a_, b_, filename_] := (
		result = Solve[f[a, x]==g[b, x], x, Reals];
		answer = {};
		If[result=={}, answer = {}, answer = {x, f[a, x]} /. result];
		fig = Plot[
			{f[a,x], g[b, x]}, 
			{x, -1, 1}, 
			PlotLegends -> {"\[Alpha]*x", "(\[Beta]+x)^6"},
			PlotRange -> {{-0.02, 0.21}, {-0.02, 0.21}},
			PlotStyle -> {Darker[Green], Blue},
			ImageSize -> Large,
			AxesLabel -> {Style["x", Bold, 20], Style["y", Bold, 20]},
			TicksStyle -> Directive[FontSize -> 16],
			Epilog -> {Red, PointSize -> Large, Point[answer]}
		];
		Export[filename, fig, OverwriteTarget->True];
	)
End[];
EndPackage[];

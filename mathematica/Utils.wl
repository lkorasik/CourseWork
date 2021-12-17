(* ::Package:: *)

BeginPackage["Utils`"];
PlotAndSaveSolutionGraphic::usage = "Plot graphic of equation solution and save it"
PlotAndSaveTimeSeries::usage = "Plot and save time range grpahic"
PlotAndSaveBifurcation::usage = "Plot and save bifurcation graphic"
Begin["Public`"];
	(*\:0424\:0443\:043d\:043a\:0446\:0438\:044f \:0434\:043b\:044f \:043e\:0442\:0440\:0438\:0441\:043e\:0432\:043a\:0438 \:0433\:0440\:0430\:0444\:0438\:043a\:043e\:0432 \:0444\:0443\:043d\:043a\:0446\:0438\:0439 y=ax \:0438 y=(b+x)^6*)
	PlotAndSaveSolutionGraphic[f_, g_, a_, b_, filename_] := (
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
		Export[filename, fig, OverwriteTarget -> True];
	);
	
	(*\:041d\:0430\:0440\:0438\:0441\:043e\:0432\:0430\:0442\:044c \:0433\:0440\:0430\:0444\:0438\:043a \:0432\:0440\:0435\:043c\:0435\:043d\:043d\:043e\:0433\:043e \:0440\:044f\:0434\:0430*)
	PlotAndSaveTimeSeries[xs_, timeRange_, filename_] := (
		timeRangeList = List[timeRange];
		fig = ListLinePlot[
			TimeSeries[xs, List[timeRangeList]], 
			PlotRange -> {-0.1, 0.41}
		];
		Export[filename, fig, OverwriteTarget -> True];
	);
	
	(*\:041d\:0430\:0440\:0438\:0441\:043e\:0432\:0430\:0442\:044c \:0433\:0440\:0430\:0444\:0438\:043a \:0431\:0438\:0444\:0443\:0440\:043a\:0430\:0446\:0438\:0438*)
	PlotAndSaveBifurcation[drawX_, drawY_, filename_]:=(
		src = Transpose[{drawX,drawY}];
		fig = ListPlot[src, 
			ScalingFunctions -> {"Reciprocal", "Log"}
		];
		Export[filename, fig, OverwriteTarget -> True];
	)
End[];
EndPackage[];

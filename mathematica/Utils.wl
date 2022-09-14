(* ::Package:: *)

BeginPackage["Utils`"];
	PlotAndSaveSolutionGraphic::usage = "\:041d\:0430\:0440\:0438\:0441\:043e\:0432\:0430\:0442\:044c \:0438 \:0441\:043e\:0445\:0440\:0430\:043d\:0438\:0442\:044c \:0433\:0440\:0430\:0444\:0438\:043a \:0444\:0443\:043d\:043a\:0446\:0438\:0439"
	PlotAndSaveTimeSeries::usage = "\:041d\:0430\:0440\:0438\:0441\:043e\:0432\:0430\:0442\:044c \:0438 \:0441\:043e\:0445\:0440\:0430\:043d\:0438\:0442\:044c \:0433\:0440\:0430\:0444\:0438\:043a \:0432\:0440\:0435\:043c\:0435\:043d\:043d\:043e\:0433\:043e \:0440\:044f\:0434\:0430"
	PlotAndSaveBifurcation::usage = "\:041d\:0430\:0440\:0438\:0441\:043e\:0432\:0430\:0442\:044c \:0438 \:0441\:043e\:0445\:0440\:0430\:043d\:0438\:0442\:044c \:0433\:0440\:0430\:0444\:0438\:043a \:0431\:0438\:0444\:0443\:0440\:043a\:0430\:0446\:0438\:0438"
	PlotAndSaveBifurcationWithChaos::usage = "\:041d\:0430\:0440\:0438\:0441\:043e\:0432\:0430\:0442\:044c \:0438 \:0441\:043e\:0445\:0440\:0430\:043d\:0438\:0442\:044c \:0433\:0440\:0430\:0444\:0438\:043a \:0431\:0438\:0444\:0443\:0440\:043a\:0430\:0446\:0438\:0438 \:0441 \:0433\:0440\:0430\:043d\:0438\:0446\:0430\:043c\:0438 \:0445\:0430\:043e\:0441\:0430"

Begin["Public`"];
	(*\:0421\:043e\:0445\:0440\:0430\:043d\:0438\:0442\:044c \:0433\:0440\:0430\:0444\:0438\:043a \:0432 \:0444\:0430\:0439\:043b*)
	Private$SaveGraphic[filename_, figure_] := (
		Export[filename, figure, OverwriteTarget -> True];
	);
	
	(*\:0424\:0443\:043d\:043a\:0446\:0438\:044f \:0434\:043b\:044f \:043e\:0442\:0440\:0438\:0441\:043e\:0432\:043a\:0438 \:0433\:0440\:0430\:0444\:0438\:043a\:043e\:0432 \:0444\:0443\:043d\:043a\:0446\:0438\:0439 y=ax \:0438 y=(b+x)^6*)
	PlotAndSaveSolutionGraphic[f_, g_, a_, b_, filename_] := (
		result = Solve[f[a, x]==g[b, x], x, Reals];
		answer = {};
		If[result=={}, answer = {}, answer = {x, f[a, x]} /. result];
		fig = Plot[
			{f[a,x], g[b, x]}, 
			{x, -1, 1}, 
			PlotLegends -> {"\[Alpha]x", "(\[Beta]+x)^6"},
			PlotRange -> {{-0.02, 0.21}, {-0.02, 0.21}},
			PlotStyle -> {Darker[Green], Blue},
			ImageSize -> Large,
			AxesLabel -> {Style["x", Bold, 20], Style["y", Bold, 20]},
			TicksStyle -> Directive[FontSize -> 16],
			Epilog -> {Red, PointSize -> Large, Point[answer]}
		];
		Private$SaveGraphic[filename, fig];
	);
	
	(*\:041d\:0430\:0440\:0438\:0441\:043e\:0432\:0430\:0442\:044c \:0433\:0440\:0430\:0444\:0438\:043a \:0432\:0440\:0435\:043c\:0435\:043d\:043d\:043e\:0433\:043e \:0440\:044f\:0434\:0430*)
	PlotAndSaveTimeSeries[xs_, timeRange_, filename_] := (
		timeRangeList = List[timeRange];
		fig = ListLinePlot[
			TimeSeries[xs, List[timeRangeList]], 
			PlotRange -> {0, 0.41},
			ImageSize -> Large,
			AxesLabel -> {Style["t", 20], Style["x", 20]},
			TicksStyle -> Directive[FontSize -> 16]
		];
		Private$SaveGraphic[filename, fig];
	);
	
	(*\:041d\:0430\:0440\:0438\:0441\:043e\:0432\:0430\:0442\:044c \:0433\:0440\:0430\:0444\:0438\:043a \:0431\:0438\:0444\:0443\:0440\:043a\:0430\:0446\:0438\:0438*)
	PlotAndSaveBifurcation[drawX_, drawY_, filename_]:=(
		src = Transpose[{drawX, drawY}];
		fig = ListPlot[
			src, 
			ScalingFunctions -> {"Linear", "Log"},
			ImageSize -> Large,
			PlotMarkers -> {Automatic, Tiny},
			AxesLabel -> {Style["\[Beta]", 20], Style["x", 20]}
		];
		Private$SaveGraphic[filename, fig];
	)
	
	(*\:041d\:0430\:0440\:0438\:0441\:043e\:0432\:0430\:0442\:044c \:0433\:0440\:0430\:0444\:0438\:043a \:0431\:0438\:0444\:0443\:0440\:043a\:0430\:0446\:0438\:0438*)
	PlotAndSaveBifurcationWithChaos[drawX_, drawY_, line1X_, line1Y_, line2X_, line2Y_, filename_]:=(
		src = Transpose[{drawX, drawY}];
		fig1 = ListPlot[
			src, 
			ScalingFunctions -> {"Linear", "Log"},
			ImageSize -> Large,
			PlotMarkers -> {Automatic, Tiny},
			AxesLabel -> {Style["\[Beta]", 20], Style["x", 20]}
		];
		src = Transpose[{line1X, line1Y}];
		fig2 = ListPlot[
			src, 
			ScalingFunctions -> {"Linear", "Log"},
			ImageSize -> Large,
			PlotMarkers -> {Automatic, Tiny},
			AxesLabel -> {Style["\[Beta]", 20], Style["x", 20]},
			PlotStyle->Red
		];
		src = Transpose[{line2X, line2Y}];
		fig3 = ListPlot[
			src, 
			ScalingFunctions -> {"Linear", "Log"},
			ImageSize -> Large,
			PlotMarkers -> {Automatic, Tiny},
			AxesLabel -> {Style["\[Beta]", 20], Style["x", 20]},
			PlotStyle->Red
		];
		fig = Show[fig1, fig2, fig3];
		Private$SaveGraphic[filename, fig];
	)
End[];
EndPackage[];

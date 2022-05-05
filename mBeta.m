basePath = "C:\\Users\\lkora\\Desktop\\data\\";
aNoise = strcat(basePath, "a_noise\\");
bNoise = strcat(basePath, "b_noise\\");
additiveNoise = strcat(basePath, "additive_noise\\");

% size = 8;
% 
% names = [];
% for i = 1:size
%     fileNumber = int2str(i);
%     name = strcat("line", fileNumber, ".txt");
%     names = [names, name];
% end

aNoise_line0 = load(strcat(aNoise, "line0.txt"));
aNoise_line1 = load(strcat(aNoise, "line1.txt"));
aNoise_line2 = load(strcat(aNoise, "line2.txt"));
aNoise_line3 = load(strcat(aNoise, "line3.txt"));
aNoise_line4 = load(strcat(aNoise, "line4.txt"));
aNoise_line5 = load(strcat(aNoise, "line5.txt"));
aNoise_line6 = load(strcat(aNoise, "line6.txt"));
aNoise_line7 = load(strcat(aNoise, "line7.txt"));
aNoise_line8 = load(strcat(aNoise, "line8.txt"));

bNoise_line0 = load(strcat(bNoise, "line0.txt"));
bNoise_line1 = load(strcat(bNoise, "line1.txt"));
bNoise_line2 = load(strcat(bNoise, "line2.txt"));
bNoise_line3 = load(strcat(bNoise, "line3.txt"));
bNoise_line4 = load(strcat(bNoise, "line4.txt"));
bNoise_line5 = load(strcat(bNoise, "line5.txt"));
bNoise_line6 = load(strcat(bNoise, "line6.txt"));
bNoise_line7 = load(strcat(bNoise, "line7.txt"));
bNoise_line8 = load(strcat(bNoise, "line8.txt"));

additiveNoise_line0 = load(strcat(additiveNoise, "line0.txt"));
additiveNoise_line1 = load(strcat(additiveNoise, "line1.txt"));
additiveNoise_line2 = load(strcat(additiveNoise, "line2.txt"));
additiveNoise_line3 = load(strcat(additiveNoise, "line3.txt"));
additiveNoise_line4 = load(strcat(additiveNoise, "line4.txt"));
additiveNoise_line5 = load(strcat(additiveNoise, "line5.txt"));
additiveNoise_line6 = load(strcat(additiveNoise, "line6.txt"));
additiveNoise_line7 = load(strcat(additiveNoise, "line7.txt"));
additiveNoise_line8 = load(strcat(additiveNoise, "line8.txt"));

hold on
plot(aNoise_line0(:, 1), aNoise_line0(:, 2), '.', 'Color', [000/255, 000/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'a line 0');
plot(aNoise_line1(:, 1), aNoise_line1(:, 2), '.', 'Color', [020/255, 000/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'a line 1');
plot(aNoise_line2(:, 1), aNoise_line2(:, 2), '.', 'Color', [040/255, 000/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'a line 2');
plot(aNoise_line3(:, 1), aNoise_line3(:, 2), '.', 'Color', [060/255, 000/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'a line 3');
plot(aNoise_line4(:, 1), aNoise_line4(:, 2), '.', 'Color', [080/255, 000/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'a line 4');
plot(aNoise_line5(:, 1), aNoise_line5(:, 2), '.', 'Color', [100/255, 000/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'a line 5');
plot(aNoise_line6(:, 1), aNoise_line6(:, 2), '.', 'Color', [120/255, 000/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'a line 6');
plot(aNoise_line7(:, 1), aNoise_line7(:, 2), '.', 'Color', [140/255, 000/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'a line 7');
plot(aNoise_line8(:, 1), aNoise_line8(:, 2), '.', 'Color', [160/255, 000/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'a line 8');

plot(bNoise_line0(:, 1), bNoise_line0(:, 2), '.', 'Color', [020/255, 060/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'b line 0');
plot(bNoise_line1(:, 1), bNoise_line1(:, 2), '.', 'Color', [040/255, 060/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'b line 1');
plot(bNoise_line2(:, 1), bNoise_line2(:, 2), '.', 'Color', [060/255, 060/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'b line 2');
plot(bNoise_line3(:, 1), bNoise_line3(:, 2), '.', 'Color', [080/255, 060/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'b line 3');
plot(bNoise_line4(:, 1), bNoise_line4(:, 2), '.', 'Color', [100/255, 060/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'b line 4');
plot(bNoise_line5(:, 1), bNoise_line5(:, 2), '.', 'Color', [120/255, 060/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'b line 5');
plot(bNoise_line6(:, 1), bNoise_line6(:, 2), '.', 'Color', [140/255, 060/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'b line 6');
plot(bNoise_line7(:, 1), bNoise_line7(:, 2), '.', 'Color', [160/255, 060/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'b line 7');
plot(bNoise_line8(:, 1), bNoise_line8(:, 2), '.', 'Color', [180/255, 060/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'b line 8');

plot(additiveNoise_line0(:, 1), additiveNoise_line0(:, 2), '.', 'Color', [000/255, 120/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'additive line 0');
plot(additiveNoise_line1(:, 1), additiveNoise_line1(:, 2), '.', 'Color', [020/255, 120/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'additive line 0');
plot(additiveNoise_line2(:, 1), additiveNoise_line2(:, 2), '.', 'Color', [040/255, 120/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'additive line 0');
plot(additiveNoise_line3(:, 1), additiveNoise_line3(:, 2), '.', 'Color', [060/255, 120/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'additive line 0');
plot(additiveNoise_line4(:, 1), additiveNoise_line4(:, 2), '.', 'Color', [080/255, 120/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'additive line 0');
plot(additiveNoise_line5(:, 1), additiveNoise_line5(:, 2), '.', 'Color', [100/255, 120/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'additive line 0');
plot(additiveNoise_line6(:, 1), additiveNoise_line6(:, 2), '.', 'Color', [120/255, 120/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'additive line 0');
plot(additiveNoise_line7(:, 1), additiveNoise_line7(:, 2), '.', 'Color', [140/255, 120/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'additive line 0');
plot(additiveNoise_line8(:, 1), additiveNoise_line8(:, 2), '.', 'Color', [160/255, 0/255, 000/255], 'MarkerSize', 20, 'DisplayName', 'additive line 0');
hold off

legend('show','Location','southeastoutside');
path = "C:\Users\lkora\Desktop\data\";

suffix = "x";

peq_x=load(path + 'eqX2Gt2X1_' + suffix + '.txt'); %равновесие
peq1_x=load(path + 'eqX2Lt2X1_'  + suffix + '.txt'); %равновесие

markersize = 10;

%pinf=load('C:\Таня\_Прога Дискр Стох\inf.txt');
c2_x=load(path + 'cycle2_' + suffix + '.txt'); %циклы
c3_x=load(path + 'cycle3_' + suffix + '.txt');
c4_x=load(path + 'cycle4_' + suffix + '.txt');
c5_x=load(path + 'cycle5_' + suffix + '.txt');
c6_x=load(path + 'cycle6_' + suffix + '.txt');
c7_x=load(path + 'cycle7_' + suffix + '.txt');
c8_x=load(path + 'cycle8_' + suffix + '.txt');
c9_x=load(path + 'cycle9_' + suffix + '.txt');
c10_x=load(path + 'cycle10_' + suffix + '.txt');
%c11_x=load(path + 'cycle11_' + suffix + '.txt');
%c12_x=load(path + 'cycle12_' + suffix + '.txt');
%c13_x=load(path + 'cycle13_' + suffix + '.txt');
%c14_x=load(path + 'cycle14_' + suffix + '.txt');
%c15_x=load(path + 'cycle15_' + suffix + '.txt');

plot(peq_x(:,1),peq_x(:,2),'.','Color',[201/255,242/255,242/255],'MarkerSize',markersize,'DisplayName','eq1')
hold on
plot(peq1_x(:,1),peq1_x(:,2),'.','Color',[193/255,222/255,198/255],'MarkerSize',markersize,'DisplayName','eq2')

%plot(pinf(:,1),pinf(:,2),'.','Color',[204/255,204/255,204/255],'MarkerSize',markersize,'DisplayName','inf')
plot(c2_x(:,1),c2_x(:,2),'.','Color',[76/255,102/255,0/255],'MarkerSize',markersize,'DisplayName','2');
plot(c3_x(:,1),c3_x(:,2),'.','Color',[255/255,0/255,0/255],'MarkerSize',markersize,'DisplayName','3');
plot(c4_x(:,1),c4_x(:,2),'.','Color',[114/255,153/255,0/255],'MarkerSize',markersize,'DisplayName','4')
plot(c5_x(:,1),c5_x(:,2),'.','Color',[134/255,18/255,252/255],'MarkerSize',markersize,'DisplayName','5')
plot(c6_x(:,1),c6_x(:,2),'.','Color',[250/255,145/255,145/255],'MarkerSize',markersize,'DisplayName','6')
plot(c7_x(:,1),c7_x(:,2),'.','Color',[128/255,116/255,98/255],'MarkerSize',markersize,'DisplayName','7')
plot(c8_x(:,1),c8_x(:,2),'.','Color',[0/255,255/255,0/255],'MarkerSize',markersize,'DisplayName','8')
plot(c9_x(:,1),c9_x(:,2),'.','Color',[127/255,0/255,128/255],'MarkerSize',markersize,'DisplayName','9')
plot(c10_x(:,1),c10_x(:,2),'.','Color',[126/255,127/255,247/255],'MarkerSize',markersize,'DisplayName','10')
%plot(c11_x(:,1),c11_x(:,2),'.','Color',[0/255,1/255,255/255],'MarkerSize',markersize,'DisplayName','11')
%plot(c12_x(:,1),c12_x(:,2),'.','Color',[168/255,2/255,168/255],'MarkerSize',markersize,'DisplayName','12')
%plot(c13_x(:,1),c13_x(:,2),'.','Color',[0/255,253/255,255/255],'MarkerSize',markersize,'DisplayName','13')
%plot(c14_x(:,1),c14_x(:,2),'.','Color',[254/255,255/255,0/255],'MarkerSize',markersize,'DisplayName','14')
%plot(c15_x(:,1),c15_x(:,2),'.','Color',[120/255,55/255,219/255],'MarkerSize',markersize,'DisplayName','15')

legend('show','Location','southeastoutside');
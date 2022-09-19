time_range = 1:50;
x_start = 0.1;
y_start = 2.2;
skip = false;

a = 0.1;
b = 1.5;
g = 0.8;

line_x = [x_start];
line_y = [y_start];

x_i = x_start;
y_i = y_start;
if skip
    for i = time_range
        nx = f1(a, b, g, x_i, y_i);
        ny = f2(a, b, g, x_i, y_i);
        x_i = nx;
        y_i = ny;
    end
end
for i = time_range
    nx = f1(a, b, g, x_i, y_i);
    ny = f2(a, b, g, x_i, y_i);
    x_i = nx;
    y_i = ny;
    line_x = [line_x, x_i];
    line_y = [line_y, y_i];
end

plot(line_x, line_y);

function [result] = f1(a, b, g, x, y)
    result = (a*x^2) / ((b + x)^6) - g * x * y;
end

function [result] = f2(a, b, g, x, y)
    result = y + g * y * (x - y);
end

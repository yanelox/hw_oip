close all
clear variables

lambdaPr = 656.28; %нм
speedOfLight = 299792.458; %км/c

spectra = importdata ("spectra.csv"); 
lambdaStart = importdata ("lambda_start.csv");
lambdaDelta = importdata ("lambda_delta.csv");
starNames = importdata ("star_names.csv");

number_of_measurements = size (spectra, 1)

number_of_stars = size (spectra, 2)

lambda_end = lambdaStart + (number_of_measurements - 1) * lambdaDelta
lambda = (lambdaStart : lambdaDelta : lambda_end)'

[min_spectras, i_min_spectras] = min(spectra);
i_min_spectras = i_min_spectras'
min_spectras = min_spectras'

z = lambda (i_min_spectras) / lambdaPr - 1

speed = z * speedOfLight % Скорость звезд в м/с

movaway = starNames (z > 0)

fg1 = figure;

xlabel ('Длина волны, нм');
ylabel (['Интенсивность звезд, эрг/см^2/c/', char (197)]);
title ('Спектр звезд');

set (fg1, 'Position', [0, 0, 1000, 1000])

grid on

hold on
for i = 1: 1 : number_of_stars
    if (z(i) >  0)
        plot (lambda, spectra (:, i),'r', 'LineWidth', 3, 'Color', [rand, rand, rand])
    else
        plot (lambda, spectra (:, i), "b--", 'LineWidth', 1, 'Color', [rand, rand, rand])
    end
end

legend (starNames)

text (635, 2 * 10^(-13), "Радькин Кирилл Б01-005")

hold off

saveas (fg1, "spectry.png")

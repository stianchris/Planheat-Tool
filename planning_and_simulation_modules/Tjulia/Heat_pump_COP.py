# -*- coding: utf-8 -*-
"""
Created on Wed May 23 13:17:20 2018

@author: hrvoj
"""
import numpy as np
import os
import os.path



def generate_fileEta_forJulia(val_list, input_folder="", output_folder=""):

    if val_list is None:
        return

    # Only for testing
    if input_folder == "":
        input_folder = "C:\\Users\\qgis1\\AppData\\Roaming\\QGIS\\QGIS3\\profiles\\default\\python\\plugins\\planning_module\\Tjulia\\single_building"
    if output_folder == "":
        output_folder = "C:\\Users\\qgis1\\AppData\\Roaming\\QGIS\\QGIS3\\profiles\\default\\python\\plugins\\planning_module\\Tjulia\\single_building\\input"

    # Load meteorological data
    # print("etaHP: print di alcune folders per vedere quale sarebbe quella corretta")
    # print(os.path.realpath(os.path.join(input_folder)))
    # print(os.path.realpath(os.path.join(input_folder, "Outside_temperature.csv")))
    # print(os.path.realpath(os.path.join(input_folder, "../", "Outside_temperature.csv")))
    # print(os.path.realpath(os.path.join(input_folder, "./", "Outside_temperature.csv")))
    try:
        T_source_1 = np.genfromtxt(input_folder + "\\T_source_HP.csv")
    except OSError:
        T_source_1 = np.genfromtxt(os.path.realpath(os.path.join(input_folder, "Outside_temperature.csv")))
    T_source_1 = T_source_1+273.15
    # Heat sink temperature [°C]
    T_sink = val_list[0]
    T_sink_1 = T_sink +273.15
    # Lorenz efficiency
    eta_Lorentz_1 = 0.6
    eta_HP_1 = eta_Lorentz_1*T_sink_1/(T_sink_1-T_source_1)
    np.savetxt(output_folder + "\\eta_HP_1.csv", eta_HP_1, delimiter=".")

    # Heat pump 2, group 1 COP #

    #Load meteorological data
    try:
        T_source_2 = np.genfromtxt(input_folder + "\\T_source_HP_2.csv")
    except OSError:
        T_source_2 = np.genfromtxt(os.path.realpath(os.path.join(input_folder,  "Outside_temperature.csv")))
    T_source_2 = T_source_2 + 273.15
    # Heat sink temperature [°C]
    T_sink2 = val_list[2]
    T_sink_2 = T_sink2 + 273.15
    # Lorenz efficiency
    eta_Lorentz_2 = 0.6
    eta_HP_2 = eta_Lorentz_2*(T_sink_2)/(T_sink_2-T_source_2)


    np.savetxt(output_folder + "\\eta_HP_2.csv", eta_HP_2, delimiter=".")

    # Heat pump 3, group 1 COP #

    # Load meteorological data
    try:
        T_source_3 = np.genfromtxt(input_folder + "\\T_source_HP_3.csv")
    except OSError:
        T_source_3 = np.genfromtxt(os.path.realpath(os.path.join(input_folder, "Outside_temperature.csv")))
    T_source_3 = T_source_3+273.15
    # Heat sink temperature [°C]
    T_sink3 = val_list[4]
    T_sink_3 = T_sink3 + 273.15
    # Lorenz efficiency
    eta_Lorentz_3 = val_list[5]
    eta_HP_3 = eta_Lorentz_3*T_sink_3/(T_sink_3-T_source_3)

    np.savetxt(output_folder + "\\eta_HP_3.csv", eta_HP_3, delimiter=".")

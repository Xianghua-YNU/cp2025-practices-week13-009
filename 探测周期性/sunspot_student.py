#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
太阳黑子周期性分析 - 学生代码模板

请根据项目说明实现以下函数，完成太阳黑子效率与最优温度的计算。
"""

import numpy as np
import matplotlib.pyplot as plt

def load_sunspot_data(url):
    """
    从本地文件读取太阳黑子数据
    
    参数:
        url (str): 本地文件路径
        
    返回:
        tuple: (years, sunspots) 年份和太阳黑子数
    """
    # TODO: 使用np.loadtxt读取数据，只保留第2(年份)和3(太阳黑子数)列
    data = np.loadtxt(url, usecols=(0, 1, 3))  # 只读取第0(年份)、1(月份)、3(太阳黑子数)列
    years = data[:, 0] + (data[:, 1] - 1)/12.0  # 将年份转换为小数形式
    sunspots = data[:, 2]  # 第3列是太阳黑子数
    return years, sunspots

def plot_sunspot_data(years, sunspots):
    """
    绘制太阳黑子数据随时间变化图
    
    参数:
        years (numpy.ndarray): 年份数组
        sunspots (numpy.ndarray): 太阳黑子数数组
    """
    # TODO: 实现数据可视化
    plt.figure(figsize=(12, 6))
    plt.plot(years, sunspots)
    plt.xlabel('Year')
    plt.ylabel('Sunspot Number')
    plt.title('Sunspot Numbers Over Time')
    plt.grid(True)
    plt.show()
    
def compute_power_spectrum(sunspots):
    """
    计算太阳黑子数据的功率谱
    
    参数:
        sunspots (numpy.ndarray): 太阳黑子数数组
        
    返回:
        tuple: (frequencies, power) 频率数组和功率谱
    """
    # TODO: 实现傅里叶变换和功率谱计算
    N = len(sunspots)
    # 执行傅里叶变换
    fft_result = np.fft.fft(sunspots)
    # 计算功率谱 (取绝对值平方)
    power = np.abs(fft_result)**2
    # 生成对应的频率数组
    frequencies = np.fft.fftfreq(N)
    # 只返回正频率部分
    positive_freq = frequencies > 0
    return frequencies, power

def plot_power_spectrum(frequencies, power):
    """
    绘制功率谱图
    
    参数:
        frequencies (numpy.ndarray): 频率数组
        power (numpy.ndarray): 功率谱数组
    """
    # TODO: 实现功率谱可视化
    plt.figure(figsize=(12, 6))
    plt.plot(frequencies, power)
    plt.xlabel('Frequency (1/month)')
    plt.ylabel('Power')
    plt.title('Power Spectrum of Sunspot Numbers')
    plt.grid(True)
    plt.show()

def find_main_period(frequencies, power):
    """
    找出功率谱中的主周期
    
    参数:
        frequencies (numpy.ndarray): 频率数组
        power (numpy.ndarray): 功率谱数组
        
    返回:
        float: 主周期（月）
    """
    # TODO: 实现主周期检测
    # 忽略高频噪声（前几个点）
    mask = (frequencies > 0) & (frequencies < 0.1)
    power = power[mask]
    frequencies = frequencies[mask]
    
    # 找到功率谱中的最大峰值
    max_power_index = np.argmax(power)
    main_frequency = frequencies[max_power_index]
    # 计算对应的周期
    main_period = 1 / main_frequency
    return main_period

def main():
    # 数据文件路径
    data = "sunspot_data.txt"
    
    # 1. 加载并可视化数据
    years, sunspots = load_sunspot_data(data)
    plot_sunspot_data(years, sunspots)
    
    # 2. 傅里叶变换分析
    frequencies, power = compute_power_spectrum(sunspots)
    plot_power_spectrum(frequencies, power)
    
    # 3. 确定主周期
    main_period = find_main_period(frequencies, power)
    print(f"\nMain period of sunspot cycle: {main_period:.2f} months")
    print(f"Approximately {main_period/12:.2f} years")

if __name__ == "__main__":
    main()

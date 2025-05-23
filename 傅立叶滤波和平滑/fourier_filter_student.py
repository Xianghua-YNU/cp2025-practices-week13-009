
import os
def get_desktop_path():
    """获取Windows桌面路径"""
    return os.path.join(os.path.expanduser('~'), 'Desktop')

"""
傅立叶滤波和平滑 - 道琼斯工业平均指数分析

本模块实现了对道Jones工业平均指数数据的傅立叶分析和滤波处理。
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'KaiTi', 'Arial'] 
plt.rcParams['axes.unicode_minus'] = False  
def load_data(filename):
    """
    加载道Jones工业平均指数数据
    
    参数:
        filename (str): 数据文件路径
    
    返回:
        numpy.ndarray: 指数数组
    """
    # TODO: 实现数据加载功能 (约5行代码)
    # [STUDENT_CODE_HERE]
    # 提示: 使用np.loadtxt加载数据文件，处理可能的异常
    
    try:
        # 构建桌面文件路径
        desktop = get_desktop_path()
        file_path = os.path.join(desktop, filename)
        
        # 验证文件存在性
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"文件 {file_path} 不存在")
            
        data = np.loadtxt(file_path)
        return data
    except Exception as e:
        print(f"数据加载失败: {str(e)}")
        raise
    
 def plot_data(data, title="道琼斯工业平均指数"):
    """绘制时间序列数据（保证返回Figure对象）"""
    try:
        fig = plt.figure(figsize=(12, 6))
        plt.plot(data, color='navy', linewidth=1, label='原始数据')
        plt.title(title, fontsize=14)
        plt.xlabel("时间 (交易日)", fontsize=12)
        plt.ylabel("指数值", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.tight_layout()
        return fig
    except Exception as e:
        print(f"绘图错误: {e}")
        return plt.figure()  # 保证始终返回Figure对象  


def fourier_filter(data, keep_fraction=0.1):
    """
    执行傅立叶变换并滤波
    
    参数:
        data (numpy.ndarray): 输入数据数组
        keep_fraction (float): 保留的傅立叶系数比例
    
    返回:
        tuple: (滤波后的数据数组, 原始傅立叶系数数组)
    """
    # TODO: 实现傅立叶滤波功能 (约15行代码)
    # [STUDENT_CODE_HERE]
    # 提示: 
    # 1. 使用np.fft.rfft计算实数傅立叶变换
    # 2. 根据keep_fraction计算保留的系数数量
    # 3. 创建滤波后的系数数组
    # 4. 使用np.fft.irfft计算逆变换
    
    fft_coeff = np.fft.rfft(data)
    
    # 计算保留系数
    n_coeff = len(fft_coeff)
    keep_num = int(keep_fraction * n_coeff)
    
    # 创建滤波系数数组
    filtered_coeff = np.zeros_like(fft_coeff)
    filtered_coeff[:keep_num] = fft_coeff[:keep_num]
    
    # 逆变换重构信号
    filtered_data = np.fft.irfft(filtered_coeff, n=len(data))
    
    return filtered_data, fft_coeff

def plot_comparison(original, filtered, title="傅立叶滤波结果"):
    """
    绘制原始数据和滤波结果的比较
    
    参数:
        original (numpy.ndarray): 原始数据数组
        filtered (numpy.ndarray): 滤波后的数据数组
        title (str): 图表标题
    
    返回:
        None
    """
    # TODO: 实现数据比较可视化 (约15行代码)
    # [STUDENT_CODE_HERE]
    # 提示: 
    # 1. 使用不同颜色绘制原始和滤波数据
    # 2. 添加图例、标签和标题
    # 3. 使用plt.grid添加网格线
    try：

        fig = plt.figure(figsize=(12, 6))
        plt.plot(original, color='blue', alpha=0.4, linewidth=1, label='原始数据')
        plt.plot(filtered, color='red', linewidth=2, label='滤波结果')
        plt.title(title, fontsize=14)
        plt.xlabel("时间 (交易日)", fontsize=12)
        plt.ylabel("指数值", fontsize=12)
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        return fig
    except Exception as e:
        print(f"比较图错误: {e}")
        return plt.figure()
    

def main():
    # 任务1：数据加载与可视化
    data = load_data('dow.txt')
    figs = []
    figs.append(plot_data(data, "原始道琼斯指数数据"))
    # 任务2：傅立叶变换与滤波（保留前10%系数）
    filtered_10, coeff = fourier_filter(data, 0.1)
    figs.append(plot_comparison(data, filtered_10, "保留前10%系数"))
    
    # 任务3：修改滤波参数（保留前2%系数）
    filtered_2, _ = fourier_filter(data, 0.02)
    figs.append(plot_comparison(data, filtered_2, "保留前2%系数"))
    plt.show()
if __name__ == "__main__":
    main()

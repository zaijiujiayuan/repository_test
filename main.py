from hardware.sdr_source import SDRSource
from signal_processing.fft_analyzer import FFTAnalyzer
import matplotlib.pyplot as plt

def main():
    sample_rate = 2_000_000

    sdr = SDRSource(sample_rate)
    samples = sdr.read_samples(4096)

    analyzer = FFTAnalyzer(sample_rate)
    freq, mag = analyzer.compute_fft(samples)

    peak_f, peak_m = analyzer.find_peak_frequency(freq, mag)

    print(f"Peak Frequency: {peak_f:.2f} Hz")

    plt.plot(freq[:len(freq)//2], mag[:len(mag)//2])
    plt.title("FFT Spectrum MVP")
    plt.show()

if __name__ == "__main__":
    main()
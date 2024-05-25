import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

sizes = []
with open('file_sizes.txt', 'r') as f:
    for line in f:
        try:
            size = int(line.strip())
            sizes.append(size)
        except ValueError:
            print(f"Skipping invalid line: {line.strip()}")

data = pd.DataFrame(sizes, columns=['size'])

data = data[data['size'] > 0]

print(data.describe())

percentiles = [50, 75, 90, 95]
percentile_values = data['size'].quantile([p/100 for p in percentiles])
print(percentile_values)

total_files = len(data)
small_files = data[data['size'] <= 1024]  # файли <= 1KB
medium_files = data[(data['size'] > 1024) & (data['size'] <= 1048576)]  # файли від 1KB до 1MB
large_files = data[data['size'] > 1048576]  # файли > 1MB

print(f"Маленькі файли: {len(small_files)/total_files:.2%}")
print(f"Середні файли: {len(medium_files)/total_files:.2%}")
print(f"Великі файли: {len(large_files)/total_files:.2%}")

plt.figure(figsize=(10, 6))
plt.hist(data['size'], bins=100, log=True)
plt.xlabel('Розмір файлу (байти)')
plt.ylabel('Кількість файлів (логарифмічна шкала)')
plt.title('Гістограма розмірів файлів у каталозі Democracy 4')
plt.show()

log_sizes = np.log10(data['size'])
log_bins = np.logspace(0, log_sizes.max(), num=10)
log_hist, log_bins = np.histogram(log_sizes, bins=log_bins)

plt.figure(figsize=(10, 6))
plt.plot(log_bins[:-1], log_hist, marker='o', color='b')
plt.xscale('log')
plt.yscale('linear')
plt.xlabel('Log Size')
plt.ylabel('Frequency')
plt.title('Log Size Distribution')
plt.show()

size_categories = ['>0', '>10', '>100', '>1000', '>10000', '>100000']
sizes_count = [
    (data['size'] > 0).sum(),
    (data['size'] > 10).sum(),
    (data['size'] > 100).sum(),
    (data['size'] > 1000).sum(),
    (data['size'] > 10000).sum(),
    (data['size'] > 100000).sum()
]

plt.figure(figsize=(10, 6))
plt.pie(sizes_count, labels=size_categories, autopct='%1.2f%%')
plt.title('Розподіл розмірів файлів')
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(log_sizes, bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Log Frequency')
plt.ylabel('Count')
plt.title('Histogram of Log Frequencies')
plt.show()

plt.figure(figsize=(10, 6))
plt.boxplot(log_sizes, vert=False, patch_artist=True)
plt.xlabel('Log Frequency')
plt.title('Boxplot of Log Frequencies')
plt.show()

sorted_sizes = np.sort(data['size'])
cdf = np.arange(len(sorted_sizes)) / float(len(sorted_sizes))

plt.figure(figsize=(10, 6))
plt.plot(sorted_sizes, cdf, marker='.', linestyle='none')
plt.xlabel('File Size Frequency')
plt.ylabel('CDF')
plt.title('Cumulative Distribution Function of File Size Frequencies')
plt.show()
